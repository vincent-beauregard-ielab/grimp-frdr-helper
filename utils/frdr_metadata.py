from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

USER_AGENT = "grimp-frdr-helper/0.1"
DEFAULT_TIMEOUT = 30


class DatasetPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, list[str]] = {}
        self.json_ld_blocks: list[str] = []
        self._in_json_ld = False
        self._current_json_ld: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value for key, value in attrs if value is not None}
        if tag == "meta":
            name = attr_map.get("name")
            content = attr_map.get("content")
            if name and content:
                self.meta.setdefault(name, []).append(content)
        elif tag == "script" and attr_map.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._current_json_ld = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._current_json_ld.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_json_ld:
            self.json_ld_blocks.append("".join(self._current_json_ld).strip())
            self._in_json_ld = False
            self._current_json_ld = []


@dataclass
class FileListConfig:
    api_path: str
    base_path: str
    endpoint_id: str
    item_id: str
    collection_id: str


def parse_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        value = value.strip()
        if value.startswith(("\"", "'")) and value.endswith(("\"", "'")):
            value = value[1:-1]
        data[key.strip()] = value
    return data


def fetch_text(url: str) -> tuple[str, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        body = response.read().decode("utf-8", errors="replace")
        return body, response.geturl()


def fetch_json(url: str, params: dict[str, Any] | None = None) -> Any:
    if params:
        url = f"{url}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8"))


def resolve_landing_page(about: dict[str, str]) -> str:
    doi = about.get("doi", "").strip()
    doi_url = about.get("doi_url", "").strip()
    frdr_url = about.get("frdr_url", "").strip()

    candidates = []
    if doi_url:
        candidates.append(doi_url)
    if doi:
        candidates.append(f"https://doi.org/{doi}")
    if frdr_url and "/repo/dataset/" in frdr_url:
        candidates.append(frdr_url)

    for candidate in candidates:
        try:
            _, final_url = fetch_text(candidate)
        except Exception:
            continue
        if "/repo/dataset/" in final_url:
            return final_url

    if frdr_url and "/repo/dataset/" in frdr_url:
        return frdr_url

    raise RuntimeError("Could not resolve an FRDR landing page from the dataset metadata.")


def parse_page(html_text: str) -> tuple[DatasetPageParser, dict[str, Any]]:
    parser = DatasetPageParser()
    parser.feed(html_text)

    dataset_jsonld: dict[str, Any] = {}
    for block in parser.json_ld_blocks:
        try:
            candidate = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(candidate, list):
            for item in candidate:
                if isinstance(item, dict) and item.get("@type") == "Dataset":
                    dataset_jsonld = item
                    break
        elif isinstance(candidate, dict) and candidate.get("@type") == "Dataset":
            dataset_jsonld = candidate
        if dataset_jsonld:
            break

    return parser, dataset_jsonld


def extract_filelist_config(html_text: str) -> FileListConfig | None:
    filelist_match = re.search(
        r"new FileList\('(?P<api>[^']+)',\s*true,\s*'(?P<path>[^']+)'",
        html_text,
    )
    endpoint_match = re.search(r"setGlobusEndpoint\('(?P<endpoint>[^']+)'\)", html_text)
    item_match = re.search(r"setItem\('(?P<item>[^']+)'\)", html_text)
    collection_match = re.search(r"setCollection\('(?P<collection>[^']+)'\)", html_text)

    if not all([filelist_match, endpoint_match, item_match, collection_match]):
        return None

    return FileListConfig(
        api_path=filelist_match.group("api"),
        base_path=filelist_match.group("path"),
        endpoint_id=endpoint_match.group("endpoint"),
        item_id=item_match.group("item"),
        collection_id=collection_match.group("collection"),
    )


def normalize_creator(author: dict[str, Any]) -> dict[str, Any]:
    affiliation = author.get("affiliation")
    if isinstance(affiliation, str):
        affiliations = [item.strip() for item in affiliation.split(";") if item.strip()]
    elif isinstance(affiliation, list):
        affiliations = [str(item).strip() for item in affiliation if str(item).strip()]
    else:
        affiliations = []

    creator: dict[str, Any] = {
        "name": author.get("name"),
        "affiliations": affiliations,
    }
    author_url = author.get("url")
    if isinstance(author_url, str) and "orcid.org" in author_url:
        creator["orcid"] = author_url.rsplit("/", 1)[-1]
        creator["orcid_url"] = author_url
    return creator


