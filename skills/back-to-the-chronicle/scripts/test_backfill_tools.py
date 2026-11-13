#!/usr/bin/env python3
"""Synthetic local regression fixtures; these are not real project results."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import inventory
import session_inventory
import validate_manifest


class InventoryTests(unittest.TestCase):
    def test_inventory_preserves_tokenizers_but_hides_tokens(self) -> None:
        self.assertFalse(inventory.secretish("models/tokenizer/config.json"))
        self.assertTrue(inventory.secretish("runtime/token.txt"))
        self.assertTrue(inventory.secretish(".env.local"))

    def test_commits_are_chronological_and_secret_paths_are_omitted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.com"], check=True)
            (root / "CHRONICLE.md").write_text("start\n", encoding="utf-8")
            (root / "token.txt").write_text("not-a-real-secret\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "found"], check=True)
            result = inventory.commits(root)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["files"], ["CHRONICLE.md"])


class ManifestTests(unittest.TestCase):
    def run_manifest(self, data: dict[str, object]) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            original = validate_manifest.argparse.ArgumentParser.parse_args
            validate_manifest.argparse.ArgumentParser.parse_args = lambda self: type(
                "Args", (), {"manifest": path}
            )()
            try:
                self.assertEqual(validate_manifest.main(), 0)
            finally:
                validate_manifest.argparse.ArgumentParser.parse_args = original

    def test_accepts_witnessed_decision(self) -> None:
        self.run_manifest(
            {
                "schema_version": 1,
                "project": "example",
                "entries": [
                    {
                        "key": "direct-spot",
                        "title": "choose direct Spot VMs",
                        "occurred_at": "2026-08-01T12:00:00Z",
                        "evidence_class": "WITNESSED",
                        "claim": "Start with the smallest reliable controller.",
                        "anchors": ["thread:123", "docs/architecture/v0.md"],
                        "chronicle_verb": "decision",
                        "inferred": False,
                    }
                ],
            }
        )

    def test_rejects_inferred_decision(self) -> None:
        data = {
            "schema_version": 1,
            "project": "example",
            "entries": [
                {
                    "key": "guess",
                    "title": "guess a decision",
                    "occurred_at": "2026-08-01T12:00:00Z",
                    "evidence_class": "INFERRED INTENT",
                    "claim": "Maybe this was deliberate.",
                    "anchors": ["commit:abc"],
                    "chronicle_verb": "decision",
                    "inferred": True,
                    "caveat": "INFERRED - NOT WITNESSED - MAY BE WRONG",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "require witnessed intent"):
                original = validate_manifest.argparse.ArgumentParser.parse_args
                validate_manifest.argparse.ArgumentParser.parse_args = lambda self: type(
                    "Args", (), {"manifest": path}
                )()
                try:
                    validate_manifest.main()
                finally:
                    validate_manifest.argparse.ArgumentParser.parse_args = original


class SessionInventoryTests(unittest.TestCase):
    def test_indexes_matching_codex_and_claude_sessions_without_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            project = base / "project"
            project.mkdir()
            codex = base / "codex"
            claude = base / "claude"
            codex.mkdir()
            claude.mkdir()
            secret_marker = "do-not-copy-this-message"
            (codex / "rollout.jsonl").write_text(
                json.dumps(
                    {
                        "type": "session_meta",
                        "payload": {"id": "codex-1", "cwd": str(project)},
                        "timestamp": "2026-08-01T10:00:00Z",
                    }
                )
                + "\n"
                + json.dumps({"type": "message", "content": secret_marker})
                + "\n",
                encoding="utf-8",
            )
            (claude / "session.jsonl").write_text(
                json.dumps(
                    {
                        "type": "user",
                        "sessionId": "claude-1",
                        "cwd": str(project / "subdir"),
                        "timestamp": "2026-08-01T11:00:00Z",
                        "message": {"content": secret_marker},
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            result = session_inventory.build_inventory(project, codex, claude)
            encoded = json.dumps(result)
            self.assertEqual([item["source"] for item in result["sessions"]], ["codex", "claude"])
            self.assertNotIn(secret_marker, encoded)
            self.assertEqual(result["sessions"][0]["session_ids"], ["codex-1"])
            self.assertEqual(result["sessions"][1]["session_ids"], ["claude-1"])
            self.assertEqual(result["sessions"][0]["matched_lines"], [1])

    def test_excludes_session_for_another_project(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            project = base / "project"
            project.mkdir()
            codex = base / "codex"
            claude = base / "claude"
            codex.mkdir()
            claude.mkdir()
            (codex / "other.jsonl").write_text(
                json.dumps({"type": "session_meta", "payload": {"cwd": str(base / "other")}})
                + "\n",
                encoding="utf-8",
            )

            result = session_inventory.build_inventory(project, codex, claude)
            self.assertEqual(result["sessions"], [])


if __name__ == "__main__":
    unittest.main()
