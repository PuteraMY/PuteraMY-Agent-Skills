#!/usr/bin/env python3
"""Static inventory and structural checks; never certifies upstream or installation."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import subprocess
import sys

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable inventory")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    base = root / ".agents" / "skills"
    if not base.is_dir():
        print("ERROR: .agents/skills is missing", file=sys.stderr)
        return 2
    folders = sorted(p for p in base.iterdir() if p.is_dir())
    rows = []
    failures = []
    if not folders:
        failures.append("No skill directories found; empty inventory is not a passing audit")
    for folder in folders:
        entry = folder / "SKILL.md"
        files = sorted(p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file())
        valid = False
        if entry.is_file():
            body = entry.read_text(encoding="utf-8-sig")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", body, flags=re.DOTALL)
            if match:
                header = match.group(1)
                valid = all(re.search(rf"(?m)^{field}:\s*\S+", header) for field in ("name", "description"))
        if not valid:
            failures.append(f"{folder.name}: missing or malformed SKILL.md frontmatter")
        rows.append({"directory": folder.name, "entrypoint_valid": valid, "file_count": len(files), "files": files})
    try:
        tracked = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True).stdout.decode("utf-8", errors="replace").split("\0")
        tracked = sorted(x for x in tracked if x)
    except (OSError, subprocess.CalledProcessError):
        tracked = None
    result = {"status": "PASS" if not failures else "FAIL", "scope": "local structural checks only", "skills": rows, "tracked_file_count": len(tracked) if tracked is not None else None, "tracked_paths": tracked, "failures": failures, "upstream_verified": False, "codex_installed": False, "work_installed": False}
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"{result['status']}: {len(rows)} skill directories; {len(failures)} structural failures; tracked files: {result['tracked_file_count'] if tracked is not None else 'unavailable'}")
        for failure in failures:
            print("ERROR:", failure, file=sys.stderr)
        print("NOTE: this does not validate complete upstream distributions, licenses, plugin manifests, runtime discovery, or installation.")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
