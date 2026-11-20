import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "judgment_tools.py"
SPEC = importlib.util.spec_from_file_location("judgment_tools", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def judgment(*, surface=True, score=80, action="see", more=False):
    return {
        "surface": surface,
        "score": score,
        "reasons": ["time-sensitive project context"],
        "recommendedAction": action,
        "needMoreContext": more,
    }


class JudgmentTests(unittest.TestCase):
    def test_lede_with_reply(self):
        items = [judgment(action="seeAndReply"), judgment(action="see"), judgment(surface=False, score=5, action="nothing")]
        self.assertEqual(MODULE.lede(items), "2 emails worth your time, 1 suggested reply — 1 handled quietly.")

    def test_empty_surface_lede(self):
        items = [judgment(surface=False, score=5, action="nothing")]
        self.assertEqual(MODULE.lede(items), "Nothing needs you right now — 1 handled quietly.")

    def test_suppressed_mail_cannot_recommend_action(self):
        with self.assertRaisesRegex(ValueError, "suppressed mail"):
            MODULE.validate_judgment(judgment(surface=False, action="see"), 1)

    def test_draft_content_is_not_part_of_a_judgment(self):
        value = judgment(action="reply")
        value["draft"] = "Thanks for the note."
        with self.assertRaisesRegex(ValueError, "extra"):
            MODULE.validate_judgment(value, 1)

    def test_unknown_fields_fail_closed(self):
        value = judgment()
        value["recipient"] = "generated@example.invalid"
        with self.assertRaisesRegex(ValueError, "extra"):
            MODULE.validate_judgment(value, 1)

    def test_cli_validates_and_prints_lede(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "judgments.json"
            path.write_text(json.dumps([judgment(action="see")]), encoding="utf-8")
            result = subprocess.run([sys.executable, str(MODULE_PATH), str(path)], text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "1 email worth your time — 0 handled quietly.")


if __name__ == "__main__":
    unittest.main()
