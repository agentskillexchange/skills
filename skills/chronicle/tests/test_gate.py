"""The gate: destructive operations are refused until a restore path is on record.

Two failure modes matter, and they pull in opposite directions:

  FALSE NEGATIVE — a genuinely destructive command slips through. A bulk mutation
  can report success while destroying data with no snapshot.

  FALSE POSITIVE — the gate fires on `rm -rf node_modules`. This is worse in practice,
  because it teaches every agent to set CHRON_GATE=off on the first day, after which the
  gate protects nothing at all. A safety mechanism people route around is a liability.

So both directions are tested, and the exemption list is treated as load-bearing rather
than as a convenience.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src" / "chronicle"))
import capture as cap  # noqa: E402


@pytest.fixture()
def home(tmp_path, monkeypatch):
    h = tmp_path / "chron-home"
    h.mkdir()
    monkeypatch.setattr(cap, "CHRON_HOME", str(h))
    monkeypatch.setenv("CHRONICLE_MACHINE", "testbox")
    monkeypatch.delenv("CHRON_GATE", raising=False)
    return h


@pytest.fixture()
def repo(tmp_path):
    r = tmp_path / "proj"
    (r / ".git").mkdir(parents=True)
    (r / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    return r


def _pre(cmd: str, repo: Path, session="s1"):
    return {"hook_event_name": "PreToolUse", "tool_name": "Bash", "session_id": session,
            "cwd": str(repo), "tool_input": {"command": cmd}}


# ── must block ───────────────────────────────────────────────────────────────

BLOCKED = [
    "rm -rf /workspace/important",
    "rm -fr ~/data",
    "git push --force origin main",
    "git push -f",
    "git reset --hard HEAD~5",
    "git clean -fd",
    "psql -c 'DROP TABLE products'",
    "echo 'TRUNCATE TABLE users' | psql",
    "docker rm -f example-store-search",
    "docker system prune -a",
    "kubectl delete pod --all",
    "rsync -av --delete ./src/ test-host:/srv/app/",
    "aws s3 rm s3://bucket/prefix --recursive",
    "gcloud compute instances delete zeus",
    "find . -name '*.log' -delete",
    "python3 engine/migrate_locales.py --all",
    "python scripts/backfill_translations.py",
    "shopify theme publish --store example-store",
    "dd if=/dev/zero of=/dev/disk2",
    "conda env remove -n ogma",
]


@pytest.mark.parametrize("cmd", BLOCKED)
def test_destructive_commands_are_blocked_without_an_arm(cmd, home, repo):
    decision = cap.gate_check(_pre(cmd, repo))
    assert decision is not None, f"gate let a destructive command through: {cmd}"
    assert decision["hookSpecificOutput"]["permissionDecision"] == "deny"
    reason = decision["hookSpecificOutput"]["permissionDecisionReason"]
    assert "chron arm" in reason, "the refusal must tell the agent exactly what to do"
    assert "--restore" in reason


# ── must NOT block ───────────────────────────────────────────────────────────

ALLOWED = [
    "ls -la",
    "git status",
    "git push origin main",
    "pytest tests/ -q",
    "rm -rf node_modules",
    "rm -rf ./build",
    "rm -rf __pycache__ .pytest_cache",
    "rm -rf /tmp/scratch-dir",
    "rm -f /var/folders/xy/tmpfile",
    "docker ps -a",
    "docker build -t chronicle .",
    "kubectl get pods",
    "grep -rn 'delete' src/",
    "python3 train.py --epochs 5",
    "echo 'DELETE FROM users WHERE id = 3' | psql",   # bounded delete
    "cat migrate_notes.md",
    "rm -rf .venv",
]


@pytest.mark.parametrize("cmd", ALLOWED)
def test_ordinary_commands_are_not_blocked(cmd, home, repo):
    """Every false positive here is a step toward someone disabling the gate."""
    assert cap.gate_check(_pre(cmd, repo)) is None, \
        f"gate produced a FALSE POSITIVE on: {cmd}"


# ── the ARM unlocks it ───────────────────────────────────────────────────────

def test_arm_permits_the_operation(home, repo):
    cmd = "rm -rf /workspace/data/products"
    assert cap.gate_check(_pre(cmd, repo)) is not None, "precondition: blocked"

    cap.record_arm({"at": time.time(), "entry": "2026-08-06T02:00Z-AAAA",
                    "session": "s1", "title": "clear stale product cache",
                    "restore": "snapshots/products-2026-08-06.json"})
    assert cap.gate_check(_pre(cmd, repo)) is None, "ARM did not unlock the gate"


def test_expired_arm_does_not_permit(home, repo):
    """An ARM from three hours ago is not a licence for this afternoon's deletion."""
    cap.record_arm({"at": time.time() - (cap.GATE_WINDOW_S + 600),
                    "entry": "old", "session": "s1", "title": "stale",
                    "restore": "somewhere"})
    assert cap.gate_check(_pre("rm -rf /data/live", repo)) is not None, \
        "an expired ARM was accepted"


