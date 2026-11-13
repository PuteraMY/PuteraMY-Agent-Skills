"""Isolated smoke tests for the repository's structural validator.

These tests do not certify upstream provenance or installation.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

VALIDATOR = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(VALIDATOR, self.root / "scripts" / "validate_skills.py")
        self.skill = self.root / ".agents" / "skills" / "example"
        self.skill.mkdir(parents=True)

    def run_validator(self):
        proc = subprocess.run(
            [sys.executable, str(self.root / "scripts" / "validate_skills.py"), "--json"],
            capture_output=True, text=True, check=False
        )
        return proc, json.loads(proc.stdout)

    def test_valid_entrypoint_does_not_claim_installation(self):
        (self.skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: Test\n---\n", encoding="utf-8"
        )
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["skills"][0]["file_count"], 1)
        self.assertFalse(result["upstream_verified"])
        self.assertFalse(result["codex_installed"])
        self.assertFalse(result["work_installed"])

    def test_invalid_frontmatter_fails(self):
        (self.skill / "SKILL.md").write_text("not a skill", encoding="utf-8")
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(len(result["failures"]), 1)

    def test_empty_inventory_fails(self):
        self.skill.rmdir()
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("No skill directories", result["failures"][0])

    def test_frontmatter_keys_must_be_actual_fields(self):
        (self.skill / "SKILL.md").write_text(
            "---\nnotname: fake\ndescription: Test\n---\n", encoding="utf-8"
        )
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(result["status"], "FAIL")

    def test_frontmatter_values_cannot_be_empty(self):
        (self.skill / "SKILL.md").write_text(
            "---\nname: \ndescription: Test\n---\n", encoding="utf-8"
        )
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(result["status"], "FAIL")

    def test_missing_entrypoint_fails(self):
        (self.skill / "reference.md").write_text("support", encoding="utf-8")
        proc, result = self.run_validator()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(result["skills"][0]["files"], ["reference.md"])


if __name__ == "__main__":
    unittest.main()