def extract_license_name(html_text: str) -> str | None:
    match = re.search(
        r"Access to this dataset is subject to the following terms:</div>\s*<div class=\"card-body\">\s*([^<]+)",
        html_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        return unescape(match.group(1)).strip()
    return None


def extract_related_identifiers(html_text: str, landing_page_url: str) -> list[dict[str, str]]:
    related: list[dict[str, str]] = []
    collection_match = re.search(
        r"Appears in Collections:</td><td class=\"metadataFieldValue\"><a href=\"(?P<href>[^\"]+)\">(?P<title>[^<]+)</a>",
        html_text,
    )
    if collection_match:
        related.append(
            {
                "relation_type": "isPartOf",
                "identifier": urljoin(landing_page_url, collection_match.group("href")),
                "title": unescape(collection_match.group("title")).strip(),
            }
        )
    return related


def list_dataset_files(landing_page_url: str, config: FileListConfig) -> list[dict[str, Any]]:
    api_url = urljoin(landing_page_url, config.api_path)
    root_path = f"{config.base_path.rstrip('/')}/submitted_data/"

    def request(path: str) -> dict[str, Any]:
        return fetch_json(
            api_url,
            {
                "item_id": config.item_id,
                "collection_id": config.collection_id,
                "endpoint_id": config.endpoint_id,
                "path": path,
                "limit": 100,
                "offset": 0,
            },
        )

    root = request(root_path)
    results: list[dict[str, Any]] = []

    for entry in root.get("files", []):
        results.append(
            {
                "path": relative_dataset_path(entry["name"], root_path),
                "type": "file",
                "size_bytes": entry.get("size"),
                "last_modified": entry.get("lastModified"),
            }
        )

    for folder in root.get("folders", []):
        folder_path = folder["name"]
        folder_summary: dict[str, Any] = {
            "path": relative_dataset_path(folder_path, root_path),
            "type": "folder",
            "children_count": folder.get("size"),
            "last_modified": folder.get("lastModified"),
        }

        nested = request(f"{folder_path.rstrip('/')}/")
        child_entries: list[dict[str, Any]] = []
        for child_file in nested.get("files", []):
            child_entries.append(
                {
                    "path": relative_dataset_path(child_file["name"], root_path),
                    "type": "file",
                    "size_bytes": child_file.get("size"),
                    "last_modified": child_file.get("lastModified"),
                }
            )
        for child_folder in nested.get("folders", []):
            child_entries.append(
                {
                    "path": relative_dataset_path(child_folder["name"], root_path),
                    "type": "folder",
                    "children_count": child_folder.get("size"),
                    "last_modified": child_folder.get("lastModified"),
                }
            )
        if child_entries:
            folder_summary["children"] = child_entries
        results.append(folder_summary)

    return results


def relative_dataset_path(full_path: str, root_path: str) -> str:
    normalized_root = root_path.rstrip("/") + "/"
    if full_path.startswith(normalized_root):
        return f"submitted_data/{full_path[len(normalized_root):]}".rstrip("/")
    return full_path.rstrip("/")


def extract_metadata(about: dict[str, str]) -> dict[str, Any]:
    landing_page_url = resolve_landing_page(about)
    html_text, _ = fetch_text(landing_page_url)
    parser, dataset_jsonld = parse_page(html_text)
    config = extract_filelist_config(html_text)

    meta = parser.meta
    creators = [
        normalize_creator(author)
        for author in dataset_jsonld.get("author", [])
        if isinstance(author, dict)
    ]

    keywords = dataset_jsonld.get("keywords")
    if not keywords:
        keywords = meta.get("citation_keywords", [""])[0].split(";")
    keywords = [unescape(str(keyword)).strip() for keyword in keywords if str(keyword).strip()]

    identifier = dataset_jsonld.get("identifier", {})
    doi_value = about.get("doi") or ""
    if not doi_value and isinstance(identifier, dict):
        raw_doi = str(identifier.get("value", "")).strip()
        doi_value = raw_doi.removeprefix("https://doi.org/")

    metadata: dict[str, Any] = {
        "title": unescape(dataset_jsonld.get("name") or meta.get("citation_title", [""])[0]).strip(),
        "description": unescape(dataset_jsonld.get("description") or meta.get("DC.description", [""])[0]).strip(),
        "creators": creators,
        "keywords": keywords,
        "publisher": unescape(
            (
                dataset_jsonld.get("publisher", {}) or {}
            ).get("name", meta.get("citation_publisher", [""])[0])
        ).strip(),
        "publication_date": dataset_jsonld.get("datePublished") or meta.get("citation_date", [""])[0],
        "license": {
            "name": extract_license_name(html_text),
            "url": dataset_jsonld.get("license") or meta.get("DC.rights", [""])[0],
        },
        "doi": doi_value,
        "files": list_dataset_files(landing_page_url, config) if config else [],
        "related_identifiers": extract_related_identifiers(html_text, landing_page_url),
    }

    metadata["source"] = {
        "frdr_landing_page": landing_page_url,
    }
    return metadata


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch structured dataset metadata from a public FRDR record.")
    parser.add_argument("metadata_file", type=Path, help="Path to the dataset METADATA.yaml file")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the extracted metadata as JSON",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    about = parse_simple_yaml(args.metadata_file)
    metadata = extract_metadata(about)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
