"""Wiring capture into a machine.

The hard requirement here is ADDITIVE INSTALLATION. Existing hooks may belong to
independent systems. Rewriting the file wholesale would silently break them.

So: read, merge by identity, write via a temp file, keep a timestamped backup, and be
idempotent. Running install twice must be indistinguishable from running it once.
"""
from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import capture as cap  # noqa: E402

MARKER = "chronicle/bin/capture.py"          # how we recognise our own hook entries

# Events we capture, and why each one is worth a process spawn.
HOOK_EVENTS = {
    "SessionStart":     "session boundaries — the anchor for `since you were last here`",
    "SessionEnd":       "the same, and the trigger for the narrator",
    "Stop":             "end of an assistant turn — narrator trigger",
    "SubagentStop":     "a subagent finished; its work belongs to the same story",
    "UserPromptSubmit": "what was actually asked, in the human's words",
    "PreToolUse":       "the BEFORE snapshot, and the destructive-operation gate",
    "PostToolUse":      "the AFTER snapshot, the command, and its output",
}

ZSH_HOOK = r'''
# ── chronicle capture ────────────────────────────────────────────────────────
# Records every interactive command (command, cwd, exit code, duration) into the
# work ledger. Base64 avoids every quoting hazard in passing a command line along.
# Never blocks: the capture call is backgrounded and its output discarded.
_chronicle_preexec() {
  _CHRON_CMD="$1"
  _CHRON_T0=$EPOCHREALTIME
}
_chronicle_precmd() {
  local ec=$?
  [[ -z "$_CHRON_CMD" ]] && return
  local ms=0
  if [[ -n "$_CHRON_T0" ]]; then
    ms=$(( (${EPOCHREALTIME/./} - ${_CHRON_T0/./}) / 1000 ))
  fi
  local b64
  b64=$(printf '%s' "$_CHRON_CMD" | base64 | tr -d '\n')
  ( python3 "$HOME/.chronicle/bin/capture.py" shell \
      --cmd "$b64" --exit "$ec" --ms "$ms" --cwd "$PWD" \
      --session "tty-$$" >/dev/null 2>&1 & ) 2>/dev/null
  unset _CHRON_CMD _CHRON_T0
}
autoload -Uz add-zsh-hook 2>/dev/null && {
  add-zsh-hook preexec _chronicle_preexec
  add-zsh-hook precmd  _chronicle_precmd
}
# ── end chronicle capture ────────────────────────────────────────────────────
'''

BASH_HOOK = r'''
# ── chronicle capture ────────────────────────────────────────────────────────
# bash equivalent of the zsh hook. some hosts run bash, not zsh, so a zsh-only capture
# layer would silently record nothing on the machine that does the heaviest work.
# The DEBUG trap fires for every command in a compound statement, so a latch ensures
# one record per prompt rather than one per sub-command.
_chronicle_preexec() {
  [ -n "$COMP_LINE" ] && return
  [ "$_CHRON_LATCH" = "1" ] && return
  _CHRON_LATCH=1
  _CHRON_CMD="$BASH_COMMAND"
  _CHRON_T0=$(date +%s)
}
_chronicle_precmd() {
  local ec=$?
  if [ -n "$_CHRON_CMD" ]; then
    local ms=0
    if [ -n "$_CHRON_T0" ]; then ms=$(( ($(date +%s) - _CHRON_T0) * 1000 )); fi
    local b64
    b64=$(printf '%s' "$_CHRON_CMD" | base64 | tr -d '\n')
    ( python3 "$HOME/.chronicle/bin/capture.py" shell \
        --cmd "$b64" --exit "$ec" --ms "$ms" --cwd "$PWD" \
        --session "tty-$$" >/dev/null 2>&1 & ) 2>/dev/null
  fi
  unset _CHRON_CMD _CHRON_T0
  _CHRON_LATCH=0
}
trap '_chronicle_preexec' DEBUG
PROMPT_COMMAND="_chronicle_precmd;${PROMPT_COMMAND}"
# ── end chronicle capture ────────────────────────────────────────────────────
'''

