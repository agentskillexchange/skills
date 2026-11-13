from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicPackageTests(unittest.TestCase):
    def test_no_project_specific_identifiers(self):
        text = "\n".join(
            (ROOT / relative).read_text(errors="ignore")
            for relative in (
                "SKILL.md",
                "references/bootstrap.md",
                "assets/gcp-keyless-observe.yml",
                "scripts/doctor.py",
                "scripts/validate_workflow.py",
            )
        ).lower()
        for value in (
            "axi" + "otic",
            "/" + "users" + "/",
            "ant" + "reas",
            "hepha" + "estus",
        ):
            self.assertNotIn(value, text)

    def test_workflow_has_no_generic_shell_input(self):
        workflow = (ROOT / "assets/gcp-keyless-observe.yml").read_text()
        self.assertNotIn("command:", workflow)
        self.assertNotIn("script:", workflow)


if __name__ == "__main__":
    unittest.main()
