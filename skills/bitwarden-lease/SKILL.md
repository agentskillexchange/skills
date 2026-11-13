---
name: "Bitwarden Lease"
slug: "bitwarden-lease"
description: "Install, operate, diagnose, and safely consume an owner-only macOS Bitwarden CLI lease that uses one native hidden-answer unlock interaction for a 24-hour process-continuity window. Use when repeated `bw unlock` prompts or agent handoffs disrupt work, when local agents need Bitwarden-backed credentials without persisting `BW_SESSION`, when checking whether the lease is usable, or when repairing the `io.github.antreasantoniou.bitwarden-lease` LaunchAgent. Bitwarden only; never substitute another credential store implicitly."
category: "Security & Verification"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/bitwarden-lease"
---

# Bitwarden Lease

Use one local macOS broker process to retain `BW_SESSION` in memory for 86,400
seconds. Present the human with a native secure dialog, allow three password
attempts, and share the lease across agent tasks through an owner-only Unix
socket. Never return the Bitwarden session itself.

## Resolve this skill

Set the directory containing this `SKILL.md` before invoking bundled scripts:

```bash
BITWARDEN_LEASE_SKILL="/absolute/path/to/bitwarden-lease"
```

Do not assume whether the active copy is under `~/.agents`, `~/.claude`, or
`~/.codex`; resolve the selected skill path from the available-skills catalog.

## Inspect without prompting

Run:

```bash
"$HOME/.local/bin/bw-lease" status
```

This operation must never open a dialog. Interpret only:

- `status=unlocked`: the broker holds a live lease; use `remaining_seconds`.
- `status=locked`: explicitly unlock before requesting a secret.
- missing socket/client: inspect or install the LaunchAgent.

Do not use `bw status` for this check: brokered `bw` operations intentionally
ensure a lease and may prompt.

## Install or repair

Requirements: macOS, Bitwarden CLI `bw`, and a stable absolute Python 3 path.
Prefer Homebrew Python outside a virtual environment when present.

Validate the package before installation:

```bash
python3 "$BITWARDEN_LEASE_SKILL/scripts/self_test.py"
python3 "$BITWARDEN_LEASE_SKILL/scripts/install_bitwarden_lease_broker.py" \
  install --python /opt/homebrew/bin/python3
```

On Intel Homebrew, use `/usr/local/bin/python3`; otherwise use a reviewed,
absolute, executable Python 3 path. The installer copies immutable runtime
files to `~/Library/Application Support/BitwardenLease`, writes an owner-only
LaunchAgent, installs `~/.local/bin/bw-lease`, and starts the service. Installing
or repairing restarts the broker and therefore discards any current lease.

After installation, verify all of these without unlocking:

```bash
launchctl print "gui/$(id -u)/io.github.antreasantoniou.bitwarden-lease"
ls -l "$HOME/Library/Caches/bitwarden-lease/broker.sock"
"$HOME/.local/bin/bw-lease" status
```

Require a running service and a socket mode no broader than `0600`. Never
claim a usable lease merely because the process exists.

## Unlock once

Only trigger unlock when the user asked for credentialed work or an imminent
authorized operation requires it:

```bash
"$HOME/.local/bin/bw-lease" unlock
```

The native dialog is the only password-entry surface. It permits three
attempts. Do not ask the user to type into an agent terminal, do not accept the
password in chat, and do not pass it in argv, files, shell history, clipboard
automation, or environment variables.

After success, call `status` again. Report lease state and approximate remaining
time only. Never report vault identity metadata unless the task explicitly
requires a public identity verification.

## Consume a secret without exposing it

The client supports allowlisted `bw get`, `bw list`, `bw sync`, and `bw status`
operations:

```bash
"$HOME/.local/bin/bw-lease" bw get password ITEM_ID
```

Secret-bearing output is sensitive. Never run such a command directly when its
stdout will enter a tool transcript. Route output directly into the smallest
authorized one-shot consumer, suppress diagnostics that might echo it, unset
derived environment values immediately, and verify only non-secret public
identity or operation receipts. Do not write `.env` files, shell profiles,
LaunchAgent variables, Keychain entries, GCS objects, CI outputs, logs, or
evidence records containing the secret.

Each brokered Bitwarden CLI operation is bounded to 30 seconds. A timeout
returns exit code 75 with no stdout, so one stalled `bw` child cannot serialize
all later clients behind it or expose partial secret output. Treat a timeout as
a transient broker/CLI failure; diagnose the child process and retry once after
it is absent. Do not restart a healthy broker merely to retry, because restart
discards the in-memory lease.

The broker rejects `--session`, `--passwordfile`, and `--passwordenv` supplied
by callers. It has no operation that returns its in-memory session key.

## Honor the availability boundary

The guarantee is one prompt per 24 hours while the broker process survives.
A reboot, logout, broker crash/restart, explicit vault lock, account revocation,
or Bitwarden session invalidation requires a fresh prompt. Never claim
prompt-free survival across those events: that would require persisting a
reusable decrypted credential.

If a brokered operation reports the session invalid before lease expiry, treat
the lease as unusable and request a fresh explicit unlock. Do not silently fall
back to ambient `BW_SESSION`, raw `bw unlock`, 1Password, service-account keys,
or credentials found in project files.

## Diagnose safely

Read only process state, permissions, and secret-free logs:

```bash
launchctl print "gui/$(id -u)/io.github.antreasantoniou.bitwarden-lease"
tail -100 "$HOME/Library/Caches/bitwarden-lease/broker.stderr.log"
```

The logs must remain empty of passwords, sessions, vault objects, and secret
command output. Read [references/security-contract.md](references/security-contract.md)
before changing the protocol, lifetime, persistence model, permissions, or
allowed Bitwarden commands.

## Close the loop

For changes to this skill or broker:

1. Run `scripts/self_test.py` and the skill validator.
2. Verify installed/reviewed script hashes if installation changed.
3. Check `launchctl` state and non-prompting lease status.
4. Record only the custody decision, lease state, and non-secret receipts.
5. Publish only source, tests, and non-secret receipts. Never publish runtime
   state, socket contents, vault identifiers, or retrieved values.

## Installation and upstream provenance

The upstream skill identifier is `bitwarden-lease`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/bitwarden-lease --skill bitwarden-lease --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/bitwarden-lease#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`813b98b13399`](https://github.com/AntreasAntoniou/bitwarden-lease/tree/813b98b13399d66f550a97a97ef809992019f864). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
