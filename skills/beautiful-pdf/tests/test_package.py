from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_private_brand_and_delivery_paths_are_absent(self):
        text = "\n".join(
            (ROOT / relative).read_text(errors="ignore")
            for relative in (
                "SKILL.md",
                "references/style-guide.md",
                "references/doc-types.md",
                "scripts/pdf-to-png.py",
            )
        )
        self.assertNotIn("Axi" + "otic", text)
        self.assertNotIn("open" + "claw", text.lower())
        self.assertNotIn("/" + "Users" + "/", text)

    def test_required_assets_exist(self):
        for relative in (
            "SKILL.md",
            "assets/default.css",
            "references/style-guide.md",
            "references/doc-types.md",
            "scripts/pdf-to-png.py",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
