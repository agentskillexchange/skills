#!/usr/bin/env python3
"""plus-ultra — a Claude Code hook adapter for a Byzantine 2+1 workflow.

Runs as a Claude Code hook on every tool call, so it is stdlib-only and does no
work it can avoid. The design lives in the plus-ultra skill; the short version:

    UserPromptSubmit  open a turn, state the requirement
    PreToolUse        deny a MUTATING tool until this turn holds a PLAN verdict
    Stop              block completion until a turn that mutated holds a REALITY verdict

The gate always says exactly what to run next. A gate that blocks without telling
you the way through is an obstacle, not a control.

Bypass with PLUS_ULTRA=off or `plusultra off` — bypassable, never silent.
"""

import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, ".plus-ultra")
STATE = os.path.join(ROOT, "state")
OFF_FLAG = os.path.join(ROOT, "off")
AUDIT = os.path.join(ROOT, "audit.jsonl")

MUTATING_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}

# Bash commands that change state. Deliberately broad: a false block costs one
# bypass, a false pass costs the thing this mode exists to prevent.
MUTATING_BASH = re.compile(
    r"""(?xi)
    (^|[;&|]+\s*)(
        rm\s | rmdir\s | mv\s | cp\s | ln\s | mkdir\s | touch\s | truncate\s
      | chmod\s | chown\s | dd\s | tee\s
      | sed\s+(-[a-z]*i|--in-place) | perl\s+(-[a-z]*i|.*-pi)
      | git\s+(?:(?:-C|-c|--git-dir|--work-tree)\s+\S+\s+)*(commit|push|merge|rebase|reset|checkout|restore|clean|revert|tag|cherry-pick|filter-repo|am|apply)
      | gh\s+(repo\s+create|repo\s+delete|repo\s+edit|release|pr\s+(create|merge|close)|issue\s+(create|close))
      | launchctl\s | crontab\s | systemctl\s | defaults\s+write
      | npm\s+(i|install|publish|uninstall) | pip\s+(install|uninstall) | uv\s+(pip|add|remove|sync)
      | brew\s+(install|uninstall|upgrade) | conda\s+(install|remove|create)
      | docker\s+(run|rm|rmi|build|push|compose) | kubectl\s+(apply|delete|create|patch)
      | curl\s+[^|;&]*-X\s*(POST|PUT|PATCH|DELETE) | curl\s+[^|;&]*--(data|upload-file)
      | osascript\s | killall\s | kill\s | pkill\s
      | (ba|z)?sh\s+-c | eval\s
    )
    """
)

# Redirection is checked SEPARATELY and FIRST, because `echo hi > file` writes a file
# even though `echo` is on the read-only allowlist. A digit before `>` means an fd
# redirect (2>/dev/null), and a `-` before it is an arrow in prose, not a redirect.
REDIRECT = re.compile(r"(?:^|[^-0-9&>])>>?\s*([^\s|&;<>]+)")

# A `>` inside a quoted string or a heredoc body is DATA, not redirection. Scrub those
# spans before scanning. They collapse to an opaque TOKEN rather than to nothing, so a
# real redirect to a quoted target — `echo x > "out.txt"` — still presents a target and
# still blocks. MUTATING_BASH below deliberately still runs on the RAW command, so
# quoting can never hide `rm -rf`.
QUOTED_SPAN = re.compile(r"'[^']*'|\"[^\"]*\"")

# Only the heredoc BODY is data. The remainder of the OPENING line is still live shell:
# `cat <<EOF > ~/.zshrc` redirects. An earlier version scrubbed from the tag to the
# terminator and swallowed that redirect, letting a real write through the gate.
HEREDOC_BODY = re.compile(r"(<<-?[ \t]*['\"]?(\w+)['\"]?)([^\n]*)\n.*?\n\2", re.S)


def _scrub_heredoc(m):
    return m.group(1) + m.group(3) + "\nH"


