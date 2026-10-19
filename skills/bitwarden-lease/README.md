# Bitwarden Lease

Bitwarden Lease lets local AI agents and terminal workflows reuse an unlocked
Bitwarden CLI session without copying `BW_SESSION` between shells, agent tasks,
or project files. It is an unofficial, local-only macOS broker with an
accompanying agent skill.

Use it when several authorized tasks need vault-backed credentials during a
working day and repeated unlock prompts interrupt the work. The broker keeps
the session in one place; each task asks it to run a narrow Bitwarden command
instead of handling the session key itself.

One native hidden-answer dialog unlocks Bitwarden for up to 24 hours while the
broker process survives. The session remains in that process and is supplied
only to allowlisted child `bw` commands. It is never returned by the protocol,
written to disk, added to shell profiles, or placed in a project `.env` file.

## Skill and runtime

[SKILL.md](SKILL.md) instructs the agent when to check status, request an unlock,
consume a secret, and diagnose failures safely. The Python broker, client, and
installer in [scripts](scripts) implement the actual lease. Installing skill
instructions alone does not start the broker.

The installer creates a per-user LaunchAgent and the `bw-lease` client. A native
hidden-answer dialog passes the owner's password to `bw unlock` through a
one-use pipe. The broker retains the resulting session in memory and supplies
it to allowed child `bw` processes. Clients receive command results, never the
session key.

This is credential leasing, not keyless authentication: a reusable vault session
exists for the lease duration, and retrieved secrets still require careful
handling. It is not a per-agent or per-vault-item permission system.

## Security model

- Per-user LaunchAgent; no privileged daemon.
- Owner-only runtime directory (`0700`) and Unix socket (`0600`).
- Only `bw get`, `bw list`, `bw sync`, and `bw status` are accepted.
- Caller-supplied `--session`, `--passwordfile`, and `--passwordenv` options are
  rejected, including `--option=value` forms.
- Bitwarden CLI unlock and child operations time out after 30 seconds; the
  human confirmation dialog itself waits for its owner.
- A monotonic 24-hour expiry clears the in-memory session even when idle.
- Logs contain no request bodies, command output, passwords, sessions, or vault
  objects.

The broker reduces accidental disclosure across terminals, logs, files, and
agent handoffs. It does **not** defend against another process already running
as the same macOS user. Read [the security contract](references/security-contract.md)
before changing the protocol or persistence model.

## Install

Install the agent instructions:

```bash
npx skills add AntreasAntoniou/bitwarden-lease
```

Requirements: macOS, the official `bw` CLI configured for your account, and an
absolute executable Python 3 path. Run these commands from this repository or
the installed skill directory:

```bash
python3 scripts/self_test.py
python3 scripts/install_bitwarden_lease_broker.py install \
  --python /opt/homebrew/bin/python3
```

Intel Homebrew commonly uses `/usr/local/bin/python3`. Installation restarts
the broker and therefore invalidates any existing in-memory lease. The client
is installed at `~/.local/bin/bw-lease`; use that path if it is not on your `PATH`.

## Use

```bash
bw-lease status             # never prompts
bw-lease unlock             # native secure dialog, at most three attempts
bw-lease bw sync
```

Only unlock for user-authorized credentialed work. `bw-lease status` reports
local lease state and remaining time without prompting; `bw-lease bw status`
is a brokered Bitwarden command and may prompt if locked. A running service or
an unexpired local lease does not prove a revoked Bitwarden session still works.

For retrieval, `bw-lease bw get password ITEM_ID` is the supported command
shape, not a safe transcript-producing example. Pipe secret-bearing output
directly into the smallest authorized one-shot consumer. Do not run it where
stdout will be captured in an agent transcript or CI log. The broker does not
redact the results returned to its caller.

Run the package checks without accessing a real vault:

```bash
python3 scripts/self_test.py
python3 scripts/validate_package.py
```

## Boundaries

The lease is lost on reboot, logout, broker restart or crash, explicit vault
lock, account revocation, or Bitwarden session invalidation. Avoiding a new
prompt across those events would require persistent reusable credentials and is
deliberately out of scope.

Bitwarden Lease is not affiliated with, endorsed by, or maintained by
Bitwarden, Inc. Bitwarden is a trademark of its respective owner.

Released under the [MIT License](LICENSE).
