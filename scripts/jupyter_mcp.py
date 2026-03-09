#!/usr/bin/env python3
"""
Start JupyterLab with the token expected by the MCP server config.

Usage:
    uv run scripts/jupyter_mcp.py

The MCP server (jupyter-mcp-server) is launched on-demand by the MCP client
(Claude Code, GitHub Copilot) via the config in .claude/settings.json and
.vscode/mcp.json. This script only needs to start the Jupyter server.

Token and port must match the values in the MCP config files.
"""
import os
import subprocess
import sys
from pathlib import Path

# Load .env if present (simple key=value parsing, no extra dependencies)
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

TOKEN = os.environ.get("JUPYTER_TOKEN", "grimp-local-token")
PORT = int(os.environ.get("JUPYTER_PORT", "8888"))


def main() -> None:
    cmd = [
        sys.executable, "-m", "jupyter", "lab",
        f"--port={PORT}",
        f"--IdentityProvider.token={TOKEN}",
        "--ip=127.0.0.1",
        "--no-browser",
        "--notebook-dir=.",
    ]
    print(f"Starting JupyterLab on http://127.0.0.1:{PORT}/?token={TOKEN}")
    print(f"MCP clients should connect to: http://localhost:{PORT} with token {TOKEN!r}")
    print("Press Ctrl+C to stop.\n")
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nShutting down JupyterLab.")


if __name__ == "__main__":
    main()
