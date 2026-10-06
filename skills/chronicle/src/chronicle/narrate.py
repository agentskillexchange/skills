"""An optional narrator that drafts hypotheses anchored to captured evidence.

Inferred entries remain labelled and cannot replace firsthand entries or authorize
an operation. Narration uses an explicitly configured model through the Claude CLI.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import capture as cap  # noqa: E402
import index as idx  # noqa: E402

MODEL = os.environ.get("CHRONICLE_NARRATOR_MODEL", "")
BUTLER = Path.home() / ".claude" / "skills" / "butler" / "scripts" / "butler.py"
MAX_EVENTS = int(os.environ.get("CHRONICLE_NARRATOR_MAX_EVENTS", "1200"))

# This bounds input size, not token cost; choose a budget suitable for your model.
PROMPT_BUDGET_BYTES = int(os.environ.get("CHRONICLE_NARRATOR_BUDGET", str(900_000)))

SCHEMA_HINT = """
Return ONLY a JSON object, no prose around it, of this shape:

{
  "beats": [
    {
      "prose": "One to three sentences of narrative, in past tense, plain and specific.",
      "anchors": ["<event id>", "<event id>"],
      "confidence": "high" | "medium" | "low"
    }
  ],
  "entries": [
    {
      "trigger": "DECISION" | "LANDED" | "NOTE" | "OPEN" | "EXPERIMENT" | "ABANDONED",
      "title": "<short imperative-free summary>",
      "why": "<the reason, if the evidence supports one>",
      "state": "<only if a state is genuinely ambiguous: say which reading the evidence supports and how confident that is>",
      "not_done": "<work visibly started and not finished>",
      "open": ["<a question a future session must answer>"],
      "anchors": ["<event id>"]
    }
  ],
  "experiments": [
    {
      "title": "<what was tried>",
      "hypothesis": "<what it was expected to show or achieve, if the trace supports one>",
      "setup": "<what was actually run: command, config, variant, data, scale>",
      "varied": "<what changed relative to the previous attempt>",
      "result": "<what actually happened — numbers, errors, exit codes, measured values>",
      "conclusion": "<what was learned>",
      "outcome": "kept" | "abandoned" | "inconclusive" | "superseded",
      "why_abandoned": "<if abandoned or superseded: the reason, so nobody retries it blindly>",
      "anchors": ["<event id>"],
      "confidence": "high" | "medium" | "low"
    }
  ],
  "disagreements": [
    {
      "entry": "<the first-hand entry id you disagree with>",
      "question": "<phrased as an OPEN question, never as a correction>"
    }
  ]
}
"""

PROMPT = """You are the narrator of a work ledger. You did not do this work. You are
reading its complete machine-captured trace after the fact.

Your job is to write the STORY of what happened — what was attempted, what was decided,
what landed, what broke, what was left unfinished — anchored to the evidence.

Hard rules:

- Never state intent as fact when you
  are inferring it. Say "the trace is consistent with X" or mark confidence "low". If a
  state could be read two ways, that ambiguity IS the finding — record it as an OPEN
  question rather than resolving it.
- Never contradict a first-hand entry. If the trace suggests a first-hand entry is wrong,
  put it in "disagreements" as a question, not as a correction.
- Every beat and entry must cite the event ids that support it in "anchors". A claim you
  cannot anchor is a claim you should not make.
- Be specific and concrete. "Refactored the module" is worthless; "moved the gate matcher
  out of the PostToolUse path after it added 30ms to every tool call" is the record.
- Do not pad. If little happened, write little.

RECORD WHAT WAS TRIED, NOT ONLY WHAT SURVIVED.

The failures, dead ends, and abandoned approaches are the most valuable part of the record
and the part that is always lost. A future session that cannot see what was already tried
will retry it. So:

- Every attempt that did not work gets an entry, with WHY it did not work.
- An approach that was considered and rejected gets an entry, with the reason, so nobody
  re-litigates a settled question or re-runs a settled failure.
- If something was tried three times with variations, that is three experiments and the
  variations are the point — say what changed each time.
