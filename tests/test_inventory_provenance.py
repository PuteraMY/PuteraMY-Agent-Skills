#!/usr/bin/env python3
"""Regression tests for the non-destructive inventory; no vendor/runtime certification."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "inventory_provenance.py"

class InventoryProvenanceTests(unittest.TestCase):
    def test_tracked_files_and_unverified_status(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "scripts").mkdir()
            (root / "scripts" / "inventory_provenance.py").write_bytes(SOURCE.read_bytes())
            skill = root / ".agents" / "skills" / "original"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: original\ndescription: Test fixture\n---\n", encoding="utf-8")
            (skill / "LICENSE").write_text("fixture only\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
            result = subprocess.run([sys.executable, str(root / "scripts" / "inventory_provenance.py"), "--json"],
                                    cwd=root, check=True, capture_output=True, text=True)
            data = json.loads(result.stdout)
            self.assertEqual(data["skill_directories"], 1)
            self.assertEqual(data["frontmatter_failures"], [])
            self.assertEqual(data["entries"][0]["tracked_files"], ["LICENSE", "SKILL.md"])
            self.assertTrue(data["entries"][0]["contains_license_named_file"])
            for key in ("upstream_complete", "codex_discovered", "work_connected"):
                self.assertEqual(data["entries"][0][key], "UNVERIFIED")

    def test_malformed_local_guide_not_certified(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "scripts").mkdir()
            (root / "scripts" / "inventory_provenance.py").write_bytes(SOURCE.read_bytes())
            skill = root / ".agents" / "skills" / "local"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("PuteraMY-authored integration guide; not an official upstream skill\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
            result = subprocess.run([sys.executable, str(root / "scripts" / "inventory_provenance.py"), "--json"],
                                    cwd=root, check=True, capture_output=True, text=True)
            data = json.loads(result.stdout)
            self.assertEqual(data["frontmatter_failures"], ["local"])
            self.assertEqual(data["local_guide_candidates"], 1)
            self.assertEqual(data["entries"][0]["upstream_complete"], "UNVERIFIED")

if __name__ == "__main__":
    unittest.main()
