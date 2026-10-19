"""Regression tests for privacy-safe cross-agent synchronization."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "agent_sync.py"
SPEC = importlib.util.spec_from_file_location("agent_sync", SCRIPT)
assert SPEC is not None
assert SPEC.loader is not None
AGENT_SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AGENT_SYNC)


def _event(event_id: str, summary: str) -> dict[str, object]:
    return {
        "version": AGENT_SYNC.SCHEMA_VERSION,
        "id": event_id,
        "timestamp": "2026-01-02T03:04:05Z",
        "source": "codex",
        "session_id": "test-session",
        "summary": summary,
        "decisions": [],
        "evidence": [],
        "completed": [],
        "next_actions": [],
        "blockers": [],
        "artifacts": [],
        "notes": [],
    }


def _update_args(**overrides: object) -> argparse.Namespace:
    values: dict[str, object] = {
        "from_json": None,
        "summary": "Verified release state.",
        "source": "codex",
        "session_id": "test-session",
        "decision": [],
        "evidence": [],
        "completed": [],
        "next_action": [],
        "blocker": [],
        "artifact": [],
        "note": [],
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class ProgressStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.project = Path(self.temporary_directory.name) / "public-project"
        self.project.mkdir()
        self.paths = AGENT_SYNC.ensure_store(self.project)

    def _write_events(self, *events: dict[str, object]) -> None:
        content = "".join(json.dumps(event) + "\n" for event in events)
        self.paths["events"].write_text(content, encoding="utf-8")

    def test_render_preserves_manual_suffix(self) -> None:
        first = _event("first", "Initial handoff")
        self._write_events(first)
        generated = AGENT_SYNC.render_progress(self.project, [first])
        manual = "\n# Release note\n\nHuman-authored context.\n"
        self.paths["progress"].write_text(generated + manual, encoding="utf-8")

        AGENT_SYNC.render_store(self.project)

        rendered = self.paths["progress"].read_text(encoding="utf-8")
        self.assertIn(manual.strip(), rendered)

    def test_render_refuses_edits_inside_generated_view(self) -> None:
        first = _event("first", "Initial handoff")
        self._write_events(first)
        generated = AGENT_SYNC.render_progress(self.project, [first])
        edited = generated.replace("Initial handoff", "Untracked edit", 1)
        self.paths["progress"].write_text(edited, encoding="utf-8")

        with self.assertRaisesRegex(RuntimeError, "Refusing to overwrite"):
            AGENT_SYNC.render_store(self.project)

        self.assertEqual(self.paths["progress"].read_text(encoding="utf-8"), edited)

    def test_append_is_idempotent_for_same_semantic_event(self) -> None:
        with mock.patch.object(AGENT_SYNC, "iso_utc", return_value="2026-01-01T00:00:00Z"):
            first = AGENT_SYNC.build_event(_update_args())
        with mock.patch.object(AGENT_SYNC, "iso_utc", return_value="2026-01-02T00:00:00Z"):
            retry = AGENT_SYNC.build_event(_update_args())

        self.assertEqual(first["id"], retry["id"])
        _, appended_first = AGENT_SYNC.append_event(self.project, first)
        _, appended_retry = AGENT_SYNC.append_event(self.project, retry)
        self.assertTrue(appended_first)
        self.assertFalse(appended_retry)
        self.assertEqual(len(AGENT_SYNC.load_events(self.paths["events"])), 1)

    def test_render_is_stable_and_does_not_leak_absolute_project_path(self) -> None:
        event = _event("first", "Initial handoff")
        first = AGENT_SYNC.render_progress(self.project, [event])
        second = AGENT_SYNC.render_progress(self.project, [event])

        self.assertEqual(first, second)
        self.assertIn("Project: `public-project`", first)
        self.assertNotIn(str(self.project), first)

    def test_malformed_curated_jsonl_fails_closed(self) -> None:
        self.paths["events"].write_text('{"version": 1}\nnot-json\n', encoding="utf-8")

        with self.assertRaisesRegex(RuntimeError, "unsupported event on line 1"):
            AGENT_SYNC.load_events(self.paths["events"])

        self.paths["events"].write_text("not-json\n", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "invalid JSON on line 1"):
            AGENT_SYNC.load_events(self.paths["events"])

    def test_store_repairs_missing_privacy_ignore_rules(self) -> None:
        self.paths["ignore"].write_text("custom-rule\n", encoding="utf-8")

        AGENT_SYNC.ensure_store(self.project)

        rules = self.paths["ignore"].read_text(encoding="utf-8").splitlines()
        self.assertEqual(rules, ["custom-rule", "imports/", "*.lock"])

    def test_import_output_outside_private_directory_is_rejected(self) -> None:
        args = argparse.Namespace(
            project=str(self.project),
            write=True,
            output=str(self.project / "packet.md"),
        )
        with mock.patch.object(AGENT_SYNC, "discover_sessions", return_value=[]):
            with self.assertRaisesRegex(SystemExit, "may only be written"):
                AGENT_SYNC.command_import(args)

    def test_generated_output_has_no_trailing_whitespace(self) -> None:
        event = _event("first", "Initial handoff")
        event["decisions"] = ["Keep the generated view clean."]

        rendered = AGENT_SYNC.render_progress(self.project, [event])

        trailing = [line for line in rendered.splitlines() if line != line.rstrip()]
        self.assertEqual(trailing, [])


class TranscriptParsingTest(unittest.TestCase):
    def test_claude_parser_keeps_text_and_excludes_tool_blocks(self) -> None:
        record = {
            "type": "assistant",
            "message": {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": "Visible answer"},
                    {"type": "tool_use", "text": "private payload"},
                ],
            },
        }

        self.assertEqual(
            AGENT_SYNC.message_from_record(record, "claude"),
            ("assistant", "Visible answer"),
        )

    def test_codex_parser_excludes_system_and_function_records(self) -> None:
        visible = {
            "type": "response_item",
            "payload": {
                "type": "message",
                "role": "assistant",
                "content": [{"type": "output_text", "text": "Visible answer"}],
            },
        }
        function_call = {
            "type": "response_item",
            "payload": {"type": "function_call", "arguments": "secret"},
        }

        self.assertEqual(
            AGENT_SYNC.message_from_record(visible, "codex"),
            ("assistant", "Visible answer"),
        )
        self.assertIsNone(AGENT_SYNC.message_from_record(function_call, "codex"))

    def test_known_generated_wrapper_is_filtered(self) -> None:
        record = {
            "type": "response_item",
            "payload": {
                "type": "message",
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "<environment_context>generated context</environment_context>",
                    }
                ],
            },
        }
        self.assertIsNone(AGENT_SYNC.message_from_record(record, "codex"))

    def test_malformed_source_jsonl_is_skipped_without_hiding_valid_records(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.jsonl"
            valid = {
                "type": "response_item",
                "timestamp": "2026-01-01T00:00:00Z",
                "payload": {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": "Project update"}],
                },
            }
            path.write_text("not-json\n" + json.dumps(valid) + "\n", encoding="utf-8")

            parsed = AGENT_SYNC.parse_session(path, "codex", [], 4, 1000)

        self.assertEqual([item["text"] for item in parsed["messages"]], ["Project update"])

    def test_session_roots_respect_documented_environment_overrides(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"CLAUDE_CONFIG_DIR": "/tmp/claude-config", "CODEX_HOME": "/tmp/codex-home"},
        ):
            roots = AGENT_SYNC.session_roots()

        self.assertEqual(roots["claude"], [Path("/tmp/claude-config/projects")])
        self.assertEqual(
            roots["codex"],
            [Path("/tmp/codex-home/sessions"), Path("/tmp/codex-home/archived_sessions")],
        )


if __name__ == "__main__":
    unittest.main()
