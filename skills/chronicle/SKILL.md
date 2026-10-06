---
name: "Chronicle"
slug: "chronicle"
description: "Preserve operational history and intent across agent sessions. Use when resuming work, recording a decision, preparing a destructive or bulk operation, verifying a deployment, correcting a claim, reconstructing a captured file version, or handing off unfinished work."
category: "Developer Tools"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/chronicle"
---

# Chronicle

Chronicle separates observed events from the intent only the person or agent doing the
work can state. Capture requires installed, active hooks; check coverage before assuming
the trace is complete.

## Resume first

Run `chron resume` in the project root. Read unresolved questions and state declarations.
Then record what you are taking up:

```bash
chron open "continue search" --state "empty results are intentional staging"
```

If the CLI is missing, install with
`pipx install 'git+https://github.com/AntreasAntoniou/chronicle.git'`. Installing the skill
does not install hooks or establish capture coverage.

## Five moments worth recording

| Command | What to record |
| --- | --- |
| `chron open` | Your belief about current state and what you are taking up |
| `chron arm` | The operation, intent, reversibility class, and verified restore path |
| `chron decision` | The choice, reason, and any ambiguous state that is intentional |
| `chron landed` | A verified external change with resource/version and rollback references |
| `chron close` | Where work stopped, what remains undone, and open questions |

Before a destructive or bulk operation:

```bash
chron arm "replace the staging index" \
  --intent "load the verified replacement" \
  --class R1 \
  --restore "snapshot path and tested restoration command" \
  --verified "restoration tested on a disposable copy"
```

R0 is fully reversible, R1 needs a recovery artifact, and R2 is irreversible. An ARM does
not grant user authority or prove that a host gate is active. Follow the user's scope and
verify hook integration separately.

After publication or deployment, record observed state using `chron landed --ext` and
`--verified`. A successful command alone does not prove an external change.

## Correct and recover

Append `chron correct` with the original entry ID, truth, and evidence. Preserve history.

```bash
chron history src/app.py
chron show src/app.py --at 2h
chron restore src/app.py --at 2h --to /tmp/recovered-app.py
chron search "search index"
chron doctor
```

Only captured versions can be recovered. State gaps explicitly. Use `chron experiment`
and `chron abandoned` for attempts and dead ends, quoting measured results only.

## Inference and privacy

- Narrated entries marked `inferred` are hypotheses. Inspect anchored events before
  acting; append a firsthand statement when you can resolve an uncertainty.
- Narration requires an explicit model, can incur cost, and sends trace content to that
  provider. Review its dry-run prompt first.
- Keep secrets out of narrative entries and keep the ledger, CAS, transcripts, and canvas
  private. Redaction does not guarantee detection of every embedded secret.
- Keep operational history here; route commitments to a task tracker and lasting
  knowledge to canonical project documentation.

Read [references/codex.md](references/codex.md) before experimenting with Codex hooks.
Configuration, trust, execution, and verified coverage are separate states.

## Installation and upstream provenance

The upstream skill identifier is `chronicle`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/chronicle --skill chronicle --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/chronicle#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`016848e36fb8`](https://github.com/AntreasAntoniou/chronicle/tree/016848e36fb89c8b199a1c265e543d31b3a36795). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
