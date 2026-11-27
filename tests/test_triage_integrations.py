"""Regression tests for conservative integration classification."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "triage_integrations.py"
spec = importlib.util.spec_from_file_location("triage_integrations", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class TriageTests(unittest.TestCase):
    def test_local_guide_is_not_mistaken_for_installed_skill(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "context7"
            folder.mkdir()
            (folder / "SKILL.md").write_text("# Context7 MCP\nThis is a locally authored integration guide, not an installed copy.", encoding="utf-8")
            row = module.triage(Path(temp))["entries"][0]
            self.assertEqual(row["classification"], "local_integration_guide")
            self.assertFalse(row["valid_skill_frontmatter"])
            self.assertTrue(row["mentions_mcp"])
            self.assertEqual(row["work_connected"], "UNVERIFIED")

    def test_valid_entrypoint_is_only_candidate(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "example"
            folder.mkdir()
            (folder / "SKILL.md").write_text("---\nname: example\ndescription: Real entrypoint\n---\n", encoding="utf-8")
            row = module.triage(Path(temp))["entries"][0]
            self.assertEqual(row["classification"], "skill_entrypoint_candidate")
            self.assertEqual(row["upstream_distribution_complete"], "UNVERIFIED")
            self.assertEqual(row["codex_installed"], "UNVERIFIED")

    def test_manifest_does_not_prove_plugin_installed(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / "example"
            (folder / ".claude-plugin").mkdir(parents=True)
            (folder / "SKILL.md").write_text("---\nname: example\ndescription: Test\n---\n", encoding="utf-8")
            (folder / ".claude-plugin" / "plugin.json").write_text("{}", encoding="utf-8")
            row = module.triage(Path(temp))["entries"][0]
            self.assertEqual(row["plugin_manifest_paths"], [".claude-plugin/plugin.json"])
            self.assertEqual(row["work_connected"], "UNVERIFIED")

if __name__ == "__main__":
    unittest.main()
