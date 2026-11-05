"""Opt-in integration with an explicitly supplied public Chronicle checkout.

Set PUBLIC_CHRONICLE_SOURCE to its repository root. Only a disposable Git project
and disposable CHRONICLE_HOME are written; no hooks, network or narration run.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


@unittest.skipUnless(os.environ.get("PUBLIC_CHRONICLE_SOURCE"), "optional public Chronicle source not supplied")
class ChronicleCompatibilityTests(unittest.TestCase):
    def test_append_and_resume_preserve_inference_warning(self):
        source = Path(os.environ["PUBLIC_CHRONICLE_SOURCE"]).resolve()
        self.assertTrue((source / "src" / "chronicle" / "cli.py").is_file())
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            project = base / "project"
            project.mkdir()
            subprocess.run(["git", "init", "-q", str(project)], check=True)
            env = dict(os.environ, CHRONICLE_HOME=str(base / "ledger"), PYTHONPATH=str(source / "src"), CHRONICLE_SESSION="synthetic-integration", CHRONICLE_MACHINE="synthetic-machine", CHRONICLE_HARNESS="synthetic-test", PYTHONDONTWRITEBYTECODE="1")
            env.pop("CLAUDE_SESSION_ID", None)
            env.pop("CHRONICLE_OFF", None)

            def chron(*args):
                result = subprocess.run([sys.executable, "-m", "chronicle.cli", *args], cwd=project, env=env, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout

            chron("open", "Synthetic integration only", "--state", "No live project or provider touched")
            path = project / "CHRONICLE.md"
            first = path.read_bytes()
            warning = "INFERRED - NOT WITNESSED - MAY BE WRONG"
            chron("note", "Synthetic retrospective", "--state", warning + "; occurred_at=2026-01-01T00:00:00Z; anchor=synthetic:L1")
            self.assertTrue(path.read_bytes().startswith(first))
            self.assertIn(warning, path.read_text())
            self.assertIn(warning, chron("resume"))
            chron("close", "Synthetic test complete", "--not-done", "No historical ARM, external publication or hooks")
            self.assertIn("Synthetic test complete", path.read_text())


if __name__ == "__main__":
    unittest.main()
