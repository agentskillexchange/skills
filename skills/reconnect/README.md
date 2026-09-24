# Reconnect

Find people you would like to talk to. Keep track of why, and pick up where you left off.

Reconnect is an agent skill for building a professional network: meeting peers,
finding collaborators or mentors, following up after events, and reconnecting with
former colleagues. Start with a goal, a field, a project, or a list of names.

It helps your agent research relevant people, explain the evidence behind each
match, prepare a shortlist, and track connection requests across sessions. You
choose whom to contact and for what purpose. The skill carries that context forward.

**Release candidate: 0.1.0-rc.2 · MIT · Python 3.10+ for the optional local helper**

## What using it looks like

> Use reconnect to find researchers working on accessible robotics. Start with a
> shortlist and explain what makes each person's work relevant to mine.

> Use reconnect to find the public profiles of people I met at the conference.
> Distinguish people I actually spoke to from others on the programme.

> Use reconnect to review my existing queue. I sent some invitations myself;
> reconcile those before preparing another batch.

The shortlist includes a profile, a reason to connect, supporting sources, known
relationship context, and uncertainty. A high match score does not establish that
someone is the right person—or that they fit your goal.

## What is included

| Part | What it does |
| --- | --- |
| Agent instructions | Guide discovery, identity review, invitation preparation, and resumption |
| Browser workflow | Guide the agent through explicitly authorised LinkedIn actions using tools available in its host |
| Local Python helper | Store evidence, deduplicate profiles, reserve batches, and record observations in SQLite |
| Fictional examples and tests | Let you try the local workflow without contacting anyone |

The helper makes no network calls, sends no invitations, and needs no API key. Web
research and browser control depend on tools supplied by your agent application.
LinkedIn currently supplies the destination format used by the ledger. Other
platforms and CRM writebacks require separate integrations.

## Install

From an extracted release directory or a local checkout:

```sh
# Shared skill directory; use with agents that discover this location.
python3 scripts/install.py --target "$HOME/.agents/skills/reconnect"

# Alternatively, install directly for Codex:
python3 scripts/install.py --target "$HOME/.codex/skills/reconnect"

# Or for Claude Code:
python3 scripts/install.py --target "$HOME/.claude/skills/reconnect"
```

Choose the location your application loads. The installer copies only skill
instructions, references, metadata, the helper, and the licence. It refuses to
overwrite an existing installation. Restart or refresh your agent session if it
does not discover the new skill immediately.

Invoke `$reconnect` where skill invocation is supported, or ask the agent to read
the installed `SKILL.md`. The instructions are tool-neutral; browser capabilities
and permissions vary between applications. Installation does not add browser tools
or grant access to an account.

## Try the local workflow

These examples are fictional. Do not visit or contact their profile URLs.
Run from the package directory:

```sh
mkdir -p "$HOME/reconnect-demo"
python3 scripts/reconnect.py --db "$HOME/reconnect-demo/ledger.sqlite3" import --input examples/candidates.json
python3 scripts/reconnect.py --db "$HOME/reconnect-demo/ledger.sqlite3" prepare --batch demo-001 --size 2
python3 scripts/reconnect.py --db "$HOME/reconnect-demo/ledger.sqlite3" batch --batch demo-001
python3 scripts/reconnect.py --db "$HOME/reconnect-demo/ledger.sqlite3" status
```

Preparing the same batch again returns its existing members. Preparing a new batch
excludes destinations already reserved. Records marked requested, connected, held,
or excluded do not enter a new ordinary review batch. See
[tracking commands and input format](references/tracking.md) for recording
observations, preserving an existing list, and releasing reservations.

An `authorize` record stores a reference to actual user approval; it is not an
access-control mechanism. An `observe` record stores supplied evidence; the helper
cannot independently verify what happened in a browser. Live readback and accurate
reconciliation remain the agent's responsibility.

## Private by default

Keep each network project outside the skill directory. Store only the professional
context and evidence you need, respect source permissions and exclusions, and keep
private exports out of Git. New ledgers request owner-only filesystem permissions;
they are **not encrypted**, and filesystem protections depend on your OS. No
telemetry or hosted service is included.

The ledger tracks one campaign's relationship and optional group state. Use separate
project ledgers for separate groups or accounts. Existing CRM or community databases
can stay authoritative, with project-local adapters translating to the generic
candidate format.

## Scope and limitations

- Identity matches and professional relevance need review; discovery cannot guarantee completeness.
- Sending requires explicit user authorisation and supported browser tools. The skill does not supply LinkedIn API access or exemption from platform rules.
- Stop on platform warnings, restrictions, invitation limits, or verification challenges. There is no promised safe sending rate or bot-evasion mode.
- Acceptance of a connection is not permission for an unrelated messaging campaign.
- Local tests cover the ledger and packaging. Automated browser compatibility has not been certified across agent hosts or LinkedIn interface versions.

## Development and packaging

No third-party Python packages are required for the helper or tests.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/release.py --output-dir dist
```

Packaging includes only explicitly listed files, verifies their expected text
formats, and rejects common private-data and credential markers. The ZIP contains
a per-file SHA-256 manifest; a separate checksum covers the ZIP. This scan is a
useful check, not a guarantee that arbitrary text is suitable for publication.

See [release notes](docs/release-notes.md). Contributions should include minimal,
fictional examples and tests; do not submit contact databases or account details.

## Licence

MIT. Copyright 2026 Antreas Antoniou. See [LICENSE](LICENSE).
Reconnect is an independent project and is not affiliated with LinkedIn.
