"""Public regression suite using synthetic, isolated local evidence only."""
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest

import session_inventory

SCRIPTS = Path(__file__).resolve().parent


class BoundaryTests(unittest.TestCase):
    def run_cli(self, script, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)], capture_output=True, text=True)

    def test_no_implicit_home_scan(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_cli("session_inventory.py", "--root", folder)
            self.assertEqual(result.returncode, 2)
            self.assertIn("explicitly approved", result.stderr)

    def test_exclusive_private_output(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            store = root / "store"
            store.mkdir()
            output = root / "output.json"
            args = ("--root", root, "--codex-root", store, "--output", output)
            result = self.run_cli("session_inventory.py", *args)
            self.assertEqual(result.returncode, 0, result.stderr)
            original = output.read_bytes()
            self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)
            result = self.run_cli("session_inventory.py", *args)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_bytes(), original)

    def test_message_content_cannot_forge_project_association(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "session.jsonl"
            source.write_text(json.dumps({"type": "user", "cwd": str(root / "other"), "message": {"cwd": str(root / "project")}}) + "\n")
            self.assertIsNone(session_inventory.inspect_jsonl(source, "claude", root / "project"))

    def test_malformed_lines_are_counted_and_symlinks_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            store = root / "store"
            store.mkdir()
            raw = root / "source.jsonl"
            raw.write_text(json.dumps({"type": "session_meta", "payload": {"cwd": str(root)}}) + "\nnot-json\n")
            result = session_inventory.inspect_jsonl(raw, "codex", root)
            self.assertEqual(result["parse_errors"], 1)
            self.assertEqual(result["lines"], 2)
            (store / "linked.jsonl").symlink_to(raw)
            self.assertEqual(session_inventory.discover(store, "codex", root), [])

    def test_temporal_and_authority_manifest_rejections(self):
        valid = {"key": "test-choice", "title": "Synthetic choice", "occurred_at": "2026-01-01T00:00:00Z", "evidence_class": "WITNESSED", "claim": "Test only", "anchors": ["synthetic:L1"], "chronicle_verb": "decision", "inferred": False}
        variants = [
            dict(valid, occurred_at="2026-01-01T00:00:00"),
            dict(valid, chronicle_verb="arm"),
            dict(valid, chronicle_verb="landed"),
            dict(valid, anchors=[]),
            dict(valid, inferred=True),
            dict(valid, evidence_class="ARTIFACT-MEASURED"),
            dict(valid, chronicle_verb="correct"),
        ]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "manifest.json"
            for entry in [valid] + variants:
                path.write_text(json.dumps({"schema_version": 1, "project": "synthetic", "entries": [entry]}))
                result = self.run_cli("validate_manifest.py", path)
                self.assertEqual(result.returncode == 0, entry is valid, result.stderr)

    def test_inference_caveat_and_schema_type(self):
        entry = {"key": "synthetic", "title": "Test inference", "occurred_at": "2026-01-01T00:00:00Z", "evidence_class": "INFERRED INTENT", "claim": "Test interpretation", "anchors": ["synthetic:L1"], "chronicle_verb": "note", "inferred": True, "caveat": "INFERRED - NOT WITNESSED - MAY BE WRONG"}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "manifest.json"
            for schema, caveat, expected in (
                (1, entry["caveat"], 0),
                (True, entry["caveat"], 1),
                (1.0, entry["caveat"], 1),
                (1, "INFERRED and completely certain", 1),
                (1, "INFERRED - NOT WITNESSED", 1),
                (1, "MAY BE WRONG", 1),
            ):
                path.write_text(json.dumps({"schema_version": schema, "project": "synthetic", "entries": [dict(entry, caveat=caveat)]}))
                result = self.run_cli("validate_manifest.py", path)
                self.assertEqual(result.returncode, expected, result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_malformed_manifest_cli_has_clear_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "manifest.json"
            for content in ("{", "[]", "null", '{"schema_version": true}'):
                path.write_text(content)
                result = self.run_cli("validate_manifest.py", path)
                self.assertEqual(result.returncode, 1)
                self.assertIn("Invalid manifest", result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
