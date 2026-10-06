"""Installation must be additive.

Existing settings can contain unrelated integrations. Test that merges preserve every
non-Chronicle command, including quoted commands and Unicode.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src" / "chronicle"))
import install as ins  # noqa: E402

REAL_SETTINGS = Path.home() / ".claude" / "settings.json"


def _commands(settings: dict) -> set[str]:
    """Every hook command string present, regardless of nesting."""
    out = set()
    for entries in (settings.get("hooks") or {}).values():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            for h in (entry or {}).get("hooks", []) or []:
                cmd = h.get("command")
                if cmd:
                    out.add(cmd)
    return out


@pytest.mark.skipif(not REAL_SETTINGS.exists(), reason="no real settings.json here")
def test_merge_preserves_every_existing_command():
    original = json.loads(REAL_SETTINGS.read_text())
    before = _commands(original)
    assert before, "fixture is meaningless if there were no hooks to begin with"

    desired = ins.hook_command("claude-code")
    already_current = desired in before
    merged, added = ins.merge_hooks(json.loads(json.dumps(original)))
    after = _commands(merged)

    lost = {cmd for cmd in before - after if ins.MARKER not in cmd}
    assert not lost, f"merge dropped existing hook commands: {lost}"
    assert any(ins.MARKER in cmd for cmd in after), "chronicle hook is not present after merge"
    # The test must pass both before and after chronicle is installed on this machine —
    # otherwise it silently becomes a no-op the moment the tool starts being used, which
    # is the point at which its guarantee actually matters.
    if already_current:
        assert added == [], "re-merging an installed machine added duplicates"
        assert len(after) == len(before), "re-merge changed the command set"
    else:
        assert added, "nothing was added on a fresh machine"
        expected = len(before) if any(ins.MARKER in cmd for cmd in before) else len(before) + 1
        assert len(after) == expected, "expected one in-place upgrade or one new command"


@pytest.mark.skipif(not REAL_SETTINGS.exists(), reason="no real settings.json here")
def test_merge_preserves_non_hook_settings():
    original = json.loads(REAL_SETTINGS.read_text())
    merged, _ = ins.merge_hooks(json.loads(json.dumps(original)))
    for key, value in original.items():
        if key == "hooks":
            continue
        assert merged[key] == value, f"install mutated unrelated setting {key!r}"


def test_merge_is_idempotent():
    settings = {"hooks": {"PostToolUse": [
        {"matcher": "*", "hooks": [{"type": "command", "command": "curl other-system"}]}]}}
    once, added1 = ins.merge_hooks(json.loads(json.dumps(settings)))
    twice, added2 = ins.merge_hooks(json.loads(json.dumps(once)))
    assert added2 == [], "second install added duplicate entries"
    assert json.dumps(once, sort_keys=True) == json.dumps(twice, sort_keys=True)


def test_merge_upgrades_legacy_hook_in_place_without_duplication():
    legacy = 'python3 "$HOME/.chronicle/bin/capture.py" hook'
    settings = {"hooks": {event: [{"matcher": "*", "hooks": [
        {"type": "command", "command": legacy, "timeout": 5}
    ]}] for event in ins.HOOK_EVENTS}}

    merged, changed = ins.merge_hooks(settings, harness="claude-code")

    assert set(changed) == set(ins.HOOK_EVENTS)
    for event, entries in merged["hooks"].items():
        commands = [hook["command"] for entry in entries for hook in entry["hooks"]]
        assert commands == [ins.hook_command("claude-code")], event


def test_codex_and_claude_commands_declare_distinct_harnesses():
    assert "CHRONICLE_HARNESS=claude-code" in ins.hook_command("claude-code")
    assert "CHRONICLE_HARNESS=codex" in ins.hook_command("codex")
    assert ins.hook_command("claude-code") != ins.hook_command("codex")


def test_codex_trust_refuses_without_mutating_config(tmp_path, monkeypatch):
    config = tmp_path / "config.toml"
    config.write_text('model = "chosen-by-user"\n')
    monkeypatch.setattr(ins, "_codex_config_path", lambda: config)
    before = config.read_bytes()
    result = ins.codex_trust(dry_run=False)
    assert "interactive" in result["error"]
    assert config.read_bytes() == before


def test_codex_install_preserves_config_and_existing_hooks(tmp_path, monkeypatch):
    hooks = tmp_path / "hooks.json"
    config = tmp_path / "config.toml"
    config.write_text('model = "chosen-by-user"\n')
    hooks.write_text(json.dumps({"hooks": {"Stop": [{"hooks": [
        {"type": "command", "command": "keep-me"}]}]}}))
    monkeypatch.setattr(ins, "_codex_hooks_path", lambda: hooks)
    before = config.read_bytes()
    assert ins.install_codex_hooks(dry_run=False)
    assert "keep-me" in _commands(json.loads(hooks.read_text()))
    assert config.read_bytes() == before


def test_merge_into_empty_settings():
    merged, added = ins.merge_hooks({})
    assert set(added) == set(ins.HOOK_EVENTS)
    assert len(_commands(merged)) == 1


def test_merge_tolerates_malformed_event_lists():
    """A hand-edited settings.json may hold a dict where a list belongs. Skip it rather
    than crash — refusing to install because of someone else's typo helps nobody."""
    settings = {"hooks": {"PostToolUse": {"not": "a list"},
                          "Stop": [{"hooks": [{"command": "keep-me"}]}]}}
    merged, added = ins.merge_hooks(settings)
    assert "keep-me" in _commands(merged)
    assert "PostToolUse" not in added