- "abandoned" is a first-class outcome, not an absence. Say what would have to be true for
  it to be worth trying again.

IF THIS IS AN EXPERIMENT REPOSITORY, THAT IS THE MAIN STORY.

Training runs, evaluations, sweeps, ablations, benchmark measurements, parameter searches:
each is an experiment. Fill in "experiments" with what was run, what it was expected to
show, what changed relative to the last attempt, what the numbers actually were, and what
was concluded. Quote real measured values from the trace — never invent, round, or infer a
number that is not there. If a run produced no result you can see, say the result is
unknown rather than guessing at it; an invented metric is far worse than a missing one.
Record the configuration precisely enough that the run could be repeated.

%(schema)s

--- FIRST-HAND ENTRIES (written by whoever did the work; treat as ground truth) ---
%(narrative)s

--- EVENT TRACE (%(n_events)d events) ---
%(events)s

%(transcript)s
"""


# ── evidence gathering ───────────────────────────────────────────────────────

def _compact(ev: idx.Event) -> str:
    """One line per event. Compact because the point of the 1M window is to fit MORE
    events, not more formatting."""
    raw = ev.raw
    bits = [ev.id, ev.ts[11:19], ev.kind]
    actor = raw.get("actor") or {}
    if actor.get("kind") == "human":
        bits.append("HUMAN")
    if ev.machine and ev.machine != cap.machine():
        bits.append("@" + ev.machine)
    summary = (ev.summary or "").replace("\n", " ⏎ ")[:220]
    bits.append(summary)
    for f in raw.get("files") or []:
        flag = " REDACTED" if f.get("redacted") else ""
        bits.append("file=%s%s" % (f.get("path", "?").split("/")[-1], flag))
    cmd = raw.get("cmd") or {}
    if "exit" in cmd:
        bits.append("exit=%s" % cmd["exit"])
    if raw.get("gate"):
        bits.append("GATE=%s" % ("blocked" if raw["gate"].get("blocked") else "passed"))
    for key in ("output_head", "text"):
        if raw.get(key):
            bits.append("%s=%s" % (key, str(raw[key]).replace("\n", " ⏎ ")[:400]))
    return " | ".join(str(b) for b in bits)


def gather(conn, session: str | None, since: str | None, project: str | None) -> dict:
    sql = "SELECT * FROM events WHERE kind<>'narrative'"
    args: list = []
    if session:
        sql += " AND session=?"
        args.append(session)
    if since:
        sql += " AND ts>=?"
        args.append(since)
    if project:
        sql += " AND project=?"
        args.append(project)
    sql += " ORDER BY ts ASC LIMIT ?"
    args.append(MAX_EVENTS)
    events = [idx._ev(r) for r in conn.execute(sql, args)]

    narrative = idx.narrative(conn, project, limit=60,
                             since=since or (events[0].ts if events else None))
    return {"events": events, "narrative": narrative}


def find_transcript(session: str) -> Path | None:
    """Claude Code keeps per-session transcripts under ~/.claude/projects/**.

    Reading the transcript is what separates this narrator from one guessing at intent
    from tool calls alone: the transcript contains the reasoning that produced them.
    """
    base = Path.home() / ".claude" / "projects"
    if not base.exists() or not session:
        return None
    for candidate in base.rglob(f"{session}.jsonl"):
        return candidate
    return None


def _transcript_block(session: str | None, budget: int) -> str:
    """The transcript gets whatever budget the events did not use.

    Deliberately in this order: the event trace is the ground truth and must never be
    truncated to make room for the transcript, which is context. A transcript also GROWS
    as the session runs, so a fixed cap that fits at 09:00 overflows by mid-afternoon —
    the budget has to be computed per call.
    """
    if not session or budget <= 0:
        return ""
    path = find_transcript(session)
    if not path:
        return ""
    try:
        data = path.read_bytes()
    except OSError:
        return ""
    note = ""
    if len(data) > budget:
        # Head and tail: the beginning holds the intent, the end holds what actually
        # happened, and the middle is where the repetition lives.
        half = budget // 2
        dropped = len(data) - budget
        data = data[:half] + b"\n...[transcript truncated]...\n" + data[-half:]
        note = (f"\n[NOTE: {dropped:,} bytes of the middle of this transcript were "
                f"omitted to fit the context budget. Do not treat the gap as inactivity; "
                f"the EVENT TRACE above is complete and authoritative.]\n")
    text = cap.redact_text(data.decode("utf-8", "replace"))
    return ("--- SESSION TRANSCRIPT (the reasoning behind the trace) ---" + note
            + "\n" + text)


# ── budget ───────────────────────────────────────────────────────────────────

def butler_gate(project: str = "chronicle") -> tuple[bool, str]:
    """Ask the butler before spending. A narrator that quietly drains the weekly budget
    is a narrator that gets uninstalled."""
    if not BUTLER.exists():
        return True, "butler not installed; proceeding"
    try:
        proc = subprocess.run([sys.executable, str(BUTLER), "gate", "--project", project],
                              capture_output=True, text=True, timeout=60)
    except subprocess.SubprocessError as exc:
        return True, f"butler unavailable ({exc}); proceeding"
    if proc.returncode == 0:
        try:
            payload = json.loads(proc.stdout)
            return True, f"budget ok ({payload.get('pct_of_budget', 0):.1f}% of weekly)"
        except Exception:
            return True, "budget ok"
    verdict = "soft_stop" if proc.returncode == 1 else "hard_stop"
    return False, f"butler says {verdict}: {proc.stdout.strip()[:200]}"


# ── the call ─────────────────────────────────────────────────────────────────

def call_model(prompt: str, timeout: int = 1800) -> str:
    """Invoke Claude headlessly, feeding the prompt on STDIN.

    Not as an argv argument: the whole point of the 1M window is that this prompt is
    megabytes, and ARG_MAX on macOS is about 1 MB. Passing it positionally fails with
    `[Errno 7] Argument list too long` — and it fails at exactly the sizes the feature
    exists to handle, so a small-input test would never catch it.
    """
    if not MODEL:
        raise RuntimeError("Set CHRONICLE_NARRATOR_MODEL explicitly before narration")
    claude = os.environ.get("CHRONICLE_CLAUDE_BIN") or "claude"
    last = ""
    # Retry once: an observed failure returned rc=1 with an EMPTY stderr and succeeded on
    # an identical re-run. Narration is a background convenience, so a transient blip
    # should cost a few seconds, not a session's story.
    for attempt in (1, 2):
        proc = subprocess.run(
            [claude, "-p", "--model", MODEL],
            input=prompt, capture_output=True, text=True, timeout=timeout)
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout
        # The CLI reports some failures on stdout, so an error that only reads stderr
        # produces the useless message "failed (1): " with nothing after the colon.
        last = (proc.stderr or "").strip() or (proc.stdout or "").strip() or "(no output)"
        if attempt == 1:
            cap._log_error(f"narrator attempt 1 failed (rc={proc.returncode}): {last[:200]}")
    raise RuntimeError(f"narrator model call failed after 2 attempts "
                       f"(rc={proc.returncode}): {last[:500]}")


def parse_response(text: str) -> dict:
    """Extract the JSON object, tolerating fenced code blocks and surrounding prose."""
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    blob = fence.group(1) if fence else None
    if blob is None:
        start = text.find("{")
        end = text.rfind("}")
        blob = text[start:end + 1] if start >= 0 and end > start else ""
    if not blob:
        raise ValueError("no JSON object in the narrator's response")
    return json.loads(blob)


# ── writing back ─────────────────────────────────────────────────────────────

# Carried IN the event, not merely rendered by one UI. A narrated entry travels: it is
# read back by `chron resume`, printed into CHRONICLE.md, shown in the canvas, grepped out
# of a lane by a script, and fed to the next agent's context. If the warning lives only in
# a stylesheet then every one of those paths presents a model's after-the-fact
# reconstruction as though someone had witnessed it.
CAVEAT = (
    "⚠ INFERRED — reconstructed after the fact by a model reading the trace. "
    "NOT witnessed. MAY BE WRONG. Do not treat as fact or act on it without checking the "
    "anchored events; where this conflicts with a first-hand entry, the first-hand entry "
    "wins."
)


def validate_anchors(result: dict, known: set) -> dict:
    """Drop any anchor that does not name a real event, and count what was dropped.

    The evidence gutter's entire value rests on an anchor being a pointer to bytes rather
    than a decoration. A hallucinated id renders identically to a real one in the UI, so a
    single fabricated anchor would quietly convert the anti-fiction mechanism into
    theatre. Measured at 210/210 valid on the first real run — which is a reason to keep
    it that way, not a reason to stop checking.
    """
    dropped = 0

    def clean(anchors):
        nonlocal dropped
        out = []
        for a in anchors or []:
            if a in known:
                out.append(a)
            else:
                dropped += 1
        return out

    for beat in result.get("beats") or []:
        beat["anchors"] = clean(beat.get("anchors"))
    for entry in result.get("entries") or []:
        entry["anchors"] = clean(entry.get("anchors"))
    result["_dropped_anchors"] = dropped
    return result


def write_entries(result: dict, session: str, project: str, cwd: str,
                  window: dict) -> list[str]:
    """Append the narrator's output. `inferred: true` on everything, no exceptions."""
    written = []

    beats = result.get("beats") or []
    if beats:
        eid = cap.emit({
            "kind": "narrative", "trigger": "NARRATION", "inferred": True,
            "caveat": CAVEAT,
            "entry": _entry_id(),
            "summary": "narrated %d event(s) from session %s" % (
                len(window["events"]), session[:12]),
            "beats": beats,
            "model": MODEL,
            "actor": {"kind": "agent", "harness": "narrator", "session": session,
                      "model": MODEL},
            "covers": {"from": window["events"][0].ts if window["events"] else None,
                       "to": window["events"][-1].ts if window["events"] else None,
                       "events": len(window["events"])},
        }, cwd, session)
        written.append(eid)

    for entry in result.get("entries") or []:
        trigger = (entry.get("trigger") or "NOTE").upper()
        # ARM and CLOSE are never the narrator's to write: an ARM implies a restore path
        # somebody verified, and a CLOSE asserts a session ended deliberately.
        if trigger not in ("DECISION", "LANDED", "NOTE", "OPEN", "EXPERIMENT", "ABANDONED"):
            trigger = "NOTE"
        ev = {
            "kind": "narrative", "trigger": trigger, "inferred": True,
            "caveat": CAVEAT,
            "entry": _entry_id(),
            "summary": entry.get("title") or "(untitled)",
            "why": entry.get("why"),
            "state": entry.get("state"),
            "not_done": entry.get("not_done"),
            "open": entry.get("open") or [],
            "anchors": entry.get("anchors") or [],
            "model": MODEL,
            "actor": {"kind": "agent", "harness": "narrator", "session": session,
                      "model": MODEL},
        }
        written.append(cap.emit({k: v for k, v in ev.items() if v not in (None, [], "")},
                                cwd, session))

    # Experiments are the main story in a research repo, and the part that is always lost:
    # what was tried, what changed each time, what the numbers were, and what was given up
    # on. A future session that cannot see the dead ends will walk down them again.
    for exp in result.get("experiments") or []:
        ev = {
            "kind": "narrative", "trigger": "EXPERIMENT", "inferred": True,
            "caveat": CAVEAT,
            "entry": _entry_id(),
            "summary": exp.get("title") or "(untitled experiment)",
            "hypothesis": exp.get("hypothesis"),
            "setup": exp.get("setup"),
            "varied": exp.get("varied"),
            "result": exp.get("result"),
            "conclusion": exp.get("conclusion"),
            "outcome": exp.get("outcome"),
            "why_abandoned": exp.get("why_abandoned"),
            "confidence": exp.get("confidence"),
            "anchors": exp.get("anchors") or [],
            "model": MODEL,
            "actor": {"kind": "agent", "harness": "narrator", "session": session,
                      "model": MODEL},
        }
        written.append(cap.emit({k: v for k, v in ev.items() if v not in (None, [], "")},
                                cwd, session))

    # Disagreements become OPEN questions, never corrections. The narrator has evidence;
    # it does not have the authority of having been there.
    for dis in result.get("disagreements") or []:
        written.append(cap.emit({
            "kind": "narrative", "trigger": "OPEN", "inferred": True,
            "caveat": CAVEAT,
            "entry": _entry_id(),
            "summary": "narrator questions entry %s" % dis.get("entry", "?"),
            "open": [dis.get("question") or ""],
            "questions_entry": dis.get("entry"),
            "model": MODEL,
            "actor": {"kind": "agent", "harness": "narrator", "session": session,
                      "model": MODEL},
        }, cwd, session))
    return written


def _entry_id() -> str:
    import datetime as dt
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ") + \
        "-" + cap.ulid()[-4:]


# ── command ──────────────────────────────────────────────────────────────────

def cmd_narrate(args) -> int:
    conn = idx.connect()
    idx.refresh(conn)

    session = getattr(args, "session", None)
    if not session:
        row = conn.execute(
            "SELECT session FROM events WHERE session<>'' AND session<>'cli' "
            "ORDER BY ts DESC LIMIT 1").fetchone()
        session = row["session"] if row else None
    if not session:
        print("no session to narrate")
        return 1

    project = cap.project_name(os.getcwd())
    window = gather(conn, session, getattr(args, "since", None), None)
    if not window["events"]:
        print(f"nothing to narrate for session {session[:12]}")
        return 1

    print(f"narrating {len(window['events'])} events from session {session[:12]}")
    print(f"  model: {MODEL}")

    events_block = "\n".join(_compact(e) for e in window["events"])
    narrative_block = "\n".join(
        f"[{e.raw.get('entry', e.id)}] {e.trigger}: {e.summary}"
        + (f"\n    intent: {e.raw['intent']}" if e.raw.get("intent") else "")
        + (f"\n    state: {e.raw['state']}" if e.raw.get("state") else "")
        for e in reversed(window["narrative"])) or "(none — nobody said why)"

    fixed = len(PROMPT) + len(SCHEMA_HINT) + len(events_block) + len(narrative_block)
    transcript = _transcript_block(session, PROMPT_BUDGET_BYTES - fixed)
    print(f"  events: {len(events_block) // 1024} KB · "
          f"transcript: {(len(transcript) // 1024) if transcript else 0} KB "
          f"(budget {(PROMPT_BUDGET_BYTES - fixed) // 1024} KB)")

    prompt = PROMPT % {
        "schema": SCHEMA_HINT,
        "narrative": narrative_block,
        "n_events": len(window["events"]),
        "events": events_block,
        "transcript": transcript,
    }

    print(f"  prompt: {len(prompt) // 1024} KB")
    if getattr(args, "dry_run", False):
        out = Path(cap.CHRON_HOME) / "narrator-prompt.txt"
        out.write_text(prompt)
        print(f"  dry run — prompt written to {out}")
        return 0

    ok, why = butler_gate()
    print(f"  butler: {why}")
    if not ok:
        return 2

    try:
        raw = call_model(prompt)
        result = parse_response(raw)
    except Exception as exc:
        print(f"  narration FAILED: {exc}")
        cap._log_error(f"narrator: {exc}")
        return 1

    result = validate_anchors(result, {e.id for e in window["events"]})
    dropped = result.get("_dropped_anchors", 0)
    if dropped:
        print(f"  ⚠ dropped {dropped} anchor(s) that named no real event")

    written = write_entries(result, session, project, os.getcwd(), window)
    print(f"  wrote {len(written)} inferred entr(ies)")
    for beat in (result.get("beats") or [])[:6]:
        anchors = ", ".join(a[-6:] for a in (beat.get("anchors") or [])[:3])
        print(f"    · {beat.get('prose', '')[:110]}  [{anchors}]")
    if result.get("disagreements"):
        print(f"  {len(result['disagreements'])} disagreement(s) filed as OPEN questions")
    return 0
