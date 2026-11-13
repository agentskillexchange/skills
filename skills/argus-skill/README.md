# Argus

**Turn the important parts of a conversation into knowledge the next session can find.**

A conversation ends with a decision, a corrected assumption, a useful result, or a promise.
If that information stays in the chat, the next agent may never see it. If every agent
copies it into another summary, you get several competing accounts of what is true.

Argus is a checkpoint-and-routing skill for that problem. It asks: **what changed that
should outlive this session, and where does that fact belong?** It preserves the meaningful
delta in the existing canonical record, keeps its evidence and links, and leaves the rest
of the conversation alone.

This is an [Agent Skill](SKILL.md) with two read-only Python helpers—not a hosted memory
service, an automatic transcript archiver, or a new database. The agent does the judgment
and authorized record editing. The helpers discover registered knowledge workspaces and
check their home-index links and configured backlinks.

## Why it is useful

Argus helps long-running work accumulate knowledge rather than accumulate summaries.
It is useful when a project spans many sessions, when research and operations live in
different repositories, or when private source material supports a public artifact.

The result should be small and concrete: a corrected project record, an evidence-backed
result, a commitment in the task system, or a link connecting a specialist archive to its
home index. There should be one authoritative home for each fact, not one per assistant.

## A checkpoint in practice

Imagine a session that chooses a deployment approach, measures a regression, and agrees
to ask a collaborator a question. Argus does not save the entire conversation as one note:

| Durable change | Where it belongs |
| --- | --- |
| Chosen approach and reason | The owning project's decision record |
| Measured regression and supporting artifact | The project's evidence or experiment record |
| Commitment to contact the collaborator | The configured task or commitment system |
| Public release produced from private work | A private output record linking outward to the public release |

It then checks the changed records and links, reports what was preserved, and says what
was intentionally left untouched. Unselected ideas, repeated summaries, and unsupported
claims are not automatically promoted into knowledge.

## How it works

1. Identify the decisions, corrections, evidence, commitments, or project-state changes
   that are genuinely new.
2. Resolve the registry of known archives and select the record's owner. Read that
   workspace's contract and configured paths before editing it.
3. Update the existing canonical surface. Use the configured task system for commitments
   and budget authority for resource records instead of inventing parallel ledgers.
4. Keep private specialist records reachable from the home archive and linked back to it.
5. Validate the changes and report the delta. Commit or publish only when separately
   authorized by the user or repository contract.

An Archivum is a Git-backed knowledge workspace with its own layout and agent contract.
The [registry and backlink contract](references/backlink-contract.md) maps stable logical
links to local directories. The [routing guide](references/routing.md) explains ownership.
Argus respects those existing structures; installing it does not create an archive system
or configure a task tracker for you.

## Install and inspect

Install the skill in a compatible agent harness:

```bash
npx skills add AntreasAntoniou/argus-skill
```

The runtime skill name is `argus`. Ask it to checkpoint the durable changes after a
meaningful milestone, or use the [checkpoint prompt](references/checkpoint-prompt.md) in
your workspace instructions. That prompt is a convention the agent follows, not a
background watcher or an enforced hook.

The helper scripts require Python 3.11+ (`tomllib` is part of the standard library there).
Run these commands from the installed skill directory or a clone of this repository,
replacing the registry path with your existing private registry:

```bash
export ARCHIVUM_REGISTRY=/path/to/00_meta/archivum_registry.toml
python3 scripts/discover_archivums.py --json
python3 scripts/check_backlinks.py --registry "$ARCHIVUM_REGISTRY"
```

Discovery reports registered archives, their configuration versions, and available agent
contracts. The backlink checker checks targets in the home index and configured home
anchors; it does not recursively prove the correctness of every statement or link in
every archive. Both scripts are read-only and make no model calls.

## Boundaries that matter

- Preservation is not permission to send mail, publish a draft, spend money, or create a
  new archive. Those retain their own authority boundaries.
- A fact belongs with its owner, not every place its keywords appear. If ownership is
  ambiguous, resolve it before writing.
- Public outputs must not expose private archive paths or backlinks. Keep the outward
  provenance link in the private record instead.
- Argus does not decide that a claim is true merely because it appeared in conversation.
  Preserve evidence, uncertainty, and whether something was proposed or actually done.
- No durable change means no checkpoint write. Do not recursively archive the fact that
  Argus just archived something.

## How it differs from the other continuity tools

- **Argus:** what should become lasting knowledge, and which record owns it?
- **[Cross-Agent Sync](https://github.com/AntreasAntoniou/cross-agent-sync):** what verified
  current-state handoff should Claude Code and Codex share?
- **[Chronicle](https://github.com/AntreasAntoniou/chronicle):** what happened during the
  work, why, and which captured file versions and recovery context remain available?

Argus is the step from working context to maintained knowledge. It does not replace an
operational history, source control, or a backup system, and it works without those two
companion skills.

## Test

```bash
python3 -m unittest discover -s tests
```

MIT licensed.
