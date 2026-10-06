from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("scan_uis", ROOT / "scan_uis.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class LocalUITests(unittest.TestCase):
    def test_dashboard_escapes_service_metadata(self):
        path = MODULE.build([{
            "port": 8000,
            "title": "<script>alert(1)</script>",
            "cmd": "<server>",
            "pid": "7",
            "status": 200,
        }])
        html = path.read_text()
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", html)
        self.assertIn("&lt;server&gt;", html)

    def test_private_installation_names_are_absent(self):
        text = (ROOT / "SKILL.md").read_text() + (ROOT / "scan_uis.py").read_text()
        for value in (
            "Ant" + "reas",
            "Hepha" + "estus",
            "/" + "Users" + "/",
            "~/" + ".claude",
        ):
            self.assertNotIn(value, text)


if __name__ == "__main__":
    unittest.main()