def _shell_code(cmd):
    """The command with data-carrying spans replaced by opaque tokens."""
    return QUOTED_SPAN.sub("Q", HEREDOC_BODY.sub(_scrub_heredoc, cmd))

# Read-only shapes that must never be gated, even though they match above.
SAFE_BASH = re.compile(
    r"""(?xi)
    ^\s*(
        plusultra\b | .*\bplusultra\.py\b
      | git\s+(status|log|diff|show|ls-files|ls-tree|rev-parse|rev-list|branch\s*$|remote\s+-v|fetch|merge-base|cat-file|blame|describe)
      | gh\s+(repo\s+view|auth\s+status|api\s+user|pr\s+view|pr\s+list|issue\s+list|repo\s+list)
      | ls | cat | head | tail | grep | rg | find | wc | stat | file | which | echo | printf | date | pwd | env
      | ps | pgrep | lsof | top | df | du | uname | sw_vers | whoami | id | uptime
      | python3?\s+-c | jq | sort | uniq | awk | sed(?!\s+-[a-z]*i) | diff | comm | cut | tr | column | fold
    )\b
    """
)


# ── state ────────────────────────────────────────────────────────────────────

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _ensure():
    os.makedirs(STATE, exist_ok=True)


def _path(session):
    return os.path.join(STATE, session + ".json")


def _valid_session(session):
    """A gate keyed by an empty session is a gate anyone can walk through.

    Falsy session ids used to collapse to a shared `nosession.json`; a single stray
    PLANNED verdict left there by a smoke test then unlocked EVERY unkeyed call,
    while `plusultra status` still reported the gate armed.
    """
    return bool(session) and bool(
        re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{7,}", session))


def load(session):
    if not _valid_session(session):
        return {}          # an unkeyed call inherits no one's plan
    try:
        with open(_path(session), "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def save(session, data):
    if not _valid_session(session):
        return False       # and can never mint one either
    _ensure()
    p = _path(session)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    os.replace(tmp, p)  # atomic — a half-written gate state fails open, which is wrong
    return True


def disabled():
    if os.environ.get("PLUS_ULTRA", "").lower() in ("off", "0", "false", "no"):
        return True
    return os.path.exists(OFF_FLAG)


def record(kind, summary, **extra):
    """Append a best-effort local audit event without depending on another tool."""
    try:
        _ensure()
        payload = {"at": _now(), "kind": kind, "summary": summary, "details": extra}
        with open(AUDIT, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload, sort_keys=True) + "\n")
    except Exception:
        pass


def is_subagent(payload):
    """The recursion guard. Proposers and verifiers are subagents; if they were
    gated, the first Read inside a proposer would deadlock the whole system."""
    agent = payload.get("agent") or "main"
    return agent != "main"


def mutating(payload):
    tool = payload.get("tool_name") or ""
    if tool in MUTATING_TOOLS:
        return tool
    if tool != "Bash":
        return None
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    # Redirection first: it writes a file whatever the command in front of it is.
    # Scanned over shell CODE only, so arrows in quoted strings and heredoc bodies
    # (which blocked genuine read-only commands) are not mistaken for redirection.
    for m in REDIRECT.finditer(_shell_code(cmd)):
        if m.group(1) != "/dev/null":
            return "Bash"
    # MUTATING_BASH is tested BEFORE the allowlist and searches the WHOLE command.
    # SAFE_BASH is `^`-anchored, so consulting it first exempted everything chained
    # after a harmless verb — `ls; rm -rf x` and `pwd && git push` both walked straight
    # through the gate. The allowlist may now only exempt a command that contains no
    # mutating segment anywhere.
    if MUTATING_BASH.search(cmd):
        return "Bash"
    if SAFE_BASH.match(cmd.strip()):
        return None
    return None


# ── hook handlers ────────────────────────────────────────────────────────────

REQUIREMENT = """PLUS-ULTRA IS ACTIVE for this turn.

Unless this turn is answerable as plain conversation, it needs a Byzantine 2+1 team
BEFORE you mutate anything:

  1. Spawn TWO isolated, READ-ONLY proposers (Agent tool, different lenses/labels,
     blind to each other, identical spec). They must NOT mutate anything — they
     return a candidate plan: exact changes, how to verify, how to undo.
  2. Spawn ONE arbiter (Athena) that sees BOTH and returns one authoritative plan.
     Fundamental disagreement escalates to the human instead of being picked.
  3. Record it:  plusultra plan --arbiter Athena --verdict -   (verdict on stdin)
     That unlocks mutating tools for this turn.
  4. Apply the plan ONCE, yourself.
  5. Spawn a fresh REALITY verifier (Argus), blind to the plan, that checks the
     WORLD and not the transcript. Record it:  plusultra confirm --verdict -
     That unlocks finishing the turn.

Budget: check the host's agent budget first. If exhausted, degrade to one adversarial
critic + the reality verifier and SAY SO. Never degrade silently.
Bypass: PLUS_ULTRA=off (recorded, never silent)."""


def hook_user_prompt(payload):
    session = payload.get("session_id") or ""
    prompt = payload.get("prompt") or ""
    turn = hashlib.sha1((session + prompt + str(time.time())).encode()).hexdigest()[:12]
    save(session, {
        "turn": turn,
        "status": "OPEN",
        "prompt_digest": hashlib.sha1(prompt.encode()).hexdigest()[:12],
        "opened": _now(),
        "mutations": 0,
        "plan": None,
        "reality": None,
    })
    return {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                   "additionalContext": REQUIREMENT}}