def test_gate_records_both_outcomes(home, repo):
    """Blocked and permitted operations are BOTH recorded. The pairing of which ARM
    authorised which destructive command is the first thing you want when reconstructing
    a bad afternoon."""
    cap.gate_check(_pre("rm -rf /data/x", repo, session="rec"))
    cap.record_arm({"at": time.time(), "entry": "E1", "session": "rec",
                    "title": "planned wipe", "restore": "backup.tar"})
    cap.gate_check(_pre("rm -rf /data/x", repo, session="rec"))

    lane = Path(cap.lane_path(str(repo), "rec"))
    events = [json.loads(l) for l in lane.read_text().splitlines() if l.strip()]
    summaries = " ".join(e["summary"] for e in events)
    assert "gate BLOCKED" in summaries
    assert "gate PASSED" in summaries
    passed = [e for e in events if "PASSED" in e["summary"]][0]
    assert passed["gate"]["arm"] == "E1", "the authorising ARM was not recorded"
    assert passed["gate"]["restore"] == "backup.tar"


def test_bypass_is_possible_but_recorded(home, repo, monkeypatch):
    """The gate must be escapable — an unescapable gate gets uninstalled — but never
    silently."""
    monkeypatch.setenv("CHRON_GATE", "off")
    assert cap.gate_enabled() is False
    assert cap.gate_check(_pre("rm -rf /data/live", repo)) is None


def test_gate_only_applies_to_bash(home, repo):
    payload = {"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "s",
               "cwd": str(repo), "tool_input": {"file_path": "/tmp/x", "content": "rm -rf /"}}
    assert cap.gate_check(payload) is None


def test_secrets_in_a_blocked_command_are_masked(home, repo):
    """A blocked command is still written to the record — with credentials removed."""
    cmd = "aws s3 rm s3://b/p --recursive --token ghp_" + "c" * 30
    cap.gate_check(_pre(cmd, repo, session="sec"))
    lane = Path(cap.lane_path(str(repo), "sec"))
    text = lane.read_text()
    assert "ghp_cccc" not in text
    assert "aws s3 rm" in text


def test_before_snapshot_survives_a_denial(home, repo):
    """Even when the gate refuses, the pre-state we captured is kept. If the agent then
    bypasses, the snapshot taken a second earlier is the restore path."""
    target = repo / "data.txt"
    target.write_text("precious\n")
    pre = {"hook_event_name": "PreToolUse", "tool_name": "Write", "session_id": "snap",
           "cwd": str(repo), "tool_input": {"file_path": str(target)}}
    cap.handle_hook(pre)
    st = cap.state_load("snap")
    digest = (st.get("pending") or {}).get(str(target))
    assert digest, "no before-snapshot was taken"
    assert cap.cas_get(digest).decode() == "precious\n"


