"""Exercise the bundled tools as users invoke them, with disposable repositories."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(prefix="daedalus-test-")
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "example.py").write_text(
            "class Example:\n    pass\n\ndef normal(value):\n    return value\n"
            "\nasync def async_function(item):\n    return item\n"
        )
        (self.source / "README.md").write_text("Fixture documentation.\n")
        (self.source / "ignored.bin").write_bytes(b"\x00\xff")

    def run_tool(self, name, *args):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / name), *map(str, args)],
            cwd=self.root, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_mapper_includes_python_outline_and_ignores_selected_directories(self):
        ignored = self.source / "node_modules"
        ignored.mkdir()
        (ignored / "excluded.py").write_text("def hidden(): pass\n")
        output = self.root / "map.md"
        self.run_tool("map_directory.py", self.source, output,
                      '--ignore_dirs=["node_modules"]')
        text = output.read_text()
        for expected in ["example.py", "class Example:", "normal(value)",
                         "async_function(item)", "README.md"]:
            self.assertIn(expected, text)
        self.assertNotIn("node_modules", text)
        self.assertNotIn("hidden()", text)

    def test_directory_ingestion_preserves_content_and_filters_extensions(self):
        output = self.root / "content.txt"
        self.run_tool("ingest_content.py", self.source, output,
                      '--extensions=[".py"]')
        text = output.read_text()
        self.assertIn("--- Start of example.py ---", text)
        self.assertIn((self.source / "example.py").read_text(), text)
        self.assertNotIn("Fixture documentation", text)
        self.assertNotIn("ignored.bin", text)

    def test_repository_ingestion_clones_selected_branch(self):
        def git(*args):
            subprocess.run(["git", "-C", str(self.source), *args], check=True,
                           capture_output=True, text=True)

        git("init", "-b", "fixture")
        git("add", "example.py", "README.md", "ignored.bin")
        git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
            "commit", "-m", "Fixture")
        output = self.root / "repo.txt"
        self.run_tool("ingest_github_repo.py", f"--repo_url={self.source.as_uri()}",
                      f"--output_file={output}", "--branch=fixture",
                      '--extensions=["md"]')
        text = output.read_text()
        self.assertIn("==== START OF README.md ====", text)
        self.assertIn("Fixture documentation.", text)
        self.assertNotIn("example.py", text)

    def test_every_tool_exposes_command_help(self):
        for name in ["map_directory.py", "ingest_content.py", "ingest_github_repo.py"]:
            with self.subTest(tool=name):
                result = self.run_tool(name, "--help")
                self.assertIn("output_file", (result.stdout + result.stderr).lower())

    def test_mapper_skips_symlinks_and_its_own_output(self):
        (self.source / "cycle").symlink_to(self.source, target_is_directory=True)
        external = self.root / "external.py"
        external.write_text("def outside_secret(): pass\n")
        (self.source / "external.py").symlink_to(external)
        output = self.source / "map.md"
        self.run_tool("map_directory.py", self.source, output)
        text = output.read_text()
        for excluded in ["outside_secret", "external.py", "cycle", "map.md"]:
            self.assertNotIn(excluded, text)
        self.assertIn("example.py", text)

    def test_directory_ingestion_skips_symlinks_and_existing_output(self):
        external = self.root / "external.py"
        external.write_text("PRIVATE_FIXTURE\n")
        (self.source / "external.py").symlink_to(external)
        output = self.source / "content.md"
        output.write_text("PREVIOUS_OUTPUT\n")
        self.run_tool("ingest_content.py", self.source, output)
        text = output.read_text()
        self.assertNotIn("PRIVATE_FIXTURE", text)
        self.assertNotIn("content.md", text)
        self.assertNotIn("PREVIOUS_OUTPUT", text)
        self.assertIn("Fixture documentation.", text)


if __name__ == "__main__":
    unittest.main()
