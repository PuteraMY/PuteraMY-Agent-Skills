"""Regression tests for complete committed Git tree inventory.

No GitHub access, vendor installation, or upstream provenance is implied.
"""
import importlib.util
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "inventory_git_tree.py"
spec = importlib.util.spec_from_file_location("inventory_git_tree", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class GitTreeInventoryTests(TestCase):
    def test_includes_trees_blobs_submodules_and_unicode_paths(self):
        records = (
            b"040000 tree " + b"a" * 40 + b"\t.agents\0"
            + b"100644 blob " + b"b" * 40 + b"\t.agents/skills/caf\xc3\xa9/SKILL.md\0"
            + b"160000 commit " + b"c" * 40 + b"\tvendor/submodule\0"
        )
        with patch.object(module, "git", side_effect=[b"d" * 40 + b"\n", records]) as mocked:
            result = module.inventory("HEAD")
        self.assertEqual(result["entry_count"], 3)
        self.assertEqual(result["tree_count"], 1)
        self.assertEqual(result["blob_count"], 1)
        self.assertEqual(result["submodule_count"], 1)
        self.assertEqual(result["entries"][1]["path"], ".agents/skills/caf\u00e9/SKILL.md")
        self.assertFalse(result["truncated"])
        self.assertEqual(mocked.call_args_list[1].args[:3], ("ls-tree", "-r", "-t"))

    def test_empty_tree_is_not_misrepresented_as_upstream_verification(self):
        with patch.object(module, "git", side_effect=[b"f" * 40 + b"\n", b""]):
            result = module.inventory("HEAD")
        self.assertEqual(result["entry_count"], 0)
        self.assertIn("not upstream provenance", result["scope"])
        self.assertEqual(result["entries"], [])
