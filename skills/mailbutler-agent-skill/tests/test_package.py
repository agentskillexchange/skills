import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [
    path
    for path in ROOT.rglob("*")
    if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
]


class PackageTests(unittest.TestCase):
    def test_required_release_files_exist(self):
        for relative in (
            "SKILL.md",
            "README.md",
            "LICENSE",
            "SECURITY.md",
            "CONTRIBUTING.md",
            "agents/openai.yaml",
            "references/security-contract.md",
            "scripts/judgment_tools.py",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_frontmatter_is_agent_skills_compatible(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: mailbutler\ndescription: "))
        self.assertEqual(skill.split("---", 2)[1].count("\nname:"), 1)
        self.assertNotIn("[TODO", skill)

    def test_private_provenance_and_vendor_routing_are_absent(self):
        joined = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in TEXT_FILES)
        for forbidden in (
            "Syner" + "gram",
            "Codex-" + "sonnet",
            "antreas" + "@",
            "axiotic" + ".ai",
            "antri" + "kohs",
            "EC-" + "FRONTIER",
            "Neur" + "IPS",
        ):
            self.assertNotIn(forbidden, joined)

    def test_no_real_looking_email_addresses(self):
        pattern = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)
        for path in TEXT_FILES:
            for address in pattern.findall(path.read_text(encoding="utf-8", errors="ignore")):
                self.assertTrue(address.endswith(".invalid"), f"{path}: {address}")


if __name__ == "__main__":
    unittest.main()
