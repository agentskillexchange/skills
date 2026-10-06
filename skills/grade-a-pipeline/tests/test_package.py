from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_remote_push_is_opt_in(self):
        source = (ROOT / "examples/grade-a-pipeline.workflow.js").read_text()
        self.assertRegex(source, r"const PUSH = args\?\.push === true")
        self.assertRegex(source, r"const PUSH_AGENT_BRANCHES = args\?\.pushAgentBranches === true")
        self.assertNotRegex(source, r"const PUSH = args\?\.push !== false")

    def test_no_private_paths(self):
        text = (ROOT / "SKILL.md").read_text() + (ROOT / "examples/grade-a-pipeline.workflow.js").read_text()
        self.assertNotIn("/" + "Users" + "/", text)
        self.assertNotIn("Ant" + "reas", text)


if __name__ == "__main__":
    unittest.main()
