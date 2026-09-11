---
name: "YYLO Ledger Task Management"
slug: "ledger-tasks-yylo"
description: "Operate a YYLO Ledger Kanban board from the command line with the yy ledger CLI; create, search, update, and mark tasks with required response receipts, manage blocked-by dependencies, compute ready and topologically ordered work, merge scattered boards with reviewed plans, and emit ndjson, JSON, XML, or table output."
verification: "listed"
source: "https://github.com/yylo-dev/yylo-skills"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "yylo-dev/yylo-skills"
---

# YYLO Ledger Task Management

Use this skill when an agent works in a repository whose task state is tracked by a YYLO Ledger board. All board operations run through the `yy ledger` command of the YYLO CLI (YYLO 0.2.2 supports the exact `yylo-ledger 0.2.0` task CLI surface; `yy kanban` is a labelled compatibility alias). The skill covers the full task lifecycle — create, list, search, get, mark, update, archive — plus dependency management with `blocked_by` relations, ready/ordered work computation, multi-directory board consolidation, and machine-readable output formats for scripting.

The board lives under the repository's `.juno_task/` directory. Task state is plain, hash-chained Markdown; the CLI is the only sanctioned mutation path. Agents read current task state before mutating it, preserve mutation receipts where offered, and never edit board files directly to change lifecycle state.

## Prerequisites

- Node.js and the YYLO CLI installed globally:

```bash
npm install --global @yylo/cli
yy ledger --version
```

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/yylo-dev/yylo-skills

## Task lifecycle commands

Create a task with status and tags:

```bash
yy ledger create "Task description here" --status backlog --tags feature,backend
```

Browse and filter tasks:

```bash
yy ledger list --status todo,in_progress --limit 10 --sort asc
yy ledger search --status todo --tag backend --limit 10
yy ledger search --body "OAuth" --open
```

Fetch full task details, including resolved dependency and related-task info:

```bash
yy ledger get TASK_ID
```

Update status with a required response message that documents what was done and how it was tested:

```bash
yy ledger mark in_progress --id TASK_ID --response "Starting work on this"
yy ledger mark done --id TASK_ID --response "Completed: implemented X, tested Y" --commit abc123def
```

Modify task fields or attach a commit hash:

```bash
yy ledger update TASK_ID --status todo --tags backend,urgent
yy ledger update TASK_ID --commit abc123def
```

Archive a task instead of deleting it (soft delete; data preserved):

```bash
yy ledger archive TASK_ID
```

## Dependencies and ordering

View blockers, dependents, and priority score for a task, then add or remove blockers:

```bash
yy ledger deps TASK_ID
yy ledger deps add --id TASK_ID --blocked-by BLOCKER1 BLOCKER2
yy ledger deps remove --id TASK_ID --blocked-by BLOCKER1
```

Cycle detection prevents circular dependencies automatically. List tasks whose blockers are all satisfied, safe to start:

```bash
yy ledger ready --tag backend --limit 5
```

Produce a topological order of open tasks for safe parallel execution planning:

```bash
yy ledger order --scores
```

Dependencies and relations can also be declared inline in task body text when tasks are created or updated:

```text
[blocked_by]TASK_ID[/blocked_by]
[blocked_by]ID1, ID2[/blocked_by]
[task_id]RELATED_ID[/task_id]
```

## Merging scattered boards

When tasks are scattered across subdirectories, first produce and review a deterministic plan, then apply only that reviewed plan and retain its receipt:

```bash
yy ledger merge ./sub1/.juno_task ./sub2/.juno_task --into ./.juno_task --dry-run --plan-file /external/ledger-merge-plan.json
yy ledger merge ./sub1/.juno_task ./sub2/.juno_task --into ./.juno_task --apply-plan /external/ledger-merge-plan.json --receipt-file /external/ledger-merge-receipt.json
```

## Output formats

Every command supports `-f json`, `-f ndjson` (default), `-f xml`, and `-f table`. Add `--raw` for compact output or `-p` for pretty printing, which keeps the CLI scriptable inside agent loops.

## Operating rules

- Keep tasks small enough to complete in one iteration; status flow is backlog, then todo, then in_progress, then done (or archive for abandoned work).
- Always pass `--response` when marking; use `--commit` to link task history to git history.
- Check `yy ledger ready` before starting work and `yy ledger order --scores` when planning parallel work.
- Read task state before mutation, preserve receipts, and route every change through the CLI rather than direct file edits.
- Normal discovery is hot-only; archived tasks are reached through exact `get`, explicit `history`, and bounded `archive-search`, never by enumerating archive files.

## References

- Canonical skill pack: https://github.com/yylo-dev/yylo-skills
- YYLO CLI (orchestrator providing `yy ledger`): https://github.com/yylo-dev/yylo
- License: MIT