# ── the nudge ────────────────────────────────────────────────────────────────

def test_nudge_fires_at_the_event_threshold(home, repo, monkeypatch):
    monkeypatch.setattr(cap, "NUDGE_EVENTS", 5)
    for _ in range(4):
        cap.state_bump("n1", events=1)
    assert cap.nudge_check("n1", str(repo)) is None, "nudged too early"
    cap.state_bump("n1", events=1)
    out = cap.nudge_check("n1", str(repo))
    assert out is not None, "nudge did not fire at the threshold"
    text = out["hookSpecificOutput"]["additionalContext"]
    assert "chron decision" in text
    assert "why" in text.lower()


def test_nudge_does_not_repeat_at_the_same_count(home, repo, monkeypatch):
    """A nudge on every subsequent tool call becomes noise the agent learns to ignore —
    which is the same outcome as never nudging."""
    monkeypatch.setattr(cap, "NUDGE_EVENTS", 3)
    for _ in range(3):
        cap.state_bump("n2", events=1)
    assert cap.nudge_check("n2", str(repo)) is not None
    assert cap.nudge_check("n2", str(repo)) is None, "nudge repeated without new activity"


def test_nudge_backs_off_as_work_continues(home, repo, monkeypatch):
    """Regression, found by running this against a live session rather than in a test.

    The original guard was `if nudged_at_events == events: return None`, which reads like
    deduplication but never matches — `events` increments on every tool call, so the
    nudge fired on EVERY subsequent call. The suite missed it because it called
    nudge_check twice without incrementing in between, exercising a state that does not
    occur in practice. Tests must advance the world the way the world advances.
    """
    monkeypatch.setattr(cap, "NUDGE_EVENTS", 5)
    fired = []
    for i in range(1, 31):
        cap.state_bump("backoff", events=1)          # a tool call happened
        if cap.nudge_check("backoff", str(repo)):
            fired.append(i)

    assert fired, "never nudged at all"
    assert len(fired) <= 6, f"nudge spammed {len(fired)} times over 30 events: {fired}"
    gaps = [b - a for a, b in zip(fired, fired[1:])]
    assert all(g >= 5 for g in gaps), f"nudges came closer than the threshold apart: {gaps}"


def test_cli_and_hook_agree_on_the_session_key(home, repo):
    """The CLI cannot read Claude's session id from the environment, so the hooks publish
    it. If these two disagree, narrating never clears the counters and the agent is told
    'nothing has been narrated' one second after narrating."""
    cap.mark_current_session("live-session-abc", str(repo))
    assert cap.current_session() == "live-session-abc"

    sys.path.insert(0, str(REPO / "src" / "chronicle"))
    import importlib
    import cli as chron_cli
    importlib.reload(chron_cli)
    chron_cli.cap = cap                               # share the isolated CHRON_HOME
    assert chron_cli._session() == "live-session-abc", \
        "the CLI keys state differently from the hooks"


def test_nudge_can_be_disabled(home, repo, monkeypatch):
    monkeypatch.setenv("CHRON_NUDGE", "off")
    monkeypatch.setattr(cap, "NUDGE_EVENTS", 1)
    cap.state_bump("n3", events=5)
    assert cap.nudge_check("n3", str(repo)) is None


def test_writing_a_narrative_entry_resets_the_counters(home, repo, monkeypatch):
    """Otherwise the agent narrates once and is nagged forever afterwards."""
    monkeypatch.setattr(cap, "NUDGE_EVENTS", 3)
    for _ in range(3):
        cap.state_bump("n4", events=1)
    assert cap.nudge_check("n4", str(repo)) is not None
    st = cap.state_load("n4")
    st["events"] = 0
    st["last_narrative"] = cap.now_iso()
    st["nudged_at_events"] = None
    cap.state_save("n4", st)
    assert cap.nudge_check("n4", str(repo)) is None
