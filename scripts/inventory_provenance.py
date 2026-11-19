#!/usr/bin/env python3
"""Non-destructive evidence inventory. Does NOT certify upstream provenance or runtime installation."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents" / "skills"
FRONT = re.compile(r"\\A---\\r?\\n(.*?)\\r?\\n---(?:\\r?\\n|\\Z)", re.S)
URL = re.compile(r"https?://[^\\s)<>\\]\"']+")
FIELDS = ("name", "description")

def tracked_paths():
    proc = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True)
    return sorted(x for x in proc.stdout.decode("utf-8", "replace").split("\\0") if x)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    paths = tracked_paths()
    rows = []
    for folder in sorted(p for p in BASE.iterdir() if p.is_dir()):
        prefix = folder.relative_to(ROOT).as_posix() + "/"
        files = [p[len(prefix):] for p in paths if p.startswith(prefix)]
        entry = folder / "SKILL.md"
        body = entry.read_text(encoding="utf-8-sig") if entry.is_file() else ""
        match = FRONT.match(body)
        valid = bool(match and all(re.search(rf"(?m)^{field}:[ \\t]*[^ \\t\\r\\n#][^\\r\\n]*", match.group(1)) for field in FIELDS))
        guide = bool(re.search(r"PuteraMY-authored|not a copy of the upstream|not an official|integration guide", body, re.I))
        rows.append({
            "directory": folder.name,
            "tracked_files": files,
            "entrypoint_frontmatter_valid": valid,
            "self_identifies_local_guide": guide,
            "source_urls_in_entrypoint": sorted(set(URL.findall(body))),
            "contains_license_named_file": any(Path(p).name.lower().startswith(("license", "licence", "copying")) for p in files),
            "contains_plugin_manifest": any(Path(p).name in ("plugin.json", "marketplace.json") for p in files),
            "upstream_complete": "UNVERIFIED",
            "codex_discovered": "UNVERIFIED",
            "work_connected": "UNVERIFIED"
        })
    output = {"scope": "tracked local tree, not upstream or runtime verification",
              "tracked_file_count": len(paths), "skill_directories": len(rows),
              "local_guide_candidates": sum(r["self_identifies_local_guide"] for r in rows),
              "frontmatter_failures": [r["directory"] for r in rows if not r["entrypoint_frontmatter_valid"]],
              "entries": rows}
    if args.json:
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print(f"{len(rows)} directories, {len(paths)} tracked files; {output['local_guide_candidates']} local-guide candidates")
        print("Invalid frontmatter:", ", ".join(output["frontmatter_failures"]) or "none")
        print("NOT VERIFIED: upstream completeness, licenses, Codex discovery, Work connections")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
