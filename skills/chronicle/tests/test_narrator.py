"""The narrator's constraints, which are the difference between a record and a story.

The narrator forms hypotheses about intent from outside the work. These tests enforce
the boundary between an inference and a witnessed account.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src" / "chronicle"))
import capture as cap  # noqa: E402
import narrate  # noqa: E402


@pytest.fixture()
def home(tmp_path, monkeypatch):
    h = tmp_path / "chron-home"
    h.mkdir()
    monkeypatch.setattr(cap, "CHRON_HOME", str(h))
    monkeypatch.setenv("CHRONICLE_MACHINE", "testbox")
    return h


@pytest.fixture()
def repo(tmp_path):
    r = tmp_path / "proj"
    (r / ".git").mkdir(parents=True)
    (r / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    return r


def _events(repo, session="s"):
    lane = Path(cap.lane_path(str(repo), session))
    return [json.loads(l) for l in lane.read_text().splitlines() if l.strip()]


# ── the fence ────────────────────────────────────────────────────────────────

def test_every_narrator_entry_is_marked_inferred(home, repo):
    """An inferred claim that renders like a witnessed one is worse than no claim."""
    result = {
        "beats": [{"prose": "Something happened.", "anchors": ["01AAA"], "confidence": "low"}],
        "entries": [{"trigger": "DECISION", "title": "a call was made", "why": "reasons"},
                    {"trigger": "LANDED", "title": "a thing shipped"}],
    }
    window = {"events": [], "narrative": []}
    narrate.write_entries(result, "s", "proj", str(repo), window)
    events = _events(repo)
    assert events, "nothing was written"
    for e in events:
        assert e.get("inferred") is True, f"entry not marked inferred: {e.get('summary')}"


def test_disagreements_become_open_questions_never_corrections(home, repo):
    """The narrator has evidence; it does not have the authority of having been there.
    A CORRECTION asserts knowledge — that is not its to assert."""
    result = {"disagreements": [
        {"entry": "2026-08-06T02:24Z-AN3S",
         "question": "the trace suggests the migration ran twice — did it?"}]}
    narrate.write_entries(result, "s", "proj", str(repo), {"events": [], "narrative": []})
    events = _events(repo)
    assert events
    triggers = {e.get("trigger") for e in events}
    assert "CORRECTION" not in triggers, "the narrator filed a CORRECTION"
    assert "OPEN" in triggers
    assert all(e.get("inferred") for e in events)


def test_unknown_triggers_are_downgraded_to_note(home, repo):
    """The narrator must not be able to invent an ARM — which would imply a restore path
    that nobody ever verified."""
    result = {"entries": [{"trigger": "ARM", "title": "pretend arm"},
                          {"trigger": "WHATEVER", "title": "nonsense"}]}
    narrate.write_entries(result, "s", "proj", str(repo), {"events": [], "narrative": []})
    triggers = {e.get("trigger") for e in _events(repo)}
    assert "ARM" not in triggers, "the narrator was allowed to forge an ARM"
    assert triggers <= {"NOTE", "DECISION", "LANDED", "OPEN"}


# ── anchors must be real ─────────────────────────────────────────────────────

def test_hallucinated_anchors_are_dropped():
    """An anchor is a pointer to bytes. A fabricated one renders identically to a real one,
    which would turn the anti-fiction mechanism into theatre."""
    known = {"01REAL1", "01REAL2"}
    result = {
        "beats": [{"prose": "x", "anchors": ["01REAL1", "01FAKE9"]}],
        "entries": [{"trigger": "NOTE", "title": "y", "anchors": ["01FAKE8", "01REAL2"]}],
    }
    out = narrate.validate_anchors(result, known)
    assert out["beats"][0]["anchors"] == ["01REAL1"]
    assert out["entries"][0]["anchors"] == ["01REAL2"]
    assert out["_dropped_anchors"] == 2


def test_valid_anchors_are_all_kept():
    known = {"01A", "01B", "01C"}
    result = {"beats": [{"prose": "x", "anchors": ["01A", "01B", "01C"]}], "entries": []}
    out = narrate.validate_anchors(result, known)
    assert out["beats"][0]["anchors"] == ["01A", "01B", "01C"]
    assert out["_dropped_anchors"] == 0


# ── prompt construction ──────────────────────────────────────────────────────

def test_response_parsing_tolerates_fences_and_prose():
    """Models wrap JSON in explanations and code fences. Failing on that would make the
    narrator flaky for a cosmetic reason."""
    body = '{"beats": [{"prose": "hi", "anchors": []}]}'
    for text in (body,
                 f"Here you go:\n```json\n{body}\n```\nHope that helps.",
                 f"```\n{body}\n```",
                 f"Some preamble.\n{body}"):
        assert narrate.parse_response(text)["beats"][0]["prose"] == "hi"


def test_response_parsing_fails_loudly_on_garbage():
    with pytest.raises((ValueError, json.JSONDecodeError)):
        narrate.parse_response("I could not complete this request.")


def test_transcript_respects_its_byte_budget(home, tmp_path, monkeypatch):
    """The usable window is the model's context MINUS system prompt, tools and overhead —
    measured, not assumed: a 1.9 MB prompt reported ~1,063,000 tokens against a 1,000,000
    limit. And a transcript grows during a session, so the cap must be computed per call.
    """
    session = "budget-session"
    fake = tmp_path / "projects" / "p" / f"{session}.jsonl"
    fake.parent.mkdir(parents=True)
    fake.write_bytes(b"x" * 500_000)
    monkeypatch.setattr(narrate, "find_transcript", lambda s: fake)

    block = narrate._transcript_block(session, 100_000)
    assert len(block) < 130_000, "transcript ignored its budget"
    assert "truncated" in block
    # The gap must be declared, or the narrator reads a quiet middle as inactivity.
    assert "Do not treat the gap as inactivity" in block

    assert narrate._transcript_block(session, 0) == ""
    assert narrate._transcript_block(None, 100_000) == ""


def test_full_transcript_passes_through_when_it_fits(home, tmp_path, monkeypatch):
    session = "small"
    fake = tmp_path / f"{session}.jsonl"
    fake.write_text("a small transcript\n")
    monkeypatch.setattr(narrate, "find_transcript", lambda s: fake)
    block = narrate._transcript_block(session, 100_000)
    assert "a small transcript" in block
    assert "truncated" not in block


def test_butler_gate_is_consulted(monkeypatch):
    """A narrator that quietly drains the weekly budget is one that gets switched off."""
    calls = []

    class FakeProc:
        returncode = 1
        stdout = '{"verdict": "soft_stop"}'

    def fake_run(cmd, **kw):
        calls.append(cmd)
        return FakeProc()

    monkeypatch.setattr(narrate.subprocess, "run", fake_run)
    # Path.exists is read-only on the instance, so point BUTLER at a file that does exist.
    monkeypatch.setattr(narrate, "BUTLER", Path(__file__))
    ok, why = narrate.butler_gate("chronicle")
    assert ok is False
    assert "soft_stop" in why
    assert any("gate" in str(c) for c in calls)


def test_model_must_be_explicit_before_any_call(monkeypatch):
    monkeypatch.setattr(narrate, "MODEL", "")
    monkeypatch.setattr(narrate.subprocess, "run", lambda *a, **k: pytest.fail("model called"))
    with pytest.raises(RuntimeError, match="CHRONICLE_NARRATOR_MODEL"):
        narrate.call_model("test")


# ── the caveat must travel with the data ─────────────────────────────────────

def test_every_inferred_entry_carries_an_explicit_caveat(home, repo):
    """The warning lives IN the event, not in one UI's stylesheet.

    A narrated entry travels: read back by `chron resume`, printed into CHRONICLE.md,
    rendered in the canvas, grepped out of a lane by a script, and fed into the next
    agent's context. If the warning is only a CSS class, every one of those paths presents
    a model's after-the-fact reconstruction as though someone had witnessed it.
    """
    result = {
        "beats": [{"prose": "x", "anchors": []}],
        "entries": [{"trigger": "DECISION", "title": "a call"}],
        "experiments": [{"title": "tried a thing", "result": "it did not work"}],
        "disagreements": [{"entry": "E1", "question": "really?"}],
    }
    narrate.write_entries(result, "s", "proj", str(repo), {"events": [], "narrative": []})
    events = _events(repo)
    assert len(events) >= 4, "not every section produced an entry"
    for e in events:
        assert e.get("inferred") is True
        caveat = e.get("caveat") or ""
        assert "MAY BE WRONG" in caveat, f"no caveat on {e.get('summary')!r}"
        assert "NOT witnessed" in caveat or "NOT WITNESSED" in caveat
        assert "first-hand entry wins" in caveat, \
            "the caveat must state which source wins in a conflict"


def test_experiments_record_what_was_tried_and_why_it_was_abandoned(home, repo):
    """The dead ends are the part that is always lost, and the part that stops a future
    session repeating the work."""
    result = {"experiments": [{
        "title": "byte-level conv encoder at 50M params",
        "hypothesis": "convolution beats attention at this scale",
        "setup": "train.py --arch conv --params 50M --steps 4690",
        "varied": "swapped attention for depthwise conv vs the previous run",
        "result": "50.77% MTEB vs 53.04% for the hybrid",
        "conclusion": "conv alone underperforms the hybrid at equal parameters",
        "outcome": "abandoned",
        "why_abandoned": "hybrid dominated on every retrieval task; not worth more compute",
        "anchors": ["01A"], "confidence": "high"}]}
    narrate.write_entries(result, "s", "proj", str(repo), {"events": [], "narrative": []})
    exp = [e for e in _events(repo) if e.get("trigger") == "EXPERIMENT"]
    assert len(exp) == 1
    e = exp[0]
    for field in ("hypothesis", "setup", "varied", "result", "conclusion",
                  "outcome", "why_abandoned"):
        assert e.get(field), f"experiment lost its {field}"
    assert e["outcome"] == "abandoned"
    assert e["inferred"] is True and "MAY BE WRONG" in e["caveat"]


def test_narrator_cannot_forge_an_arm_or_a_close(home, repo):
    """An ARM implies a restore path somebody verified; a CLOSE asserts a session ended
    deliberately. Neither is the narrator's to claim."""
    result = {"entries": [{"trigger": "ARM", "title": "fake"},
                          {"trigger": "CLOSE", "title": "fake"},
                          {"trigger": "EXPERIMENT", "title": "legitimate"}]}
    narrate.write_entries(result, "s", "proj", str(repo), {"events": [], "narrative": []})
    triggers = {e.get("trigger") for e in _events(repo)}
    assert "ARM" not in triggers and "CLOSE" not in triggers
    assert "EXPERIMENT" in triggers


def test_prompt_demands_failures_and_experiments():
    """The instruction has to be in the prompt, or the narrator writes a changelog of what
    survived and silently drops everything that was tried."""
    # Matched against whitespace-collapsed text: the prompt is hard-wrapped for
    # readability, so a phrase that spans a line break is present but not findable as a
    # literal substring. Asserting on the wrapped form makes the test fail whenever
    # someone reflows a paragraph, which teaches people to delete the test.
    flat = " ".join(narrate.PROMPT.split())
    for phrase in ("RECORD WHAT WAS TRIED, NOT ONLY WHAT SURVIVED",
                   "abandoned", "EXPERIMENT REPOSITORY",
                   "never invent, round, or infer a number that is not there",
                   "say the result is unknown rather than guessing"):
        assert phrase in flat, f"prompt lost its instruction about {phrase!r}"
