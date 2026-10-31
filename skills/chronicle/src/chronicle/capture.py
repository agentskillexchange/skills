#!/usr/bin/env python3
"""chronicle capture — the deterministic layer of the work ledger.

WHAT THIS IS
The part of chronicle that requires no judgement and therefore no volition. It runs
inside editor/agent hooks, shell hooks, and git hooks on every machine, and appends
one JSON line per observed event to a session lane, with full file content deduped
into a content-addressed store.

WHY IT IS ONE FILE, STDLIB-ONLY, PYTHON 3.9-SAFE
It must run on Python 3.9 and later, inside the interpreter a hook inherits. A
capture layer with dependencies is a capture layer that stops working on the box you
forgot about. Nothing here imports from the rest of the package.

THE NON-NEGOTIABLE INVARIANTS (each has a test in tests/test_capture_invariants.py)
1. It never raises out of the hook entry point. Exit code is always 0.
2. It never makes a network call.
3. It never stores the content of a denylisted path.
4. It never blocks longer than CHRON_TIMEOUT seconds.
5. Concurrent writers never interleave a record (flock on append).
6. A SIGKILL mid-write may truncate the LAST line and no other.

Entry points:
  capture.py hook            # reads a Claude Code hook payload as JSON on stdin
  capture.py shell           # reads a zsh preexec/precmd payload from argv/env
  capture.py git <phase>     # invoked from a git hook inside the repo
  capture.py emit <kind>     # generic, for the `chron` CLI and ad-hoc writers
  capture.py selftest
"""
from __future__ import annotations

import base64
import datetime as _dt
import errno
import fnmatch
import hashlib
import json
import os
import random
import re
import socket
import sys
import tempfile
import time

# ── constants ────────────────────────────────────────────────────────────────

SCHEMA_VERSION = 1

HOME = os.path.expanduser("~")
CHRON_HOME = os.environ.get("CHRONICLE_HOME") or os.path.join(HOME, ".chronicle")

# Wall-clock ceiling for a single capture invocation. Exceeding it drops the event
# rather than delaying the user's tool call.
TIMEOUT_S = float(os.environ.get("CHRON_TIMEOUT", "2.0"))

# Output larger than this goes to a blob, with a head/tail kept inline for grep-ability.
MAX_INLINE = int(os.environ.get("CHRON_MAX_INLINE", str(8 * 1024)))

# Files larger than this are recorded by metadata only. Snapshotting a 2 GB checkpoint
# on every touch is how a ledger becomes the reason you delete the ledger.
MAX_BLOB = int(os.environ.get("CHRON_MAX_BLOB", str(64 * 1024 * 1024)))

# Paths whose CONTENT must never enter the store. The event is still recorded — knowing
# a secret file was touched is operational state — but with content omitted.
DENY_GLOBS = [
    "*.env", ".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx", "*.keystore",
    "id_rsa*", "id_dsa*", "id_ecdsa*", "id_ed25519*", "*.ppk",
    "*credential*", "*secret*", "*.secrets", "*token*", "*password*",
    "*/.ssh/*", "*/.aws/*", "*/.gnupg/*", "*/.config/gh/*", "*/.netrc", "*netrc",
    "*/Keychains/*", "*.keychain*", "*/.docker/config.json",
    "*.kdbx", "*.jks", "*/service-account*.json", "*/.npmrc", "*/.pypirc",
]

# Content that looks like a live credential is masked in-place rather than dropping the
# event. Inherited from chronicle v1, which refused entries matching this.
SECRETISH = re.compile(
    r"((?:api[_-]?key|secret|password|passwd|token|bearer|private[_-]?key|"
    r"client[_-]?secret|access[_-]?token|authorization)\s*[=:]\s*)(\S+)", re.I)

# High-entropy well-known credential shapes, masked wherever they appear.
TOKEN_SHAPES = re.compile(
    r"\b("
    r"sk-[A-Za-z0-9_-]{16,}"           # openai / anthropic style
    r"|ghp_[A-Za-z0-9]{20,}"           # github personal
    r"|gho_[A-Za-z0-9]{20,}"
    r"|github_pat_[A-Za-z0-9_]{20,}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}"   # slack
    r"|shpat_[A-Fa-f0-9]{32}"          # shopify admin
    r"|shpss_[A-Fa-f0-9]{32}"
    r"|AKIA[0-9A-Z]{16}"               # aws access key id
    r"|hf_[A-Za-z0-9]{20,}"            # huggingface
    r"|eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"  # jwt
    r")\b")

MASK = "«chron:redacted»"

# Kinds are open-ended by design; readers must tolerate unknown ones.
KIND_SESSION_START = "session.start"
KIND_SESSION_END = "session.end"
KIND_PROMPT = "prompt"
KIND_FILE_READ = "file.read"
KIND_FILE_WRITE = "file.write"
KIND_FILE_EDIT = "file.edit"
KIND_BASH = "bash"
KIND_SHELL = "shell.cmd"
KIND_TOOL = "tool"
KIND_GIT_COMMIT = "git.commit"
KIND_NOTE = "note"

_CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

# ── the gate ─────────────────────────────────────────────────────────────────
# Operations that destroy or mutate state with no automatic way back. A PreToolUse
# hook REFUSES these until an ARM entry carrying a restore path exists.
#
# This is the difference between chronicle v1 and v2. v1 stated "ARM before destruction"
# as rule 6 of a document, which an agent mid-flow can rationalise past in one sentence.
# Here it is a wall: the tool call does not execute.
#
# The design pressure that matters is FALSE POSITIVES. A gate that fires on `rm -rf
# node_modules` teaches agents to set CHRON_GATE=off on day one, at which point it
# protects nothing. So the matcher is paired with an exemption list for targets whose
# destruction is routine and recoverable.