def test_verification_handles_quoted_commands(tmp_path, monkeypatch):
    """Regression: the post-merge verifier once compared a raw command string against a
    json.dumps() blob, so any command containing a quote — like

        "$HOME/.claude/hooks/example-notify.sh" notification

    — appeared to have been dropped (escaping turns `"` into `\\"`) and the install
    aborted on a perfectly correct merge. Verification must be structural.
    """
    settings = tmp_path / "settings.json"
    quoted = '"$HOME/.claude/hooks/example-notify.sh" notification'
    unicode_cmd = "echo 'ünïcode → 日本語'"
    settings.write_text(json.dumps({
        "hooks": {
            "Notification": [{"hooks": [{"type": "command", "command": quoted}]}],
            "Stop": [{"matcher": "*", "hooks": [{"type": "command", "command": unicode_cmd}]}],
        },
        "model": "opus",
    }, indent=2))
    monkeypatch.setattr(ins, "_settings_path", lambda: settings)

    added = ins.install_claude_hooks(dry_run=False)
    assert added, "install did not run"

    result = json.loads(settings.read_text())
    cmds = _commands(result)
    assert quoted in cmds, "quoted command was lost or falsely reported as lost"
    assert unicode_cmd in cmds, "unicode command was lost"
    assert result["model"] == "opus"
    assert any(ins.MARKER in c for c in cmds), "chronicle hook was not added"


def test_verification_actually_catches_a_real_drop(tmp_path, monkeypatch):
    """The verifier must still fire when a hook genuinely disappears — otherwise the
    previous test could pass by having disabled the check entirely."""
    settings = tmp_path / "settings.json"
    settings.write_text(json.dumps({
        "hooks": {"Stop": [{"hooks": [{"type": "command", "command": "precious"}]}]}}))
    monkeypatch.setattr(ins, "_settings_path", lambda: settings)

    def destructive(s):
        s["hooks"]["Stop"] = []          # simulate a merge bug that eats an entry
        return s, ["Stop"]

    monkeypatch.setattr(ins, "merge_hooks", destructive)
    with pytest.raises(SystemExit) as exc:
        ins.install_claude_hooks(dry_run=False)
    assert "would have dropped" in str(exc.value)
    assert "precious" in _commands(json.loads(settings.read_text())), \
        "verifier aborted but did not restore the backup"


def test_hook_command_points_at_stable_location():
    """Hooks must not point into the repo: moving or rebasing the repo would otherwise
    decapitate capture on a running machine."""
    cmd = ins.hook_command()
    assert "$HOME/.chronicle/bin/capture.py" in cmd
    assert str(REPO) not in cmd
    assert ins.MARKER in cmd


def test_git_hook_never_fails_a_commit():
    """A capture bug must not be able to block a commit."""
    assert "|| true" in ins.GIT_HOOK
    assert ins.GIT_HOOK.strip().endswith("exit 0")


def test_zsh_hook_is_non_blocking():
    """The shell hook runs on every prompt. It must background its work and swallow output."""
    assert "&" in ins.ZSH_HOOK
    assert ">/dev/null 2>&1" in ins.ZSH_HOOK
    assert "base64" in ins.ZSH_HOOK, "command must be base64'd to survive quoting"
