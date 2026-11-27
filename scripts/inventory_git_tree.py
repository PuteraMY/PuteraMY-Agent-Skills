#!/usr/bin/env python3
"""Read-only complete committed Git tree inventory; no provenance/runtime claims."""
from __future__ import annotations
import argparse
import json
import subprocess
import sys

def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], check=True, capture_output=True).stdout

def inventory(ref: str) -> dict:
    commit = git("rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    raw = git("ls-tree", "-r", "-t", "-z", commit)
    entries = []
    for record in filter(None, raw.split(b"\0")):
        meta, path = record.split(b"\t", 1)
        mode, kind, sha = meta.decode("ascii").split()
        entries.append({"path": path.decode("utf-8", "surrogateescape"), "mode": mode, "type": kind, "object_sha": sha})
    return {
        "ref": ref, "commit": commit, "truncated": False,
        "scope": "committed Git objects only; not upstream provenance or runtime installation",
        "entry_count": len(entries),
        "blob_count": sum(e["type"] == "blob" for e in entries),
        "tree_count": sum(e["type"] == "tree" for e in entries),
        "submodule_count": sum(e["type"] == "commit" for e in entries),
        "entries": entries,
    }

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        result = inventory(args.ref)
    except (OSError, subprocess.CalledProcessError, UnicodeError, ValueError) as exc:
        print(f"ERROR: cannot inventory committed tree: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        print(f"{result['commit']}: {result['entry_count']} tree entries, {result['blob_count']} blobs, {result['tree_count']} trees, {result['submodule_count']} submodules")
        print("NOTE: no upstream completeness, plugin status, Codex discovery or Work connection verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
