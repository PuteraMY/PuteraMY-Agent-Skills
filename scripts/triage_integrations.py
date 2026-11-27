#!/usr/bin/env python3
"""Conservative local entrypoint triage; never claims upstream or runtime installation."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents" / "skills"
FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)
GUIDE = re.compile(r"PuteraMY-authored|locally authored|not a copy of the upstream|not an installed copy|integration guide|not an official", re.I)
MCP = re.compile(r"\bMCP\b|model context protocol", re.I)
PLUGIN = re.compile(r"\bplugin\b", re.I)

def triage(base: Path = BASE) -> dict:
    entries = []
    for folder in sorted(p for p in base.iterdir() if p.is_dir()):
        entry = folder / "SKILL.md"
        body = entry.read_text(encoding="utf-8-sig") if entry.is_file() else ""
        match = FRONT.match(body)
        valid = bool(match and all(re.search(rf"(?m)^{key}:[ \t]*[^ \t\r\n#][^\r\n]*", match.group(1)) for key in ("name", "description")))
        guide = bool(GUIDE.search(body))
        manifests = sorted(p.relative_to(folder).as_posix() for p in folder.rglob("plugin.json") if p.is_file())
        entries.append({
            "directory": folder.name,
            "valid_skill_frontmatter": valid,
            "local_guide_evidence": guide,
            "plugin_manifest_paths": manifests,
            "mentions_mcp": bool(MCP.search(body)),
            "mentions_plugin": bool(PLUGIN.search(body)),
            "classification": "local_integration_guide" if guide else ("skill_entrypoint_candidate" if valid else "unresolved"),
            "upstream_distribution_complete": "UNVERIFIED",
            "codex_installed": "UNVERIFIED",
            "work_connected": "UNVERIFIED",
        })
    return {"scope": "local evidence only; mentions are not proof of plugin or MCP installation",
            "entries": entries,
            "unresolved_or_guides": [e["directory"] for e in entries if e["classification"] != "skill_entrypoint_candidate"]}

if __name__ == "__main__":
    print(json.dumps(triage(), indent=2, ensure_ascii=False))