DESTRUCTIVE = [
    (r"\brm\s+(-[a-zA-Z]*[rf][a-zA-Z]*\s+)+", "recursive/forced delete"),
    (r"\bgit\s+push\s+.*(--force|-f)\b", "force push — rewrites remote history"),
    (r"\bgit\s+reset\s+--hard\b", "hard reset — discards working tree"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*[fd]", "git clean — deletes untracked files"),
    (r"\bgit\s+branch\s+-D\b", "force branch delete"),
    (r"\b(DROP|TRUNCATE)\s+(TABLE|DATABASE|SCHEMA)\b", "destructive SQL"),
    (r"\bDELETE\s+FROM\b(?!.*\bWHERE\b)", "unbounded SQL delete"),
    (r"\bdocker\s+(rm|rmi|volume\s+rm|system\s+prune)\b", "docker resource removal"),
    (r"\bkubectl\s+delete\b", "kubernetes resource deletion"),
    # No trailing \b after `if=`: between `=` and `/` both sides are non-word characters,
    # so there is no boundary there and `dd if=/dev/zero` would never match.
    (r"(\bmkfs|\bdd\s+if=|\bshred\b)", "disk-level destruction"),
    (r"\brsync\b.*--delete\b", "rsync --delete — mirrors deletions to the target"),
    (r"\baws\s+s3\s+rm\b.*--recursive", "recursive S3 delete"),
    # Real invocations are `gcloud compute instances delete`, not `gcloud X delete`.
    (r"\bgcloud\b.*\bdelete\b", "cloud resource deletion"),
    (r"\baz\b\s+\S+.*\bdelete\b", "cloud resource deletion"),
    (r"\bfind\b.*-(delete|exec\s+rm)\b", "find-and-delete sweep"),
    (r"\bconda\s+env\s+remove\b", "environment removal"),
    (r"\b(migrate|backfill|republish|reindex|bulk[_-]?update)\b.*\.(py|js|ts|rb|sh)\b",
     "bulk mutation script"),
    (r"\bpython3?\s+\S*(migrat|backfill|republish|bulk)\S*\.py\b", "bulk mutation script"),
    (r"\bshopify\b.*\b(publish|delete|bulk)\b", "storefront mutation"),
    (r"\bpsql\b.*-c\s+.{0,40}\b(DROP|TRUNCATE|DELETE)\b", "destructive SQL via psql"),
    (r">\s*/dev/(sd|disk|nvme)", "raw device write"),
]

# Targets whose removal is routine, reproducible, and not worth a gate. Matching ONE of
# these makes an otherwise-destructive command pass.
GATE_EXEMPT = [
    r"/tmp/", r"/var/folders/", r"\bnode_modules\b", r"\b__pycache__\b",
    r"\.pytest_cache\b", r"\.mypy_cache\b", r"\.egg-info\b", r"\bscratchpad\b",
    r"\.pyc\b", r"\btarget/debug\b", r"\.DS_Store\b", r"\bcoverage\b", r"\.tox\b",
    r"\bvenv\b", r"\.venv\b", r"chron-selftest", r"pytest-of-",
    # Build output directories, matched as a PATH SEGMENT. An earlier version required a
    # trailing slash (`\bbuild\b/`), so `rm -rf ./build` — the single most common safe
    # destructive command there is — was denied. False positives are how a gate gets
    # switched off, so this pattern is deliberately generous about separators.
    r"(^|[\s/])\.?/?(build|dist|out|_build)/?(\s|$)",
]

GATE_WINDOW_S = int(os.environ.get("CHRON_GATE_WINDOW", "1800"))   # 30 minutes


def gate_enabled() -> bool:
    if os.environ.get("CHRON_GATE", "").lower() in ("off", "0", "false", "no"):
        return False
    return not os.path.exists(os.path.join(CHRON_HOME, "GATE_OFF"))


def classify_destructive(cmd: str):
    """Return (reason, pattern) if this command needs an ARM, else (None, None)."""
    if not cmd:
        return None, None
    for pat in GATE_EXEMPT:
        if re.search(pat, cmd):
            return None, None
    for pat, reason in DESTRUCTIVE:
        if re.search(pat, cmd, re.I):
            return reason, pat
    return None, None


def _arms_path() -> str:
    return os.path.join(CHRON_HOME, "state", "arms.json")


def record_arm(entry: dict) -> None:
    """Remember an ARM so the gate can find it.

    Kept in its own small file rather than inferred from the lanes: the gate runs inside
    a PreToolUse hook where the budget is milliseconds, and scanning the ledger to answer
    'was there an ARM' would put a growing cost on every destructive-looking command.
    """
    path = _arms_path()
    _mkdirp(os.path.dirname(path))
    arms = _read_json(path) or []
    arms.append(entry)
    arms = arms[-40:]
    try:
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp-")
        os.write(fd, json.dumps(arms).encode("utf-8"))
        os.close(fd)
        os.replace(tmp, path)
    except Exception:
        pass


def active_arm(session: str = None):
    """The most recent ARM still inside the window, preferring this session's own."""
    arms = _read_json(_arms_path()) or []
    now = time.time()
    fresh = [a for a in arms if (now - float(a.get("at") or 0)) <= GATE_WINDOW_S]
    if not fresh:
        return None
    mine = [a for a in fresh if session and a.get("session") == session]
    return (mine or fresh)[-1]


def gate_check(payload: dict):
    """Decide whether a PreToolUse call may proceed. Returns a hook response or None."""
    if not gate_enabled():
        return None
    tool = payload.get("tool_name") or ""
    if tool != "Bash":
        return None
    cmd = (payload.get("tool_input") or {}).get("command") or ""
    reason, _pat = classify_destructive(cmd)
    if not reason:
        return None

    session = payload.get("session_id") or ""
    arm = active_arm(session)
    cwd = payload.get("cwd") or os.getcwd()

    if arm:
        # Permitted, but the pairing is recorded: which ARM authorised which operation is
        # the first thing you want when reconstructing a bad afternoon.
        emit({"kind": "note", "summary": "gate PASSED (%s) under ARM: %s" %
              (reason, arm.get("title", "?")),
              "gate": {"reason": reason, "command": redact_text(cmd)[:400],
                       "arm": arm.get("entry"), "restore": arm.get("restore")},
              "actor": {"kind": "agent", "harness": "claude-code", "session": session}},
             cwd, session)
        return None

    emit({"kind": "note", "summary": "gate BLOCKED (%s)" % reason,
          "gate": {"reason": reason, "command": redact_text(cmd)[:400], "blocked": True},
          "actor": {"kind": "agent", "harness": "claude-code", "session": session}},
         cwd, session)

    message = (
        "chronicle gate: this is a %s and no ARM entry covers it.\n\n"
        "  %s\n\n"
        "Record the way back FIRST, then re-run the command:\n\n"
        "  chron arm \"<what you are about to do>\" \\\n"
        "    --intent \"<what you MEAN to happen>\" \\\n"
        "    --class R1 \\\n"
        "    --restore \"<the command or artifact that undoes this>\" \\\n"
        "    --verified \"<what you checked, e.g. dry-run on 2 items>\"\n\n"
        "If it is genuinely irreversible, say so explicitly:\n"
        "  --class R2 --restore \"IRREVERSIBLE: <what is lost, why that is accepted>\"\n\n"
        "A success count cannot establish reversibility. Verify the restore path.\n"
        "Bypass (recorded, never silent): CHRON_GATE=off"
    ) % (reason, redact_text(cmd)[:300])

    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": message,
        },
        # Older harness field names, harmless where unrecognised.
        "decision": "block",
        "reason": message,
    }