GIT_HOOK = r'''#!/bin/sh
# chronicle: record this commit into the work ledger. Never blocks or fails the commit.
PHASE="$(basename "$0")"
SUBJECT="$(git log -1 --pretty=%s 2>/dev/null)"
FILES="$(git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null)"
python3 "$HOME/.chronicle/bin/capture.py" git \
  --phase "$PHASE" --cwd "$PWD" --subject "$SUBJECT" --files "$FILES" >/dev/null 2>&1 || true
exit 0
'''


def bin_dir() -> Path:
    return Path(cap.CHRON_HOME) / "bin"


def deployed_capture() -> Path:
    return bin_dir() / "capture.py"


def hook_command(harness: str = "claude-code") -> str:
    """Return the stable capture command with an explicit harness identity.

    Claude Code and Codex use closely related hook payloads, and neither contract
    guarantees a ``harness`` field.  Put the identity in the command environment so
    capture never has to infer which harness invoked it.
    """
    if harness not in {"claude-code", "codex"}:
        raise ValueError(f"unsupported hook harness: {harness}")
    return f'CHRONICLE_HARNESS={harness} python3 "$HOME/.chronicle/bin/capture.py" hook'


def deploy_capture(dry_run: bool = False) -> Path:
    """Copy the capture core to its stable, harness-independent location.

    Hooks point at ~/.chronicle/bin/capture.py rather than at the repo, so that moving,
    renaming, or rebasing the repo cannot decapitate capture on a running machine.
    """
    dest = deployed_capture()
    src = Path(__file__).parent / "capture.py"
    if dry_run:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    dest.chmod(0o755)
    return dest


# ── Claude Code settings.json ────────────────────────────────────────────────

def _settings_path() -> Path:
    return Path.home() / ".claude" / "settings.json"


def merge_hooks(settings: dict, matcher: bool = True,
                harness: str = "claude-code") -> tuple[dict, list[str]]:
    """Add or upgrade our hook entries in place. Returns (settings, changed events).

    `matcher=False` is used for Codex. A matcher of "*" means match-everything, which is
    identical to having none — but whether the matcher forms part of Codex's trust
    identity varies by event, and for `stop`/`user_prompt_submit` no pre-existing record
    carries one, so it cannot be determined from the data. Omitting it makes the
    fingerprint unambiguous rather than a coin-flip.
    """
    hooks = settings.setdefault("hooks", {})
    changed = []
    command = hook_command(harness)
    for event in HOOK_EVENTS:
        existing = hooks.setdefault(event, [])
        if not isinstance(existing, list):
            continue
        found = False
        upgraded = False
        for entry in existing:
            if not isinstance(entry, dict):
                continue
            for hook in entry.get("hooks", []) or []:
                if not isinstance(hook, dict) or MARKER not in json.dumps(hook):
                    continue
                found = True
                if hook.get("command") != command:
                    hook["command"] = command
                    upgraded = True
        if found:
            if upgraded:
                changed.append(event)
            continue
        entry = {"hooks": [{"type": "command", "command": command, "timeout": 5}]}
        if matcher:
            entry = {"matcher": "*", **entry}
        existing.append(entry)
        changed.append(event)
    return settings, changed


def install_claude_hooks(dry_run: bool = False) -> list[str]:
    path = _settings_path()
    try:
        settings = json.loads(path.read_text()) if path.exists() else {}
    except json.JSONDecodeError as exc:
        raise SystemExit(f"REFUSED: {path} is not valid JSON ({exc}). "
                         "Fix it before installing — overwriting it would lose your hooks.")

    before = json.dumps(settings, sort_keys=True)
    settings, added = merge_hooks(settings)
    if not added:
        return []
    if dry_run:
        return added

    # Backup first. Editing the file that wires five other systems is exactly the class of
    # operation chronicle itself insists on having a restore path for.
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = path.with_suffix(f".json.chronicle-backup-{stamp}")
    if path.exists():
        shutil.copy2(path, backup)

    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(settings, indent=2) + "\n")
    os.replace(tmp, path)

    # Prove we did not destroy anything: every pre-existing NON-CHRONICLE command must
    # still be there. Chronicle's legacy command is intentionally upgraded in place.
    # Compared STRUCTURALLY — an earlier version of this check tested for the command as a
    # substring of a json.dumps() blob, which false-positived on any command containing a
    # quote (escaping turns `"$HOME/x"` into `\"$HOME/x\"`). A safety check that misfires
    # on quoted input is a safety check that will be disabled.
    after = json.loads(path.read_text())
    for event, entries in json.loads(before).get("hooks", {}).items():
        if not isinstance(entries, list):
            continue
        kept = _commands_for(after, event)
        for entry in entries:
            for h in (entry or {}).get("hooks", []) or []:
                cmd = h.get("command", "")
                if cmd and MARKER not in cmd and cmd not in kept:
                    shutil.copy2(backup, path)
                    raise SystemExit(
                        f"ABORTED: merging would have dropped an existing {event} hook "
                        f"({cmd[:60]}…). Restored from {backup}.")
    return added


