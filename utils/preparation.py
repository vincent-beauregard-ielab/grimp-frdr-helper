"""Reusable file-operation primitives for FRDR dataset preparation notebooks.

Notebooks orchestrate per-dataset preparation; this module provides the
small, dataset-agnostic toolkit they import: file ops that emit FileRecords,
and a TransformLog accumulator that renders human-readable markdown for the
data preparation report. No JSON manifest is produced here.
"""

from __future__ import annotations

import shutil
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class FileRecord:
    category: str
    role: str  # "scientific" | "support"
    source: str  # relative path (POSIX-style)
    target: str  # relative path (POSIX-style)
    transform: str  # "copy_and_rename" | "copy_and_restructure" | "docx_to_txt"
    source_size: int
    target_size: int


def _rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def normalize_text_file(path: Path) -> None:
    """Normalize a text file in place: CRLF→LF, strip trailing whitespace, ensure final newline."""
    text = path.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n")).strip()
    path.write_text(normalized + "\n", encoding="utf-8")


def copy_and_rename(
    src: Path,
    dest: Path,
    *,
    category: str,
    relative_to: Path,
    role: str = "scientific",
) -> FileRecord:
    """Copy a single file to a new path/name. Returns a FileRecord."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return FileRecord(
        category=category,
        role=role,
        source=_rel(src, relative_to),
        target=_rel(dest, relative_to),
        transform="copy_and_rename",
        source_size=src.stat().st_size,
        target_size=dest.stat().st_size,
    )


def copy_directory_files(
    src_dir: Path,
    dest_dir: Path,
    *,
    category: str,
    relative_to: Path,
    pattern: str = "*",
    lowercase_names: bool = True,
    role: str = "scientific",
) -> list[FileRecord]:
    """Copy every file in src_dir matching pattern into dest_dir.

    Files are sorted by path for deterministic ordering. When
    lowercase_names is True, target file names are lowercased.
    """
    records: list[FileRecord] = []
    for src in sorted(p for p in src_dir.glob(pattern) if p.is_file()):
        target_name = src.name.lower() if lowercase_names else src.name
        dest = dest_dir / target_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        records.append(
            FileRecord(
                category=category,
                role=role,
                source=_rel(src, relative_to),
                target=_rel(dest, relative_to),
                transform="copy_and_restructure",
                source_size=src.stat().st_size,
                target_size=dest.stat().st_size,
            )
        )
    return records


def docx_to_txt(
    src: Path,
    dest: Path,
    *,
    category: str,
    relative_to: Path,
    role: str = "support",
    cwd: Path | None = None,
) -> FileRecord:
    """Convert a DOCX file to UTF-8 plain text via pandoc, then normalize line endings."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(src), "-t", "plain", "-o", str(dest)],
        check=True,
        cwd=str(cwd) if cwd is not None else None,
    )
    normalize_text_file(dest)
    return FileRecord(
        category=category,
        role=role,
        source=_rel(src, relative_to),
        target=_rel(dest, relative_to),
        transform="docx_to_txt",
        source_size=src.stat().st_size,
        target_size=dest.stat().st_size,
    )


class TransformLog:
    """Accumulator for FileRecords. Renders human-readable markdown — no JSON."""

    def __init__(self) -> None:
        self._records: list[FileRecord] = []

    def add(self, record: FileRecord) -> None:
        self._records.append(record)

    def extend(self, records: Iterable[FileRecord]) -> None:
        self._records.extend(records)

    @property
    def records(self) -> list[FileRecord]:
        return list(self._records)

    def __len__(self) -> int:
        return len(self._records)

    def summary(self) -> dict:
        """Aggregate counts by transform, by category, by role; total sizes."""
        grouped: dict[str, list[FileRecord]] = defaultdict(list)
        for r in self._records:
            grouped[r.category].append(r)

        category_summary: dict[str, dict] = {}
        for category, items in grouped.items():
            category_summary[category] = {
                "count": len(items),
                "size_mb": round(sum(i.target_size for i in items) / 1_000_000, 2),
                "roles": dict(Counter(i.role for i in items)),
            }

        return {
            "total_files": len(self._records),
            "transform_counts": dict(Counter(r.transform for r in self._records)),
            "category_summary": category_summary,
            "total_target_bytes": sum(r.target_size for r in self._records),
        }

    def to_markdown_table(self) -> str:
        """Full per-file transformation log as a markdown table."""
        header = "| Category | Transform | Source | Target |\n|---|---|---|---|"
        rows = [
            f"| {r.category} | {r.transform} | `{r.source}` | `{r.target}` |"
            for r in self._records
        ]
        return "\n".join([header, *rows])

    def category_summary_markdown(self) -> str:
        """Per-category summary table ready to paste into the data preparation report."""
        summary = self.summary()["category_summary"]
        header = "| Category | Files | Size (MB) | Roles |\n|---|---:|---:|---|"
        rows = []
        for category in sorted(summary):
            entry = summary[category]
            roles = ", ".join(f"{role}: {count}" for role, count in sorted(entry["roles"].items()))
            rows.append(f"| {category} | {entry['count']} | {entry['size_mb']} | {roles} |")
        return "\n".join([header, *rows])

    def as_dicts(self) -> list[dict]:
        return [asdict(r) for r in self._records]
