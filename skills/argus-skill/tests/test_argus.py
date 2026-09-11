from pathlib import Path
import json
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


class ArgusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.home = self.root / "home-archive"
        self.research = self.root / "research-archive"
        for name, archive in (("My Archivum", self.home), ("Research", self.research)):
            (archive / "00_meta").mkdir(parents=True)
            (archive / "config.yaml").write_text(
                textwrap.dedent(
                    f'''\
                    version: 2
                    workspace:
                      name: "{name}"
                      profile_file: "00_meta/workspace_profile.md"
                      state_file: "00_meta/workspace_state.md"
                    directories:
                      projects: "01_active_research"
                    '''
                )
            )
            (archive / "AGENTS.md").write_text("# Agent contract\n")
        (self.home / "01_projects" / "argus").mkdir(parents=True)
        (self.home / "01_projects" / "argus" / "README.md").write_text("# Argus\n")
        (self.research / "01_active_research" / "study").mkdir(parents=True)
        (self.research / "01_active_research" / "study" / "README.md").write_text(
            "# Study\n"
        )
        (self.home / "00_meta" / "cross_archive_index.md").write_text(
            "[Argus](archivum://my/01_projects/argus/README.md)\n"
            "[Study](archivum://research/01_active_research/study/README.md)\n"
        )
        (self.research / "00_meta" / "home_anchor.md").write_text(
            "[Home](archivum://my/00_meta/cross_archive_index.md)\n"
        )
        self.registry = self.home / "00_meta" / "archivum_registry.toml"
        self.registry.write_text(
            textwrap.dedent(
                f'''\
                version = 1
                home = "my"
                index = "00_meta/cross_archive_index.md"

                [archives.my]
                kind = "home"
                root = "{self.home}"

                [archives.research]
                kind = "research"
                root = "{self.research}"
                home_anchor = "00_meta/home_anchor.md"
                '''
            )
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_script(self, script: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_skill_uses_v2_config_and_composes_existing_systems(self) -> None:
        skill = (ROOT / "SKILL.md").read_text()
        self.assertIn("configured commitment system", skill)
        self.assertIn("configured budget authority", skill)
        self.assertIn("config.yaml", skill)
        self.assertIn("Never assume numbered directory names", skill)

    def test_discovery_reports_v2_config_and_agent_contract(self) -> None:
        result = self.run_script(
            "discover_archivums.py", "--registry", str(self.registry), "--json"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        research = next(item for item in payload["archives"] if item["name"] == "research")
        self.assertEqual(research["config_version"], 2)
        self.assertEqual(
            research["config_file"], str(Path(research["root"]) / "config.yaml")
        )
        self.assertEqual(research["agent_contracts"], ["AGENTS.md"])

    def test_backlink_target_cannot_escape_registered_archive(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text("private\n")
        index = self.home / "00_meta" / "cross_archive_index.md"
        index.write_text(
            index.read_text()
            + "[Escape](archivum://research/../outside.md)\n"
        )
        result = self.run_script(
            "check_backlinks.py", "--registry", str(self.registry)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("escapes archive root", result.stdout)

    def test_valid_backlinks_pass(self) -> None:
        result = self.run_script(
            "check_backlinks.py", "--registry", str(self.registry)
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