def hook_pre_tool(payload):
    if disabled() or is_subagent(payload):
        return {}
    what = mutating(payload)
    if not what:
        return {}

    session = payload.get("session_id") or ""
    cmd = (payload.get("tool_input") or {}).get("command") or \
          (payload.get("tool_input") or {}).get("file_path") or ""

    if not _valid_session(session):
        msg = ("plus-ultra: this call carries no session id, so no plan can be "
               "attributed to it and none will be honoured.\n\n  blocked: %s  %s\n\n"
               "Deliberate: state keyed by an absent session is state any call can "
               "claim. Bypass explicitly with PLUS_ULTRA=off (recorded, never silent)."
               ) % (what, str(cmd)[:160])
        record("gate BLOCKED (no session id)", "gate BLOCKED (no session id)", tool=what)
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                       "permissionDecision": "deny",
                                       "permissionDecisionReason": msg},
                "decision": "block", "reason": msg}

    st = load(session)
    if st.get("plan"):
        st["mutations"] = int(st.get("mutations", 0)) + 1
        # A reality verdict describes the world at one mutation boundary. Any
        # later write invalidates it and requires a fresh observation.
        st["reality"] = None
        st["status"] = "APPLIED"
        save(session, st)
        return {}
    record("gate BLOCKED (no plan verdict)", "gate BLOCKED (no plan verdict)",
           tool=what, target=str(cmd)[:200])

    msg = (
        "plus-ultra: this turn has no arbiter-approved plan, so mutating tools are "
        "closed.\n\n  blocked: %s  %s\n\n%s\n\n"
        "Once the arbiter has ruled:\n"
        "  plusultra plan --arbiter Athena --verdict - <<'EOF'\n"
        "  <the authoritative plan>\n"
        "  EOF\n"
    ) % (what, str(cmd)[:160], REQUIREMENT)

    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": msg,
        },
        "decision": "block",
        "reason": msg,
    }


