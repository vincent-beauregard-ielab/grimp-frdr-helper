"""Globus transfer utility for FRDR datasets.

Downloads files from a published FRDR Globus endpoint to the local machine,
and uploads a local dataset folder to an FRDR deposit endpoint.

Requires:
- Globus Connect Personal installed and running on the local machine (for
  download/upload subcommands). Not needed for ls, status, or https-download.
- GLOBUS_CLIENT_ID set in the environment or .env file.
  Register a Native App at https://developers.globus.org to get a client ID.

Token cache: ~/.grimp_globus_tokens.json (refreshed automatically).

NOTE (Windows / Git Bash): paths starting with / are mangled by MSYS2 before
Python sees them. Prefix commands with MSYS_NO_PATHCONV=1 to avoid this:
  MSYS_NO_PATHCONV=1 python -m utils.globus_transfer ls <endpoint> --path /13/...
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

TOKEN_CACHE = Path.home() / ".grimp_globus_tokens.json"
TRANSFER_SCOPE = "urn:globus:auth:scope:transfer.api.globus.org:all"


# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def _load_client_id() -> str:
    client_id = os.environ.get("GLOBUS_CLIENT_ID", "").strip()
    if not client_id:
        sys.exit(
            "Error: GLOBUS_CLIENT_ID not set.\n"
            "Register a Native App at https://developers.globus.org and add\n"
            "GLOBUS_CLIENT_ID=<your-id> to your .env file."
        )
    return client_id


def _load_tokens() -> dict[str, Any] | None:
    if TOKEN_CACHE.exists():
        try:
            return json.loads(TOKEN_CACHE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return None


def _save_tokens(tokens: dict[str, Any]) -> None:
    TOKEN_CACHE.write_text(json.dumps(tokens, indent=2), encoding="utf-8")
    TOKEN_CACHE.chmod(0o600)


def get_transfer_client() -> Any:
    """Return an authenticated TransferClient, refreshing tokens as needed."""
    try:
        import globus_sdk
    except ImportError:
        sys.exit("Error: globus-sdk is not installed. Run: pip install globus-sdk")

    client_id = _load_client_id()
    auth_client = globus_sdk.NativeAppAuthClient(client_id)

    cached = _load_tokens()

    # Try to use cached refresh token
    if cached and cached.get("refresh_token"):
        try:
            auth_client.oauth2_start_flow(requested_scopes=TRANSFER_SCOPE, refresh_tokens=True)
            response = auth_client.oauth2_refresh_token(cached["refresh_token"])
            tokens = response.by_resource_server.get("transfer.api.globus.org", {})
            if tokens:
                _save_tokens({
                    "access_token": tokens["access_token"],
                    "refresh_token": tokens.get("refresh_token", cached["refresh_token"]),
                    "expires_at": tokens.get("expires_at_seconds"),
                })
                return globus_sdk.TransferClient(
                    authorizer=globus_sdk.AccessTokenAuthorizer(tokens["access_token"])
                )
        except Exception:
            pass  # Fall through to interactive login

    # Interactive browser-based login
    auth_client.oauth2_start_flow(requested_scopes=TRANSFER_SCOPE, refresh_tokens=True)
    authorize_url = auth_client.oauth2_get_authorize_url()
    print(f"\nOpen this URL in your browser to authenticate with Globus:\n\n  {authorize_url}\n")
    auth_code = input("Paste the authorization code here: ").strip()

    token_response = auth_client.oauth2_exchange_code_for_tokens(auth_code)
    tokens = token_response.by_resource_server.get("transfer.api.globus.org", {})
    if not tokens:
        sys.exit("Error: Could not obtain transfer tokens.")

    _save_tokens({
        "access_token": tokens["access_token"],
        "refresh_token": tokens.get("refresh_token", ""),
        "expires_at": tokens.get("expires_at_seconds"),
    })

    return globus_sdk.TransferClient(
        authorizer=globus_sdk.AccessTokenAuthorizer(tokens["access_token"])
    )


def get_local_endpoint_id() -> str:
    """Return the local Globus Connect Personal endpoint ID."""
    try:
        import globus_sdk
    except ImportError:
        sys.exit("Error: globus-sdk is not installed. Run: pip install globus-sdk")

    local = globus_sdk.LocalGlobusConnectPersonal()
    endpoint_id = local.endpoint_id
    if not endpoint_id:
        sys.exit(
            "Error: Could not find a local Globus Connect Personal endpoint.\n"
            "Install and start Globus Connect Personal: https://www.globus.org/globus-connect-personal"
        )
    return endpoint_id


# ---------------------------------------------------------------------------
# LS
# ---------------------------------------------------------------------------

def cmd_ls(args: argparse.Namespace) -> None:
    """List files on a Globus endpoint path."""
    tc = get_transfer_client()
    path = args.path
    print(f"Listing {args.endpoint}:{path}")
    for entry in tc.operation_ls(args.endpoint, path=path, limit=args.limit):
        kind = "D" if entry["type"] == "dir" else "F"
        size = f"{entry.get('size', 0):>12}" if entry["type"] != "dir" else "           -"
        print(f"  [{kind}] {size}  {entry['name']}")


# ---------------------------------------------------------------------------
# HTTPS download (no Globus Connect Personal required)
# ---------------------------------------------------------------------------

def cmd_https_download(args: argparse.Namespace) -> None:
    """Download a single file from a GCSv5 endpoint via HTTPS (no GCP needed)."""
    import urllib.request

    tc = get_transfer_client()
    source_path = args.source_path
    dest_dir = Path(args.dest_dir).resolve()
    dest_dir.mkdir(parents=True, exist_ok=True)

    ep = tc.get_endpoint(args.source_endpoint)
    https_server = ep.get("https_server")
    if not https_server:
        sys.exit("Error: this endpoint does not support HTTPS downloads.")

    tokens = _load_tokens()
    if not tokens:
        sys.exit("Error: no cached tokens — run ls first to authenticate.")
    access_token = tokens["access_token"]

    url = f"{https_server.rstrip('/')}{source_path}"
    filename = source_path.rsplit("/", 1)[-1]
    dest_file = dest_dir / filename

    print(f"Downloading {url}")
    print(f"         -> {dest_file}")

    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(req) as response, open(dest_file, "wb") as out:
        total = int(response.headers.get("Content-Length", 0))
        downloaded = 0
        while True:
            data = response.read(65536)
            if not data:
                break
            out.write(data)
            downloaded += len(data)
            if total:
                print(f"\r  {downloaded:,} / {total:,} bytes ({downloaded/total*100:.0f}%)", end="", flush=True)
    print(f"\nDone: {dest_file}")


# ---------------------------------------------------------------------------
# Download (requires Globus Connect Personal)
# ---------------------------------------------------------------------------

def cmd_download(args: argparse.Namespace) -> None:
    """Transfer files from an FRDR Globus endpoint to the local machine."""
    import globus_sdk

    source_endpoint = args.source_endpoint
    source_path = args.source_path.rstrip("/")
    dest_dir = Path(args.dest_dir).resolve()
    label = args.label or f"FRDR download: {source_path}"

    tc = get_transfer_client()
    local_endpoint = get_local_endpoint_id()

    dest_dir.mkdir(parents=True, exist_ok=True)

    # List source to decide if it's a file or directory
    try:
        list(tc.operation_ls(source_endpoint, path=source_path, limit=1))
        is_dir = True
    except globus_sdk.TransferAPIError:
        is_dir = False

    task = globus_sdk.TransferData(
        source_endpoint_id=source_endpoint,
        destination_endpoint_id=local_endpoint,
        label=label,
        sync_level="checksum",
        notify_on_succeeded=False,
        notify_on_failed=True,
    )

    if is_dir:
        dest_name = source_path.rsplit("/", 1)[-1]
        task.add_item(source_path, str(dest_dir / dest_name), recursive=True)
        print(f"Queuing recursive transfer: {source_path}/ -> {dest_dir / dest_name}/")
    else:
        filename = source_path.rsplit("/", 1)[-1]
        task.add_item(source_path, str(dest_dir / filename))
        print(f"Queuing file transfer: {source_path} -> {dest_dir / filename}")

    result = tc.submit_transfer(task)
    task_id = result["task_id"]
    print(f"Transfer submitted. Task ID: {task_id}")

    if args.wait:
        _wait_for_task(tc, task_id)


# ---------------------------------------------------------------------------
# Upload (requires Globus Connect Personal)
# ---------------------------------------------------------------------------

def cmd_upload(args: argparse.Namespace) -> None:
    """Transfer a local directory to an FRDR deposit Globus endpoint."""
    import globus_sdk

    source_dir = Path(args.source_dir).resolve()
    if not source_dir.exists():
        sys.exit(f"Error: source directory does not exist: {source_dir}")

    dest_endpoint = args.dest_endpoint
    dest_path = args.dest_path.rstrip("/")
    label = args.label or f"FRDR upload: {source_dir.name}"

    tc = get_transfer_client()
    local_endpoint = get_local_endpoint_id()

    task = globus_sdk.TransferData(
        source_endpoint_id=local_endpoint,
        destination_endpoint_id=dest_endpoint,
        label=label,
        sync_level="checksum",
        notify_on_succeeded=False,
        notify_on_failed=True,
    )

    task.add_item(str(source_dir), dest_path, recursive=True)
    print(f"Queuing upload: {source_dir}/ -> {dest_path}/")

    result = tc.submit_transfer(task)
    task_id = result["task_id"]
    print(f"Transfer submitted. Task ID: {task_id}")

    if args.wait:
        _wait_for_task(tc, task_id)


# ---------------------------------------------------------------------------
# Status
# ---------------------------------------------------------------------------

def cmd_status(args: argparse.Namespace) -> None:
    """Check the status of a Globus transfer task."""
    tc = get_transfer_client()
    task = tc.get_task(args.task_id)
    status = task["status"]
    label = task.get("label", "")
    nice_status = task.get("nice_status", "")
    print(f"Task {args.task_id}: {status}")
    if label:
        print(f"  Label:  {label}")
    if nice_status and nice_status != status:
        print(f"  Detail: {nice_status}")
    if status == "SUCCEEDED":
        print(f"  Files:  {task.get('files_transferred', '?')} transferred")
    elif status == "FAILED":
        print(f"  Error:  {task.get('fatal_error', {}).get('description', 'unknown')}")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _wait_for_task(tc: Any, task_id: str, timeout: int = 3600, poll: int = 15) -> None:
    print(f"Waiting for task {task_id} (timeout {timeout}s, polling every {poll}s)...")
    start = time.monotonic()
    while time.monotonic() - start < timeout:
        task = tc.get_task(task_id)
        status = task["status"]
        elapsed = int(time.monotonic() - start)
        print(f"  [{elapsed:4d}s] {status} -- {task.get('nice_status', '')}")
        if status in ("SUCCEEDED", "FAILED"):
            if status == "SUCCEEDED":
                print(f"Done. {task.get('files_transferred', '?')} file(s) transferred.")
            else:
                print(f"Transfer failed: {task.get('fatal_error', {}).get('description', 'unknown')}")
            return
        time.sleep(poll)
    print(f"Timeout after {timeout}s. Task may still be running: {task_id}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Globus transfer utility for FRDR datasets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
NOTE: On Windows/Git Bash, prefix with MSYS_NO_PATHCONV=1 to prevent path mangling.

Examples:
  # List files on an FRDR endpoint
  MSYS_NO_PATHCONV=1 python -m utils.globus_transfer ls \\
      150c306f-4bcb-414f-9a82-fdd039cde793 \\
      --path /13/published/publication_1413/submitted_data/

  # Download a single file via HTTPS (no Globus Connect Personal needed)
  MSYS_NO_PATHCONV=1 python -m utils.globus_transfer https-download \\
      --source-endpoint 150c306f-4bcb-414f-9a82-fdd039cde793 \\
      --source-path /13/published/publication_1413/submitted_data/README.txt \\
      --dest-dir datasets/example_3/

  # Download a full dataset (requires Globus Connect Personal)
  MSYS_NO_PATHCONV=1 python -m utils.globus_transfer download \\
      --source-endpoint 150c306f-4bcb-414f-9a82-fdd039cde793 \\
      --source-path /13/published/publication_1413/submitted_data \\
      --dest-dir datasets/example_3/ --wait

  # Upload a local frdr_data/ directory to an FRDR deposit
  python -m utils.globus_transfer upload \\
      --source-dir datasets/my_dataset/frdr_data \\
      --dest-endpoint <frdr-deposit-endpoint-id> \\
      --dest-path /submission/my_dataset --wait

  # Check transfer status
  python -m utils.globus_transfer status <task-id>
""",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ls
    p_ls = sub.add_parser("ls", help="List files on a Globus endpoint")
    p_ls.add_argument("endpoint", help="Globus endpoint/collection UUID")
    p_ls.add_argument("--path", default="/", help="Remote path to list (default: /)")
    p_ls.add_argument("--limit", type=int, default=100, help="Max entries (default: 100)")

    # https-download
    p_hd = sub.add_parser("https-download", help="Download a file via HTTPS (no GCP needed)")
    p_hd.add_argument("--source-endpoint", required=True, help="FRDR Globus endpoint UUID")
    p_hd.add_argument("--source-path", required=True, help="Remote file path")
    p_hd.add_argument("--dest-dir", required=True, help="Local destination directory")

    # download
    p_dl = sub.add_parser("download", help="Download files via Globus Transfer (requires GCP)")
    p_dl.add_argument("--source-endpoint", required=True, help="FRDR Globus endpoint UUID")
    p_dl.add_argument("--source-path", required=True, help="Remote path (file or directory)")
    p_dl.add_argument("--dest-dir", required=True, help="Local destination directory")
    p_dl.add_argument("--label", default="", help="Transfer task label")
    p_dl.add_argument("--wait", action="store_true", help="Wait for transfer to complete")

    # upload
    p_ul = sub.add_parser("upload", help="Upload local files to FRDR (requires GCP)")
    p_ul.add_argument("--source-dir", required=True, help="Local directory to upload")
    p_ul.add_argument("--dest-endpoint", required=True, help="FRDR deposit Globus endpoint UUID")
    p_ul.add_argument("--dest-path", required=True, help="Remote destination path")
    p_ul.add_argument("--label", default="", help="Transfer task label")
    p_ul.add_argument("--wait", action="store_true", help="Wait for transfer to complete")

    # status
    p_st = sub.add_parser("status", help="Check status of a transfer task")
    p_st.add_argument("task_id", help="Globus task ID")

    return parser


def main() -> None:
    # Load .env if present
    env_file = Path(".env")
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "ls": cmd_ls,
        "https-download": cmd_https_download,
        "download": cmd_download,
        "upload": cmd_upload,
        "status": cmd_status,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
