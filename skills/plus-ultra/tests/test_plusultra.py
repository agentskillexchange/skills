import importlib.util
import json
from pathlib import Path
import io
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plusultra.py"
SPEC = importlib.util.spec_from_file_location("plusultra", SCRIPT)
plusultra = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(plusultra)


def bash(command, session="session-1234"):
    return {
        "tool_name": "Bash",
        "tool_input": {"command": command},
        "session_id": session,
        "agent": "main",
    }


class CommandClassificationTests(unittest.TestCase):
    def test_read_only_git_status_is_allowed(self):
        self.assertIsNone(plusultra.mutating(bash("git status --short")))

    def test_chained_mutation_is_blocked(self):
        self.assertEqual(plusultra.mutating(bash("pwd && git push")), "Bash")

    def test_git_dash_c_mutation_is_blocked(self):
        self.assertEqual(plusultra.mutating(bash("git -C repo push origin main")), "Bash")

    def test_redirect_is_blocked(self):
        self.assertEqual(plusultra.mutating(bash('echo x > "out.txt"')), "Bash")

    def test_dev_null_redirect_is_allowed(self):
        self.assertIsNone(plusultra.mutating(bash("git status 2>/dev/null")))

    def test_quoted_arrow_is_data(self):
        self.assertIsNone(plusultra.mutating(bash("printf 'a > b'")))

    def test_heredoc_body_redirect_is_data(self):
        cmd = "python3 - <<'PY'\nprint('a > b')\nPY"
        self.assertIsNone(plusultra.mutating(bash(cmd)))


class SkillContractTests(unittest.TestCase):
    def test_agent_skill_frontmatter(self):
        text = (SCRIPT.parents[1] / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        block = text.split("---\n", 2)[1]
        values = dict(line.split(":", 1) for line in block.splitlines() if ":" in line)
        name = values["name"].strip()
        description = values["description"].strip()
        self.assertEqual(name, "plus-ultra")
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertLessEqual(len(description), 1024)
        self.assertTrue(description)


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = self.temp.name
        plusultra.ROOT = root
        plusultra.STATE = str(Path(root) / "state")
        plusultra.OFF_FLAG = str(Path(root) / "off")
        plusultra.AUDIT = str(Path(root) / "audit.jsonl")

    def tearDown(self):
        self.temp.cleanup()

    def test_unkeyed_mutation_is_denied(self):
        result = plusultra.hook_pre_tool(bash("git push", session=""))
        self.assertEqual(result["decision"], "block")
        self.assertIn("no session id", result["reason"])

    def test_plan_unlocks_only_its_session(self):
        plusultra.save("session-1234", {"plan": {"arbiter": "Athena"}, "mutations": 0})
        self.assertEqual(plusultra.hook_pre_tool(bash("git push")), {})
        self.assertEqual(plusultra.load("session-1234")["mutations"], 1)
        other = plusultra.hook_pre_tool(bash("git push", session="session-5678"))
        self.assertEqual(other["decision"], "block")

    def test_subagent_is_exempt_to_avoid_deadlock(self):
        payload = bash("git push")
        payload["agent"] = "proposer"
        self.assertEqual(plusultra.hook_pre_tool(payload), {})

    def test_audit_is_local_jsonl(self):
        plusultra.record("test", "event", answer=42)
        event = json.loads(Path(plusultra.AUDIT).read_text(encoding="utf-8"))
        self.assertEqual(event["details"]["answer"], 42)

    def test_empty_plan_verdict_is_rejected(self):
        with patch("sys.stdin", io.StringIO("   \n")):
            with self.assertRaisesRegex(SystemExit, "plan verdict must contain visible content"):
                plusultra.cmd_plan(["--session", "session-1234", "--verdict", "-"])

    def test_invisible_plan_verdict_is_rejected(self):
        for verdict in ("\u200b", "\u200d", "\u2060", "\ufe0f", "\u034f", "\u0301", "\x00"):
            with self.subTest(verdict=repr(verdict)):
                with self.assertRaisesRegex(SystemExit, "visible content"):
                    plusultra.cmd_plan(
                        ["--session", "session-1234", "--verdict", verdict]
                    )

    def test_reality_cannot_be_recorded_before_mutation(self):
        plusultra.save("session-1234", {"plan": {"entry": "approved"}, "mutations": 0})
        with self.assertRaisesRegex(SystemExit, "after this session mutates"):
            plusultra.cmd_confirm(
                ["--session", "session-1234", "--verdict", "looks good"]
            )

    def test_later_mutation_invalidates_reality_verdict(self):
        plusultra.save(
            "session-1234",
            {"plan": {"entry": "approved"}, "mutations": 1, "reality": None},
        )
        plusultra.cmd_confirm(
            ["--session", "session-1234", "--verdict", "checked mutation one"]
        )
        self.assertEqual(plusultra.hook_stop({"session_id": "session-1234"}), {})

        self.assertEqual(plusultra.hook_pre_tool(bash("git push")), {})
        blocked = plusultra.hook_stop({"session_id": "session-1234"})
        self.assertEqual(blocked["decision"], "block")

    def test_empty_reality_verdict_is_rejected(self):
        plusultra.save(
            "session-1234", {"plan": {"entry": "approved"}, "mutations": 1}
        )
        with patch("sys.stdin", io.StringIO("\n")):
            with self.assertRaisesRegex(SystemExit, "reality verdict must contain visible content"):
                plusultra.cmd_confirm(
                    ["--session", "session-1234", "--verdict", "-"]
                )

    def test_invisible_reality_verdict_is_rejected(self):
        plusultra.save(
            "session-1234", {"plan": {"entry": "approved"}, "mutations": 1}
        )
        for verdict in ("\u200b", "\u200d", "\u2060", "\ufe0f", "\u034f", "\u0301", "\x00"):
            with self.subTest(verdict=repr(verdict)):
                with self.assertRaisesRegex(SystemExit, "visible content"):
                    plusultra.cmd_confirm(
                        ["--session", "session-1234", "--verdict", verdict]
                    )


if __name__ == "__main__":
    unittest.main()