def _commands_for(settings: dict, event: str) -> set:
    """Exact command strings registered for one hook event."""
    out = set()
    for entry in (settings.get("hooks") or {}).get(event, []) or []:
        if not isinstance(entry, dict):
            continue
        for h in entry.get("hooks", []) or []:
            cmd = h.get("command")
            if cmd:
                out.add(cmd)
    return out


# ── Codex ────────────────────────────────────────────────────────────────────

def _codex_hooks_path() -> Path:
    return Path.home() / ".codex" / "hooks.json"


def _codex_config_path() -> Path:
    return Path.home() / ".codex" / "config.toml"


def codex_trust(dry_run: bool = False) -> dict:
    """Compatibility stub: hook trust belongs to the operator's interactive approval."""
    return {"error": "Use the host's interactive hook approval after reviewing the command; "
                     "Chronicle does not grant or renew hook trust."}


def install_codex_hooks(dry_run: bool = False) -> list[str]:
    """Stage experimental Codex hooks without granting trust.

    Config schema, event support, and payload compatibility vary by host version.
    Review a dry run and prove capture with an actual host event before relying on it.
    This function never modifies config.toml or approves hook commands.
    """
    path = _codex_hooks_path()
    if not path.parent.exists():
        return []
    try:
        doc = json.loads(path.read_text()) if path.exists() else {}
    except json.JSONDecodeError as exc:
        raise SystemExit(f"REFUSED: {path} is not valid JSON ({exc}). "
                         "Fix it before installing — overwriting it would lose your hooks.")

    before = {cmd for cmd in _all_commands(doc) if MARKER not in cmd}
    merged, added = merge_hooks(doc, matcher=False, harness="codex")
    if not added:
        return []
    lost = before - _all_commands(merged)
    if lost:
        raise SystemExit(f"ABORTED: merging would drop existing Codex hooks: {lost}")
    if dry_run:
        return added

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    if path.exists():
        shutil.copy2(path, path.with_name(f"hooks.json.chronicle-backup-{stamp}"))
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(merged, indent=2) + "\n")
    os.replace(tmp, path)
    return added


# ── shell ────────────────────────────────────────────────────────────────────

def install_shell_hook(dry_run: bool = False) -> bool:
    zshrc = Path.home() / ".zshrc"
    body = zshrc.read_text() if zshrc.exists() else ""
    if "chronicle capture" in body:
        return False
    if dry_run:
        return True
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    if zshrc.exists():
        shutil.copy2(zshrc, zshrc.with_name(f".zshrc.chronicle-backup-{stamp}"))
    with zshrc.open("a") as fh:
        fh.write("\n" + ZSH_HOOK)
    return True


# ── git ──────────────────────────────────────────────────────────────────────

def install_git_hooks(repos: list[str], dry_run: bool = False) -> list[str]:
    """Install post-commit/merge/checkout in each repo. Never clobbers an existing hook —
    a repo with its own post-commit keeps it, and we report the conflict instead."""
    done = []
    for repo in repos:
        gitdir = Path(repo) / ".git"
        if not gitdir.is_dir():
            continue
        hookdir = gitdir / "hooks"
        for name in ("post-commit", "post-merge", "post-checkout"):
            target = hookdir / name
            if target.exists():
                text = target.read_text(errors="replace")
                if "chronicle" in text:
                    continue
                done.append(f"SKIPPED {repo}/{name} (already has a hook)")
                continue
            if dry_run:
                done.append(f"would install {repo}/{name}")
                continue
            hookdir.mkdir(parents=True, exist_ok=True)
            target.write_text(GIT_HOOK)
            target.chmod(0o755)
            done.append(f"{repo}/{name}")
    return done