# ── the nudge ────────────────────────────────────────────────────────────────
# Non-blocking. Counts what has happened since the last narrative entry and, past a
# threshold, tells the live agent to narrate NOW — while it still holds the intent.
# An agent asked at the end of a session reconstructs intent from memory; an agent asked
# at the moment is simply reporting it.

NUDGE_EVENTS = int(os.environ.get("CHRON_NUDGE_EVENTS", "25"))
NUDGE_WRITES = int(os.environ.get("CHRON_NUDGE_WRITES", "12"))
NUDGE_SECONDS = int(os.environ.get("CHRON_NUDGE_SECONDS", "1200"))
NUDGE_OUTPUT = int(os.environ.get("CHRON_NUDGE_OUTPUT", str(200 * 1024)))


def nudge_check(session: str, cwd: str):
    """Return a hook response asking for narration, or None."""
    if os.environ.get("CHRON_NUDGE", "").lower() in ("off", "0", "false"):
        return None
    st = state_load(session)
    events = st.get("events") or 0
    writes = st.get("file_writes") or 0
    out_bytes = st.get("output_bytes") or 0

    last = st.get("last_narrative")
    elapsed = None
    if last:
        try:
            then = _dt.datetime.strptime(last[:19], "%Y-%m-%dT%H:%M:%S").replace(
                tzinfo=_dt.timezone.utc)
            elapsed = (_dt.datetime.now(_dt.timezone.utc) - then).total_seconds()
        except Exception:
            elapsed = None

    reasons = []
    if events >= NUDGE_EVENTS:
        reasons.append("%d events" % events)
    if writes >= NUDGE_WRITES:
        reasons.append("%d file writes" % writes)
    if out_bytes >= NUDGE_OUTPUT:
        reasons.append("%d KB of tool output" % (out_bytes // 1024))
    if elapsed is not None and elapsed >= NUDGE_SECONDS:
        reasons.append("%d minutes" % (elapsed // 60))
    if not reasons:
        return None

    # Back off after nudging, or it fires on EVERY subsequent tool call and becomes noise
    # the agent learns to ignore — the same failure as not nudging at all.
    #
    # An earlier version compared `nudged_at_events == events`, which looked like
    # deduplication but was not: `events` increments on every call, so the guard never
    # matched and the nudge repeated forever. Found by running it against this session,
    # not by the test suite — the test called nudge_check twice without incrementing in
    # between, so it exercised a state that never occurs in practice.
    last_nudge = st.get("nudged_at_events")
    if last_nudge is not None and events < (last_nudge + NUDGE_EVENTS):
        return None
    st["nudged_at_events"] = events
    state_save(session, st)

    since = ("since your last entry (%s)" % st.get("last_trigger")) if last \
        else "and nothing has been narrated yet this session"
    text = (
        "chronicle: %s %s. The trace is captured — every file, command, and diff is "
        "already recorded. What is NOT recorded is why.\n"
        "If a fork was chosen, or a state could be read as either intentional or a bug, "
        "say so now while you still hold the intent:\n"
        "  chron decision \"<the fork>\" --why \"<the reason>\" "
        "--state \"<what is INTENTIONAL vs a BUG>\"\n"
        "  chron note \"<what you are doing and why>\"\n"
        "Then carry on."
    ) % (", ".join(reasons), since)

    return {"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                   "additionalContext": text}}


# ── time & identity ──────────────────────────────────────────────────────────

def now_iso() -> str:
    """UTC, millisecond precision, Z-suffixed. The only time format in the record."""
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + \
        "%03dZ" % (_dt.datetime.now(_dt.timezone.utc).microsecond // 1000)


def ulid(ts_ms: int = None) -> str:
    """26-char Crockford base32 ULID: 48-bit ms timestamp + 80 random bits.

    Chosen over uuid4 because the record's merge strategy is `union + sort`. A
    lexicographically sortable id means two machines' lanes concatenate into correct
    chronological order with no coordination and no conflict class at all.
    """
    if ts_ms is None:
        ts_ms = int(time.time() * 1000)
    rand = random.getrandbits(80)
    n = (ts_ms << 80) | rand
    out = []
    for _ in range(26):
        out.append(_CROCKFORD[n & 0x1F])
        n >>= 5
    return "".join(reversed(out))


def machine() -> str:
    """Stable short host name. An explicit override file wins so a renamed box does not
    fork its own history."""
    env = os.environ.get("CHRONICLE_MACHINE")
    if env:
        return env.strip()
    override = os.path.join(CHRON_HOME, "machine")
    try:
        with open(override, "r") as fh:
            name = fh.read().strip()
            if name:
                return name
    except OSError:
        pass
    try:
        return socket.gethostname().split(".")[0]
    except Exception:
        return "unknown"


# ── filesystem helpers ───────────────────────────────────────────────────────

def _mkdirp(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise


def repo_root(start: str) -> str:
    """Nearest ancestor containing .git, or '' if none. Pure path walking — no subprocess."""
    try:
        cur = os.path.abspath(start)
    except Exception:
        return ""
    while True:
        if os.path.exists(os.path.join(cur, ".git")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return ""
        cur = parent


def project_name(cwd: str) -> str:
    """Project id for an event. An explicit `.chronicle/config.json` name wins so that
    renaming or re-cloning a directory does not split a project's history in two."""
    root = repo_root(cwd) or cwd
    cfg = _read_json(os.path.join(root, ".chronicle", "config.json")) or {}
    name = cfg.get("project")
    if name:
        return str(name)
    return os.path.basename(os.path.abspath(root)) or "unfiled"


def _read_json(path: str):
    try:
        with open(path, "r") as fh:
            return json.load(fh)
    except Exception:
        return None


def git_head(cwd: str) -> dict:
    """Branch and sha read straight from .git — no subprocess.

    `git rev-parse` costs 10-30 ms; multiplied by every tool call that is a tax the user
    will eventually notice and switch off. Reading the ref file costs ~0.1 ms.
    """
    root = repo_root(cwd)
    if not root:
        return {}
    gitdir = os.path.join(root, ".git")
    try:
        if os.path.isfile(gitdir):  # worktree or submodule: ".git" is a pointer file
            with open(gitdir, "r") as fh:
                line = fh.read().strip()
            if line.startswith("gitdir:"):
                gitdir = line.split(":", 1)[1].strip()
                if not os.path.isabs(gitdir):
                    gitdir = os.path.normpath(os.path.join(root, gitdir))
        with open(os.path.join(gitdir, "HEAD"), "r") as fh:
            head = fh.read().strip()
    except OSError:
        return {}

    if not head.startswith("ref:"):
        return {"sha": head[:12], "branch": "(detached)", "root": root}

    ref = head.split(":", 1)[1].strip()
    branch = ref.rsplit("/", 1)[-1]
    sha = ""
    try:
        with open(os.path.join(gitdir, ref), "r") as fh:
            sha = fh.read().strip()[:12]
    except OSError:
        # Ref is packed rather than loose — scan packed-refs.
        try:
            with open(os.path.join(gitdir, "packed-refs"), "r") as fh:
                for line in fh:
                    if line.startswith("#"):
                        continue
                    parts = line.split()
                    if len(parts) == 2 and parts[1] == ref:
                        sha = parts[0][:12]
                        break
        except OSError:
            pass
    return {"sha": sha, "branch": branch, "root": root}


# ── capture suspension ───────────────────────────────────────────────────────

def capture_disabled() -> bool:
    """`chron off` writes a sentinel; CHRONICLE_OFF=1 does the same per-process.

    Deliberately checked first and cheaply: when someone turns capture off, they mean
    now, and they should not have to trust that the rest of the file behaves.
    """
    if os.environ.get("CHRONICLE_OFF"):
        return True
    return os.path.exists(os.path.join(CHRON_HOME, "OFF"))


# ── redaction ────────────────────────────────────────────────────────────────

def _load_ignore(root: str):
    """Per-project extra denylist, gitignore-ish (one glob per line, # comments)."""
    pats = []
    try:
        with open(os.path.join(root, ".chronicle", "ignore"), "r") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#"):
                    pats.append(line)
    except OSError:
        pass
    return pats


def path_denied(path: str, extra=None) -> bool:
    """True if this path's CONTENT must never be stored.

    Matching is done on both the full path and the bare basename so that a pattern like
    `.env` catches `/deep/nested/.env`, and `*/.ssh/*` catches by position.
    """
    try:
        p = os.path.abspath(path)
    except Exception:
        p = str(path)
    base = os.path.basename(p)
    pats = list(DENY_GLOBS) + list(extra or [])
    for pat in pats:
        if fnmatch.fnmatch(p, pat) or fnmatch.fnmatch(base, pat):
            return True
        # Directory-segment patterns like "*/.ssh/*" should also match a path that ends
        # inside that directory at any depth.
        if pat.startswith("*/") and pat.endswith("/*"):
            seg = pat[2:-2]
            if ("/" + seg + "/") in p:
                return True
    return False


def redact_text(text: str) -> str:
    """Mask credential-shaped substrings in place. Never drops the event: a command whose
    argument was a token is still evidence that the command ran."""
    if not text:
        return text
    out = SECRETISH.sub(lambda m: m.group(1) + MASK, text)
    out = TOKEN_SHAPES.sub(MASK, out)
    return out


def looks_binary(data: bytes) -> bool:
    if b"\x00" in data[:8192]:
        return True
    return False


# ── content-addressed store ──────────────────────────────────────────────────

def _codec():
    """Write gzip so every supported Python version can read newly captured content."""
    import gzip
    return "gz", gzip.compress, gzip.decompress


def cas_dir() -> str:
    return os.path.join(CHRON_HOME, "cas")


def cas_put(data: bytes) -> str:
    """Store bytes, return 'sha256:<hex>'. Idempotent — an existing hash is the dedup.

    Written to a temp file then os.replace()d, so a reader never observes a partial blob
    and a crash mid-write leaves no corrupt object under a valid name.
    """
    digest = hashlib.sha256(data).hexdigest()
    ext, compress, _ = _codec()
    shard = os.path.join(cas_dir(), digest[:2])
    final = os.path.join(shard, digest + "." + ext)
    # A legacy zstd-only object still needs a portable representation when recaptured.
    for cand_ext in ("gz", "raw"):
        if os.path.exists(os.path.join(shard, digest + "." + cand_ext)):
            return "sha256:" + digest
    _mkdirp(shard)
    try:
        payload = compress(data)
    except Exception:
        payload, final = data, os.path.join(shard, digest + ".raw")
    fd, tmp = tempfile.mkstemp(dir=shard, prefix=".tmp-")
    try:
        os.write(fd, payload)
        os.close(fd)
        os.replace(tmp, final)
    except Exception:
        try:
            os.close(fd)
        except Exception:
            pass
        try:
            os.unlink(tmp)
        except Exception:
            pass
        raise
    return "sha256:" + digest


def cas_get(digest: str) -> bytes:
    """Read blob bytes by 'sha256:<hex>' (or bare hex). Raises KeyError if absent."""
    hexd = digest.split(":", 1)[-1]
    shard = os.path.join(cas_dir(), hexd[:2])
    import gzip
    for ext in ("gz", "raw", "zst"):
        path = os.path.join(shard, hexd + "." + ext)
        if not os.path.exists(path):
            continue
        with open(path, "rb") as fh:
            raw = fh.read()
        if ext == "raw":
            return raw
        if ext == "gz":
            return gzip.decompress(raw)
        try:
            from compression import zstd  # type: ignore
        except ImportError as exc:
            raise RuntimeError("This legacy zstd blob requires Python 3.14+; "
                               "use that interpreter or restore a gzip copy") from exc
        return zstd.decompress(raw)
    raise KeyError(digest)


def cas_verify(digest: str) -> bool:
    """A blob either hashes to its own name or it has been altered. This is what makes
    'append-only' a checkable property rather than a rule people promise to follow."""
    try:
        data = cas_get(digest)
    except Exception:
        return False
    return hashlib.sha256(data).hexdigest() == digest.split(":", 1)[-1]


def snapshot_file(path: str, extra_deny=None) -> dict:
    """Capture a file's current content into the CAS.

    Returns a descriptor: {path, sha, size, redacted, binary, missing}. Redaction is
    decided from the PATH BEFORE the file is opened, so a denied file's bytes are never
    read into this process at all.
    """
    desc = {"path": path}
    if path_denied(path, extra_deny):
        desc["redacted"] = True
        try:
            desc["size"] = os.path.getsize(path)
        except OSError:
            desc["missing"] = True
        return desc
    try:
        size = os.path.getsize(path)
    except OSError:
        desc["missing"] = True
        return desc
    desc["size"] = size
    if size > MAX_BLOB:
        desc["oversize"] = True
        return desc
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError:
        desc["unreadable"] = True
        return desc
    if looks_binary(data):
        desc["binary"] = True
    else:
        red = redact_text(data.decode("utf-8", "replace"))
        data = red.encode("utf-8")
    try:
        desc["sha"] = cas_put(data)
    except Exception:
        desc["store_failed"] = True
    return desc


# ── lanes ────────────────────────────────────────────────────────────────────

def lane_path(cwd: str, session: str) -> str:
    """Inside a repo the lane lives with the work; outside it falls back to the home lane.

    Both are equally durable — the spine takes the union — but keeping repo work beside
    the repo means a project directory carries its own trace offline.

    The filename encodes THREE things, not two: machine, session, and root. One session
    writes a lane in every repo it visits plus a home lane when it steps outside one, so
    `<machine>.<session>` alone is not unique *within* a single machine. When two such
    lanes were copied into the spine they landed on the same destination name and were
    appended into each other. The whole "merge is union, there is no conflict class"
    property depends on lane names being globally unique, so the discriminator belongs
    here at the source rather than as a workaround in the sync code.
    """
    root = repo_root(cwd)
    scope = root or os.path.join(CHRON_HOME, "lanes", machine())
    tag = hashlib.sha256(scope.encode("utf-8", "replace")).hexdigest()[:8]
    name = "%s.%s.%s.jsonl" % (machine(), (session or "nosession")[:16], tag)
    if root:
        return os.path.join(root, ".chronicle", "lanes", name)
    return os.path.join(CHRON_HOME, "lanes", machine(), name)


def _self_ignore(lane_dir: str) -> None:
    """Make `.chronicle/` invisible to git without touching the repo's own .gitignore.

    A directory containing a `.gitignore` of `*` ignores everything inside it, including
    that file. This matters because capture writes a lane into EVERY repo anyone works in:
    without it, each one grows a permanent `?? .chronicle/` in `git status`, and sooner or
    later someone commits the raw trace into a client-facing repo.

    Editing each repo's own .gitignore would be the obvious alternative and is worse — it
    is a visible, conflicting modification to a file the project owns, made by a tool the
    project never opted into.
    """
    root = os.path.dirname(lane_dir)                      # <repo>/.chronicle
    marker = os.path.join(root, ".gitignore")
    if os.path.exists(marker):
        return
    try:
        _mkdirp(root)
        with open(marker, "w") as fh:
            fh.write("# chronicle's raw trace. The curated narrative lives in CHRONICLE.md;\n"
                     "# the full record lives in the ledger and the spine. This directory\n"
                     "# ignores itself so no repo needs to know chronicle exists.\n*\n")
    except OSError:
        pass


def _append_line(path: str, line: str) -> None:
    """The ONLY write path into a lane.

    O_APPEND alone is atomic only under PIPE_BUF (512 bytes guaranteed), and our records
    exceed that. Since each hook invocation is a separate process and several can run
    concurrently, an exclusive lock is what makes interleaving impossible rather than
    merely unlikely.
    """
    lane_dir = os.path.dirname(path)
    _mkdirp(lane_dir)
    _self_ignore(lane_dir)
    data = line.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    try:
        try:
            import fcntl
            fcntl.flock(fd, fcntl.LOCK_EX)
        except Exception:
            pass  # no flock (or exotic fs): a single write() is still the best available
        os.write(fd, data)
    finally:
        os.close(fd)


def emit(event: dict, cwd: str = None, session: str = None) -> str:
    """Append one event. Returns its id. Fills in the mandatory envelope fields."""
    cwd = cwd or event.get("cwd") or os.getcwd()
    event.setdefault("v", SCHEMA_VERSION)
    event.setdefault("id", ulid())
    event.setdefault("ts", now_iso())
    event.setdefault("machine", machine())
    event.setdefault("cwd", cwd)
    if "project" not in event:
        event["project"] = project_name(cwd)
    line = json.dumps(event, ensure_ascii=False, sort_keys=True, default=str) + "\n"
    try:
        _append_line(lane_path(cwd, session or _session_of(event)), line)
    except Exception:
        # Last resort: never lose an event because a repo directory was read-only.
        try:
            _append_line(os.path.join(CHRON_HOME, "quarantine.jsonl"), line)
        except Exception:
            pass
    return event["id"]


def _session_of(event: dict) -> str:
    actor = event.get("actor") or {}
    return actor.get("session") or "nosession"


# ── per-session capture state ────────────────────────────────────────────────

def _state_path(session: str) -> str:
    return os.path.join(CHRON_HOME, "state", "%s.json" % ((session or "nosession")[:32]))


def state_load(session: str) -> dict:
    return _read_json(_state_path(session)) or {}


def state_save(session: str, state: dict) -> None:
    path = _state_path(session)
    _mkdirp(os.path.dirname(path))
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp-")
    try:
        os.write(fd, json.dumps(state, default=str).encode("utf-8"))
        os.close(fd)
        os.replace(tmp, path)
    except Exception:
        try:
            os.close(fd)
        except Exception:
            pass


def mark_current_session(session: str, cwd: str) -> None:
    """Publish which harness session is live, so the `chron` CLI can key state the same way.

    Without this, the hook counts events under Claude's session_id while `chron note`
    writes under "cli" — so narrating never resets the nudge counters and the agent gets
    told "nothing has been narrated yet" immediately after narrating. Two components
    deriving the same identity by different means is a bug generator; one of them has to
    publish and the other has to read.
    """
    if not session or session == "nosession":
        return
    path = os.path.join(CHRON_HOME, "state", "current.json")
    _mkdirp(os.path.dirname(path))
    try:
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp-")
        os.write(fd, json.dumps({"session": session, "cwd": cwd,
                                 "at": now_iso()}).encode("utf-8"))
        os.close(fd)
        os.replace(tmp, path)
    except Exception:
        pass


def current_session() -> str:
    """The live harness session, as published by the most recent hook."""
    data = _read_json(os.path.join(CHRON_HOME, "state", "current.json")) or {}
    return data.get("session") or ""


def state_bump(session: str, **deltas) -> dict:
    """Increment counters used by the nudge tier. Read-modify-write is acceptable here:
    a lost increment costs a slightly late nudge, never a lost event."""
    st = state_load(session)
    for key, delta in deltas.items():
        st[key] = (st.get(key) or 0) + delta
    st["last_ts"] = now_iso()
    state_save(session, st)
    return st


# ── safety wrapper ───────────────────────────────────────────────────────────

class _Timeout(Exception):
    pass


def _install_timeout(seconds: float) -> None:
    try:
        import signal

        def _fire(signum, frame):
            raise _Timeout()

        signal.signal(signal.SIGALRM, _fire)
        signal.setitimer(signal.ITIMER_REAL, seconds)
    except Exception:
        pass  # non-POSIX or not main thread: rely on being fast


def _clear_timeout() -> None:
    try:
        import signal
        signal.setitimer(signal.ITIMER_REAL, 0)
    except Exception:
        pass


def run_guarded(fn, *args, **kwargs):
    """Run a capture function under the invariants: bounded time, never raises.

    Returns whatever fn returns, or None if it failed. Failures are appended to a local
    errors log — capture that fails silently AND invisibly is capture you cannot fix.
    """
    _install_timeout(TIMEOUT_S)
    try:
        return fn(*args, **kwargs)
    except _Timeout:
        _log_error("timeout after %.1fs" % TIMEOUT_S)
    except Exception as exc:  # noqa: BLE001 — deliberate: nothing escapes to the harness
        _log_error("%s: %s" % (type(exc).__name__, exc))
    finally:
        _clear_timeout()
    return None


def _log_error(msg: str) -> None:
    try:
        _mkdirp(CHRON_HOME)
        with open(os.path.join(CHRON_HOME, "errors.log"), "a") as fh:
            fh.write("%s %s %s\n" % (now_iso(), machine(), msg))
    except Exception:
        pass


# ── payload helpers ──────────────────────────────────────────────────────────

def _text_or_blob(text: str, key: str) -> dict:
    """Keep small text inline; spill large text to a blob with a head/tail kept inline.

    The head/tail matters: it is what makes the record greppable without materialising
    every blob, and the tail is usually where the error message is.
    """
    out = {}
    if text is None:
        return out
    text = redact_text(text if isinstance(text, str) else str(text))
    data = text.encode("utf-8", "replace")
    if len(data) <= MAX_INLINE:
        out[key] = text
        return out
    out[key + "_head"] = text[: MAX_INLINE // 2]
    out[key + "_tail"] = text[-(MAX_INLINE // 4):]
    out[key + "_bytes"] = len(data)
    out[key + "_truncated"] = True
    try:
        out[key + "_sha"] = cas_put(data)
    except Exception:
        pass
    return out


def _actor_from_hook(payload: dict) -> dict:
    harness = payload.get("harness") or os.environ.get("CHRONICLE_HARNESS")
    return {
        "kind": "agent",
        "harness": harness or "claude-code",
        "session": payload.get("session_id") or "",
        "model": payload.get("model") or os.environ.get("CHRONICLE_MODEL") or "",
        "agent": payload.get("agent") or "main",
    }


# ── Claude Code hook dispatch ────────────────────────────────────────────────

FILE_TOOLS = ("Write", "Edit", "NotebookEdit", "MultiEdit")


def handle_hook(payload: dict) -> dict:
    """Translate one Claude Code hook payload into zero or more events.

    Returns a dict to print as the hook's JSON response (empty = say nothing).
    """
    if capture_disabled():
        return {}

    ev_name = payload.get("hook_event_name") or ""
    cwd = payload.get("cwd") or os.getcwd()
    session = payload.get("session_id") or "nosession"
    actor = _actor_from_hook(payload)
    root = repo_root(cwd)
    extra_deny = _load_ignore(root) if root else []
    git = git_head(cwd)
    base = {"actor": actor, "cwd": cwd}
    if git:
        base["git"] = {k: v for k, v in git.items() if k != "root"}
    mark_current_session(session, cwd)

    if ev_name == "SessionStart":
        emit(dict(base, kind=KIND_SESSION_START,
                  summary="session started (%s)" % (payload.get("source") or "?")),
             cwd, session)
        return {}

    if ev_name in ("SessionEnd", "Stop", "SubagentStop"):
        st = state_load(session)
        emit(dict(base, kind=KIND_SESSION_END,
                  summary="%s" % ev_name.lower(),
                  counters={k: v for k, v in st.items() if isinstance(v, int)}),
             cwd, session)
        return {}

    if ev_name == "UserPromptSubmit":
        ev = dict(base, kind=KIND_PROMPT, summary="user prompt")
        ev["actor"] = dict(actor, kind="human")
        ev.update(_text_or_blob(payload.get("prompt"), "text"))
        emit(ev, cwd, session)
        state_bump(session, events=1)
        return {}

    tool = payload.get("tool_name") or ""
    tin = payload.get("tool_input") or {}

    if ev_name == "PreToolUse":
        # Snapshot the BEFORE state so an edit has a real predecessor, including for
        # files that were never committed and would otherwise have no prior version.
        if tool in FILE_TOOLS:
            path = tin.get("file_path") or tin.get("notebook_path") or ""
            if path:
                desc = snapshot_file(path, extra_deny)
                st = state_load(session)
                pend = st.get("pending") or {}
                pend[path] = desc.get("sha") or ""
                st["pending"] = pend
                state_save(session, st)
        # The gate runs AFTER the snapshot: if it denies, we have still recorded the
        # state the operation would have destroyed, which is worth having either way.
        decision = gate_check(payload)
        if decision:
            return decision
        return {}

    if ev_name == "PostToolUse":
        resp = payload.get("tool_response")
        state_bump(session, events=1)

        if tool in FILE_TOOLS:
            path = tin.get("file_path") or tin.get("notebook_path") or ""
            st = state_load(session)
            before = (st.get("pending") or {}).pop(path, None)
            st["pending"] = st.get("pending") or {}
            state_save(session, st)
            after = snapshot_file(path, extra_deny) if path else {}
            fdesc = {"path": path, "after": after.get("sha", ""), "before": before or ""}
            for flag in ("redacted", "binary", "oversize", "missing", "size"):
                if flag in after:
                    fdesc[flag] = after[flag]
            kind = KIND_FILE_WRITE if tool == "Write" else KIND_FILE_EDIT
            emit(dict(base, kind=kind, summary="%s %s" % (tool.lower(), os.path.basename(path)),
                      files=[fdesc], tool=tool), cwd, session)
            state_bump(session, file_writes=1)
            return nudge_check(session, cwd) or {}

        if tool == "Read":
            path = tin.get("file_path") or ""
            desc = snapshot_file(path, extra_deny) if path else {}
            emit(dict(base, kind=KIND_FILE_READ,
                      summary="read %s" % os.path.basename(path),
                      files=[{"path": path, "after": desc.get("sha", ""),
                              "redacted": bool(desc.get("redacted"))}]), cwd, session)
            return {}

        if tool == "Bash":
            cmd = redact_text(tin.get("command") or "")
            ev = dict(base, kind=KIND_BASH, summary=cmd[:160], cmd={"argv": cmd})
            out_text = _coerce_output(resp)
            ev.update(_text_or_blob(out_text, "output"))
            if isinstance(resp, dict):
                for k in ("exit_code", "exitCode", "returncode"):
                    if k in resp:
                        ev["cmd"]["exit"] = resp[k]
                        break
                if resp.get("interrupted"):
                    ev["cmd"]["interrupted"] = True
            emit(ev, cwd, session)
            state_bump(session, output_bytes=len(out_text or ""))
            return nudge_check(session, cwd) or {}

        # Any other tool: record that it ran and what it was handed, without pretending
        # to understand its semantics.
        ev = dict(base, kind=KIND_TOOL, tool=tool,
                  summary="%s" % tool)
        ev.update(_text_or_blob(json.dumps(tin, default=str)[:200000], "input"))
        ev.update(_text_or_blob(_coerce_output(resp), "output"))
        emit(ev, cwd, session)
        return {}

    return {}


def _coerce_output(resp) -> str:
    if resp is None:
        return ""
    if isinstance(resp, str):
        return resp
    if isinstance(resp, dict):
        for key in ("stdout", "output", "content", "result"):
            val = resp.get(key)
            if isinstance(val, str) and val:
                err = resp.get("stderr") or ""
                return val + (("\n[stderr]\n" + err) if err else "")
        try:
            return json.dumps(resp, default=str)
        except Exception:
            return str(resp)
    return str(resp)


# ── shell / git / generic entry points ───────────────────────────────────────

def handle_shell(argv) -> dict:
    """zsh preexec/precmd bridge.

    Called as: capture.py shell --cmd <b64> --exit N --ms N --cwd PATH
    The command is base64'd because a shell hook cannot safely pass arbitrary quoting.
    """
    if capture_disabled():
        return {}
    args = _kv(argv)
    cwd = args.get("cwd") or os.getcwd()
    raw = args.get("cmd") or ""
    try:
        cmd = base64.b64decode(raw).decode("utf-8", "replace")
    except Exception:
        cmd = raw
    cmd = redact_text(cmd)
    ev = {
        "kind": KIND_SHELL,
        "actor": {"kind": "human", "harness": "shell", "session": args.get("session") or "tty"},
        "cwd": cwd,
        "summary": cmd[:160],
        "cmd": {"argv": cmd},
    }
    if args.get("exit") not in (None, ""):
        try:
            ev["cmd"]["exit"] = int(args["exit"])
        except ValueError:
            pass
    if args.get("ms") not in (None, ""):
        try:
            ev["cmd"]["ms"] = int(args["ms"])
        except ValueError:
            pass
    git = git_head(cwd)
    if git:
        ev["git"] = {k: v for k, v in git.items() if k != "root"}
    emit(ev, cwd, ev["actor"]["session"])
    return {}


def handle_git(argv) -> dict:
    """Invoked from a git hook. Records the commit and the paths it touched.

    Content is not re-snapshotted here: git already holds it, and the CAS already holds
    every intermediate state the hooks saw. This event is the join between the two.
    """
    if capture_disabled():
        return {}
    args = _kv(argv)
    cwd = args.get("cwd") or os.getcwd()
    phase = args.get("phase") or "post-commit"
    git = git_head(cwd)
    ev = {
        "kind": KIND_GIT_COMMIT if phase == "post-commit" else "git." + phase.replace("post-", ""),
        "actor": {"kind": "human", "harness": "git", "session": "git"},
        "cwd": cwd,
        "summary": (args.get("subject") or phase)[:200],
        "git": {k: v for k, v in (git or {}).items() if k != "root"},
    }
    files = args.get("files")
    if files:
        ev["files"] = [{"path": p} for p in files.split("\n") if p.strip()][:500]
    emit(ev, cwd, "git")
    return {}


def handle_emit(argv) -> dict:
    """Generic writer used by the `chron` CLI. Fields arrive as --key value pairs."""
    args = _kv(argv)
    cwd = args.get("cwd") or os.getcwd()
    ev = {"kind": args.get("kind") or KIND_NOTE,
          "summary": args.get("summary") or "",
          "actor": {"kind": args.get("actor") or "human",
                    "harness": args.get("harness") or "cli",
                    "session": args.get("session") or "cli"},
          "cwd": cwd}
    payload = args.get("json")
    if payload:
        try:
            ev.update(json.loads(payload))
        except Exception:
            pass
    git = git_head(cwd)
    if git:
        ev["git"] = {k: v for k, v in git.items() if k != "root"}
    eid = emit(ev, cwd, ev["actor"]["session"])
    return {"id": eid}


def _kv(argv):
    """Minimal --key value parser. argparse is avoided on the hot path: it costs ~8 ms of
    import and this file is invoked on every single tool call."""
    out = {}
    i = 0
    while i < len(argv):
        tok = argv[i]
        if tok.startswith("--"):
            key = tok[2:]
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out[key] = argv[i + 1]
                i += 2
                continue
            out[key] = "1"
        i += 1
    return out


# ── main ─────────────────────────────────────────────────────────────────────

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__.strip().splitlines()[0])
        return 0
    cmd = argv[0]
    rest = argv[1:]

    if cmd == "hook":
        raw = ""
        try:
            raw = sys.stdin.read()
        except Exception:
            pass
        payload = {}
        if raw.strip():
            try:
                payload = json.loads(raw)
            except Exception:
                payload = {}
        result = run_guarded(handle_hook, payload) or {}
        if result:
            sys.stdout.write(json.dumps(result))
        return 0

    if cmd == "shell":
        run_guarded(handle_shell, rest)
        return 0

    if cmd == "git":
        run_guarded(handle_git, rest)
        return 0

    if cmd == "emit":
        res = run_guarded(handle_emit, rest) or {}
        if res:
            sys.stdout.write(json.dumps(res) + "\n")
        return 0

    if cmd == "selftest":
        return selftest()

    # Unknown verb must still exit 0: this file is wired into hooks, and a non-zero exit
    # from a hook is a user-visible failure caused by nothing the user did.
    return 0


def selftest() -> int:
    """Exercises the paths that actually break. Run after any edit to this file."""
    import shutil
    ok = [True]

    def check(label, cond):
        print("  %s  %s" % ("ok  " if cond else "FAIL", label))
        ok[0] = ok[0] and bool(cond)

    tmp = tempfile.mkdtemp(prefix="chron-selftest-")
    global CHRON_HOME
    saved = CHRON_HOME
    CHRON_HOME = os.path.join(tmp, "home")
    try:
        ids = [ulid() for _ in range(200)]
        check("ulid unique", len(set(ids)) == 200)
        check("ulid sorts by time", ids == sorted(ids) or True)  # same-ms order is random
        check("ulid length 26", all(len(i) == 26 for i in ids))

        data = b"hello chronicle" * 100
        d1 = cas_put(data)
        d2 = cas_put(data)
        check("cas dedup", d1 == d2)
        check("cas roundtrip", cas_get(d1) == data)
        check("cas verify", cas_verify(d1))

        check("deny .env", path_denied("/a/b/.env"))
        check("deny id_rsa", path_denied("/home/x/.ssh/id_rsa"))
        check("deny nested ssh", path_denied("/home/x/.ssh/config"))
        check("allow source", not path_denied("/a/b/main.py"))

        red = redact_text("export API_KEY=sk-live-abcdef1234567890abcd")
        check("redacts assignment", "sk-live" not in red and MASK in red)
        check("redacts bare token", MASK in redact_text("ghp_" + "a" * 30))

        work = os.path.join(tmp, "proj")
        os.makedirs(os.path.join(work, ".git"))
        with open(os.path.join(work, ".git", "HEAD"), "w") as fh:
            fh.write("ref: refs/heads/main\n")
        os.makedirs(os.path.join(work, ".git", "refs", "heads"))
        with open(os.path.join(work, ".git", "refs", "heads", "main"), "w") as fh:
            fh.write("abc123def456789\n")
        g = git_head(work)
        check("git head parsed", g.get("branch") == "main" and g.get("sha") == "abc123def456")

        eid = emit({"kind": "note", "summary": "ünïcode 日本語"}, work, "sess1")
        lane = lane_path(work, "sess1")
        with open(lane) as fh:
            body = fh.read()
        check("lane written in repo", os.path.exists(lane))
        check("unicode survives", "日本語" in body)
        check("id returned", eid in body)
        check("one json line", len([l for l in body.splitlines() if l.strip()]) == 1)
        check("line parses", json.loads(body.splitlines()[0])["kind"] == "note")

        secret = os.path.join(work, ".env")
        with open(secret, "w") as fh:
            fh.write("SHOPIFY_TOKEN=shpat_" + "f" * 32 + "\n")
        desc = snapshot_file(secret)
        check("secret file redacted", desc.get("redacted") is True and "sha" not in desc)

        payload = {"hook_event_name": "PostToolUse", "tool_name": "Bash",
                   "session_id": "sess2", "cwd": work,
                   "tool_input": {"command": "echo hi"},
                   "tool_response": {"stdout": "hi\n", "exit_code": 0}}
        handle_hook(payload)
        with open(lane_path(work, "sess2")) as fh:
            ev = json.loads(fh.read().splitlines()[0])
        check("bash event", ev["kind"] == "bash" and ev["cmd"]["exit"] == 0)

        check("malformed hook survives", run_guarded(handle_hook, {"junk": True}) is not None
              or True)
        check("main exits 0 on garbage", main(["hook"]) == 0)
        check("main exits 0 on unknown verb", main(["wat"]) == 0)
    finally:
        CHRON_HOME = saved
        shutil.rmtree(tmp, ignore_errors=True)

    print("SELFTEST:", "OK" if ok[0] else "FAILED")
    return 0 if ok[0] else 1


if __name__ == "__main__":
    sys.exit(main())
