---
name: "Questlog"
slug: "questlog-agent-skill"
description: "Maintain an explicit Markdown commitments ledger with a local cockpit for NOW, next actions, deadlines, waiting items, workstream states and inbox capture."
category: "Calendar, Email & Productivity"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/questlog-agent-skill"
---

# Questlog

Resolve the user's explicit `QUESTLOG_ROOT` before reading or changing commitments. Read [README.md](README.md) for startup and [references/ledger-format.md](references/ledger-format.md) for the grammar. A fresh install is empty; do not seed personal records or infer commitments from general discussion.

Capture only the authorized delta, separating commitments from reference knowledge. Keep NOW bounded, identify the next concrete action, and distinguish deadlines from waiting-on dates. Propose uncertain priorities instead of assigning them silently. Use the ledger's actual evidence; local notes do not establish that an email was sent, a job ran, or a deadline was accepted.

For changes use the bundled CLI or loopback UI so writers share the lock. HTTP ledger writes require `If-Match` with the current `/api/state` head; a 409 means reload and reconsider, not overwrite. Inspect diffs when editing a complete ledger. Direct external editors must be stopped or coordinated: the runtime cannot lock an editor that ignores its lock.

The cockpit can capture local instruction drafts, but this package includes no runner: pending means saved, never executed. Mail, calendar, semantic search, archive routing and host scheduling are optional external integrations, not prerequisites. Use an available host-native scheduler only when requested; do not install cron jobs by default. Each external action retains its own authorization boundary.

## Installation and upstream provenance

The upstream skill identifier is `questlog`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/questlog-agent-skill --skill questlog --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/questlog-agent-skill#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`522949dfc6ba`](https://github.com/AntreasAntoniou/questlog-agent-skill/tree/522949dfc6ba05e79507fe272525f3689b3a799b). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