# ── remote ───────────────────────────────────────────────────────────────────

def install_remote(host: str, dry_run: bool = False, shell: bool = False,
                   claude: bool = False) -> int:
    """Push capture to another machine over ssh and verify it actually runs there.

    Verification is not optional: a remote may run a different Python version, and 'it copied fine'
    says nothing about whether it executes. The selftest is the proof.
    """
    src = Path(__file__).parent / "capture.py"
    if dry_run:
        print(f"would scp {src} → {host}:~/.chronicle/bin/capture.py and run its selftest")
        return 0

    # An unreachable host is reported as skipped.
    probe = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", host, "true"],
        capture_output=True, text=True)
    if probe.returncode != 0:
        detail = (probe.stderr or "").strip().splitlines()
        why = detail[-1][:80] if detail else "no route"
        print(f"{host}: SKIPPED — unreachable ({why})")
        return 0

    try:
        subprocess.run(["ssh", "-o", "ConnectTimeout=8", host, "mkdir -p ~/.chronicle/bin"],
                       check=True, capture_output=True, timeout=30)
        subprocess.run(["scp", "-o", "ConnectTimeout=8", "-q", str(src),
                        f"{host}:~/.chronicle/bin/capture.py"],
                       check=True, capture_output=True, timeout=60)
        proc = subprocess.run(
            ["ssh", "-o", "ConnectTimeout=8", host,
             "python3 --version && python3 ~/.chronicle/bin/capture.py selftest"],
            capture_output=True, text=True, timeout=120)
    except (subprocess.SubprocessError, OSError) as exc:
        print(f"{host}: FAILED — {type(exc).__name__}: {str(exc)[:120]}", file=sys.stderr)
        return 1

    version = proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else "?"
    if proc.returncode != 0 or "SELFTEST: OK" not in proc.stdout:
        print(f"{host}: capture does NOT run correctly ({version})", file=sys.stderr)
        print(proc.stdout[-600:], file=sys.stderr)
        print(proc.stderr[-600:], file=sys.stderr)
        return 1
    # Report the interpreter: the whole reason capture is 3.9-safe is that this fleet is
    # not homogeneous, and seeing the version confirms the constraint is still real.
    print(f"{host}: capture verified on {version}")

    if shell:
        install_remote_shell(host)
    if claude:
        install_remote_claude(host)
    return 0


def install_remote_shell(host: str) -> bool:
    """Append the right shell hook for whatever shell the host actually runs.

    The command is sent base64-encoded on a SINGLE line. An earlier version piped a
    heredoc through ssh, which hung for two minutes waiting on stdin and installed
    nothing — remote installs must never depend on interactive stream behaviour.
    """
    probe = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", host,
         "command -v zsh >/dev/null && echo zsh || echo bash"],
        capture_output=True, text=True, timeout=30)
    shell_kind = (probe.stdout or "bash").strip().splitlines()[-1] if probe.stdout else "bash"
    hook, rc_file = (ZSH_HOOK, "~/.zshrc") if shell_kind == "zsh" else (BASH_HOOK, "~/.bashrc")

    payload = base64.b64encode(hook.encode("utf-8")).decode("ascii")
    script = (
        f'RC=$(eval echo {rc_file}); touch "$RC"; '
        'if grep -q "chronicle capture" "$RC" 2>/dev/null; then echo ALREADY; exit 0; fi; '
        'cp "$RC" "$RC.chronicle-backup-$(date -u +%Y%m%dT%H%M%SZ)" 2>/dev/null; '
        f'echo {payload} | base64 -d >> "$RC" && echo INSTALLED'
    )
    try:
        out = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", host, script],
            capture_output=True, text=True, timeout=45)
    except subprocess.SubprocessError as exc:
        print(f"{host}: shell hook FAILED — {exc}", file=sys.stderr)
        return False
    if "INSTALLED" in out.stdout:
        print(f"{host}: {shell_kind} hook installed in {rc_file} (active in new shells)")
        return True
    if "ALREADY" in out.stdout:
        print(f"{host}: {shell_kind} hook already present")
        return True
    print(f"{host}: shell hook FAILED — {(out.stderr or out.stdout)[-200:]}", file=sys.stderr)
    return False