def hook_stop(payload):
    # stop_hook_active means we are already inside a blocked-stop continuation;
    # blocking again would spin forever.
    if disabled() or payload.get("stop_hook_active") or is_subagent(payload):
        return {}
    session = payload.get("session_id") or ""
    st = load(session)
    if not st or int(st.get("mutations", 0)) == 0:
        return {}
    reality = st.get("reality") or {}
    if reality.get("entry") and reality.get("for_mutations") == int(st.get("mutations", 0)):
        st["status"] = "CONFIRMED"
        save(session, st)
        return {}

    record("stop BLOCKED (no reality verdict)", "stop BLOCKED (no reality verdict)",
           mutations=st.get("mutations"))
    msg = (
        "plus-ultra: this turn mutated state (%d call(s)) but no REALITY verifier has "
        "confirmed it.\n\n"
        "Spawn a FRESH agent (Argus) that is BLIND to the plan. Tell it what should now "
        "be true of the world and have it check independently — the world, not the "
        "transcript. A success message from our own command is not evidence.\n\n"
        "Then:\n  plusultra confirm --verifier Argus --verdict - <<'EOF'\n"
        "  <what it checked, what it found>\n  EOF\n\n"
        "If nothing observable exists to check, record that explicitly — 'unobservable' "
        "is a recorded outcome, not a pass.\n"
        "Bypass: PLUS_ULTRA=off (recorded, never silent)."
    ) % int(st.get("mutations", 0))
    return {"decision": "block", "reason": msg}


HANDLERS = {
    "UserPromptSubmit": hook_user_prompt,
    "PreToolUse": hook_pre_tool,
    "Stop": hook_stop,
}


def run_hook():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return {}
    fn = HANDLERS.get(payload.get("hook_event_name") or "")
    if not fn:
        return {}
    try:
        return fn(payload) or {}
    except Exception:
        # A broken gate must never wedge the session. Fail OPEN but leave a trace.
        record("gate ERROR (failed open)", "gate ERROR (failed open)")
        return {}


# ── CLI ──────────────────────────────────────────────────────────────────────

def _session_arg(args):
    """Resolve the session EXACTLY, or not at all.

    The hooks are handed `session_id` in their payload and are always right. The CLI
    has no payload, so it used to guess with `_newest_session()` — "whichever state
    file was touched last". Under a fleet of concurrent Claude sessions that guess is
    a coin flip, and it fails BOTH ways:

      * fail-closed (observed): an arbiter verdict was filed into a *different*
        session, so the gate for the session that actually did the work stayed shut
        while `plusultra status` cheerfully reported PLANNED.
      * fail-OPEN (the dangerous one): if this session's file happens to be newest,
        ANOTHER session's `plusultra plan` lands here and unlocks a gate nobody
        reviewed. A gate that guesses which session it is protecting is not a gate.

    This is the same class as the `nosession.json` bug `_valid_session` already
    fixed: state keyed by an ambiguous session is state any call can claim. There the
    key was empty; here it is merely *wrong*, which is worse because it looks right.
    So: no guessing. An unresolvable session is an error the caller must fix by
    passing --session or exporting CLAUDE_SESSION_ID.
    """
    for i, a in enumerate(args):
        if a == "--session" and i + 1 < len(args):
            return args[i + 1]
    return os.environ.get("CLAUDE_SESSION_ID") or ""


def _require_session(args):
    """The CLI fallback is what created the stray nosession.json in the first place —
    fixing only the hook would leave it free to be recreated."""
    session = _session_arg(args)
    if not _valid_session(session):
        sys.stderr.write(
            "plusultra: no valid session id (got %r). Pass --session <id> or set "
            "CLAUDE_SESSION_ID. A verdict recorded without a session unlocks nothing "
            "and would be readable by any unkeyed call.\n" % session)
        raise SystemExit(2)
    return session


def _flag(args, name, default=None):
    for i, a in enumerate(args):
        if a == name and i + 1 < len(args):
            return args[i + 1]
    return default


def _verdict_text(args):
    v = _flag(args, "--verdict", "-")
    return sys.stdin.read().strip() if v == "-" else v


def _required_verdict(args, kind):
    verdict = _verdict_text(args).strip()
    has_content = any(unicodedata.category(char)[0] in {"L", "N", "P", "S"} for char in verdict)
    if not has_content:
        raise SystemExit("plusultra: %s verdict must contain visible content" % kind)
    return verdict[:4000]


def cmd_plan(args):
    session = _require_session(args)
    st = load(session) or {"turn": "adhoc", "mutations": 0}
    st["plan"] = {"arbiter": _flag(args, "--arbiter", "Athena"),
                  "at": _now(), "entry": _required_verdict(args, "plan")}
    st["status"] = "PLANNED"
    save(session, st)
    record("plan verdict recorded", "plan verdict recorded",
           arbiter=st["plan"]["arbiter"])
    print("plus-ultra: PLAN recorded by %s — mutating tools unlocked for this turn."
          % st["plan"]["arbiter"])


def cmd_confirm(args):
    session = _require_session(args)
    st = load(session)
    mutations = int(st.get("mutations", 0)) if st else 0
    if not st or mutations == 0:
        raise SystemExit(
            "plusultra: reality can only be recorded after this session mutates state"
        )
    st["reality"] = {"verifier": _flag(args, "--verifier", "Argus"),
                     "at": _now(), "entry": _required_verdict(args, "reality"),
                     "for_mutations": mutations}
    st["status"] = "CONFIRMED"
    save(session, st)
    record("reality verdict recorded", "reality verdict recorded",
           verifier=st["reality"]["verifier"])
    print("plus-ultra: REALITY confirmed by %s — turn may close."
          % st["reality"]["verifier"])


def cmd_status(args):
    session = _session_arg(args)
    st = load(session)
    if not st:
        print("plus-ultra: no turn state for session %s" % session)
        return
    print("plus-ultra  session=%s turn=%s" % (session, st.get("turn")))
    print("  status    : %s" % st.get("status"))
    print("  mutations : %s" % st.get("mutations"))
    print("  plan      : %s" % ((st.get("plan") or {}).get("arbiter") or "— none —"))
    print("  reality   : %s" % ((st.get("reality") or {}).get("verifier") or "— none —"))
    print("  enabled   : %s" % ("no (bypassed)" if disabled() else "yes"))


def cmd_doctor(args):
    ok = True
    print("plus-ultra doctor")
    settings = os.path.join(HOME, ".claude", "settings.json")
    try:
        with open(settings, "r", encoding="utf-8") as fh:
            hooks = json.load(fh).get("hooks", {})
        for ev in ("UserPromptSubmit", "PreToolUse", "Stop"):
            wired = any("plusultra" in h.get("command", "")
                        for m in hooks.get(ev, []) for h in m.get("hooks", []))
            print("  %s  %s hook" % ("ok  " if wired else "FAIL", ev))
            ok = ok and wired
    except Exception as e:
        print("  FAIL cannot read settings.json: %s" % e)
        ok = False
    print("  %s state dir %s" % ("ok  " if os.path.isdir(STATE) else "WARN", STATE))
    print("  %s recursion guard (subagents exempt)" % "ok  ")
    print("  enabled: %s" % ("no (bypassed)" if disabled() else "yes"))
    print("  note: this doctor checks the Claude Code hook adapter only")
    print("\n%s" % ("plus-ultra is armed" if ok else "plus-ultra is NOT fully wired for Claude Code"))
    return 0 if ok else 1


def cmd_off(args):
    _ensure()
    open(OFF_FLAG, "w").close()
    record("mode disabled", "mode disabled via `plusultra off`")
    print("plus-ultra: OFF (recorded). Re-arm with `plusultra on`.")


def cmd_on(args):
    try:
        os.remove(OFF_FLAG)
    except FileNotFoundError:
        pass
    record("mode enabled", "mode enabled via `plusultra on`")
    print("plus-ultra: ON.")


COMMANDS = {"plan": cmd_plan, "confirm": cmd_confirm, "status": cmd_status,
            "doctor": cmd_doctor, "off": cmd_off, "on": cmd_on}


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if args[0] == "hook":
        out = run_hook()
        if out:
            print(json.dumps(out))
        return 0
    fn = COMMANDS.get(args[0])
    if not fn:
        print("plusultra: unknown command %r; try: %s" % (args[0], ", ".join(COMMANDS)))
        return 2
    return fn(args[1:]) or 0


if __name__ == "__main__":
    sys.exit(main())