def install_remote_claude(host: str) -> bool:
    """Merge chronicle's hooks into a remote Claude Code settings.json.

    The merge runs LOCALLY on a fetched copy, using the same merge_hooks() that is tested
    against this machine's real settings file. Reimplementing the merge in a remote shell
    one-liner would mean the dangerous path is the untested one.
    """
    import tempfile as _tf
    with _tf.TemporaryDirectory() as td:
        local = Path(td) / "settings.json"
        got = subprocess.run(
            ["scp", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-q",
             f"{host}:.claude/settings.json", str(local)],
            capture_output=True, text=True, timeout=45)
        if got.returncode != 0 or not local.exists():
            settings = {}
        else:
            try:
                settings = json.loads(local.read_text())
            except json.JSONDecodeError:
                print(f"{host}: remote settings.json is not valid JSON — skipped",
                      file=sys.stderr)
                return False

        before = _all_commands(settings)
        merged, added = merge_hooks(settings)
        if not added:
            print(f"{host}: claude hooks already installed")
            return True
        lost = before - _all_commands(merged)
        if lost:
            print(f"{host}: ABORTED — merge would drop {lost}", file=sys.stderr)
            return False

        local.write_text(json.dumps(merged, indent=2) + "\n")
        subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", host,
             'mkdir -p ~/.claude && '
             '[ -f ~/.claude/settings.json ] && '
             'cp ~/.claude/settings.json '
             '~/.claude/settings.json.chronicle-backup-$(date -u +%Y%m%dT%H%M%SZ); true'],
            capture_output=True, timeout=30)
        put = subprocess.run(
            ["scp", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-q", str(local),
             f"{host}:.claude/settings.json"], capture_output=True, text=True, timeout=45)
        if put.returncode != 0:
            print(f"{host}: claude hooks FAILED — {put.stderr[-200:]}", file=sys.stderr)
            return False
        print(f"{host}: claude hooks added ({len(added)} events)")
        return True


def _all_commands(settings: dict) -> set:
    out = set()
    for event in (settings.get("hooks") or {}):
        out |= _commands_for(settings, event)
    return out


# ── command ──────────────────────────────────────────────────────────────────

def cmd_install_hooks(args) -> int:
    if getattr(args, "trust_codex", False):
        print(codex_trust()["error"])
        return 2

    if getattr(args, "machine", None):
        return install_remote(args.machine, args.dry_run,
                              shell=getattr(args, 'shell', False),
                              claude=getattr(args, 'claude', False))

    dest = deploy_capture(args.dry_run)
    print(f"capture core → {dest}")

    added = install_claude_hooks(args.dry_run)
    if added:
        verb = "would add" if args.dry_run else "added"
        print(f"claude code hooks {verb}: {', '.join(added)}")
    else:
        print("claude code hooks: already installed")

    if getattr(args, "shell", False):
        if install_shell_hook(args.dry_run):
            print("zsh hook appended to ~/.zshrc "
                  "(open a new shell, or `source ~/.zshrc`, to activate)")
        else:
            print("zsh hook: already installed")

    if getattr(args, "codex", False):
        codex_added = install_codex_hooks(args.dry_run)
        if codex_added:
            verb = "would add" if args.dry_run else "added"
            print(f"codex hooks {verb}: {', '.join(codex_added)}")
            if not args.dry_run:
                print("  Experimental: review and approve hooks interactively in your host.")
                print("  Verify a real event before relying on capture or gate coverage.")
        else:
            print("codex hooks: already installed (or ~/.codex absent)")

    if getattr(args, "git", False):
        sys.path.insert(0, str(Path(__file__).parent))
        import index as idx
        repos = idx.registered_roots()
        results = install_git_hooks(repos, args.dry_run)
        print(f"git hooks: {len(results)} action(s) across {len(repos)} repo(s)")
        for r in results[:20]:
            print(f"  {r}")

    if not args.dry_run:
        cap.emit({
            "kind": "note",
            "summary": "chronicle capture installed on %s" % cap.machine(),
            "actor": {"kind": "human", "harness": "cli", "session": "install"},
            "installed": added,
        }, os.getcwd(), "install")
    print()
    print("verify with: chron doctor")
    return 0
