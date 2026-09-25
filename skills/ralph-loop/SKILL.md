---
name: "Ralph Loop"
slug: "ralph-loop"
description: "Run a ticket queue across agent sessions with a self-verifying loop: one item per iteration, verification gates outside the worker, commits only from a verified tree on a topic branch."
category: "Templates & Workflows"
framework: "Custom Agents"
verification: listed
source: "https://github.com/Thingscorp/skills/tree/main/skills/ralph-loop"
---

# Ralph Loop

Run a queue of vertical tickets across agent sessions with a self-verifying loop. Live agent context is disposable; durable state lives in `.ralph/` (plan, items, prompt, loop state, append-only progress log). One iteration completes exactly one item — no batching, no drive-bys.

The core discipline: never let the worker verify its own work. Each iteration spawns one fresh worker for a single item under a strict worker contract (change only that item's allowed paths, run the gate, never set `passes: true`, never touch `.ralph/loop.md`). When the worker returns, the engine saves the candidate as an immutable Git tree and runs the saved baseline gate plus the current gate **outside** the worker, in a detached worktree of that exact tree. Acceptance requires exit 0 and a final line of `ALL GATES PASS`. On pass, the engine commits hook-free (Git plumbing, not hook-rewritable `git commit`) from the verified tree, marks the item passed, appends an engine progress entry, and releases the `.git/ralph.lock` lock. On fail, it writes a recovery ref, restores the last verified branch state, and records the stop reason. A `runtime_contract` declares the verification gates, topic branch, protected paths, and the non-negotiable rules: one item per iteration, commit required, progress appended, never push without owner approval. Optional judgment gates (select, verify, triage, blocker, continue) let a small model answer the semantic questions so the frontier model doesn't have to; gate errors fall back to FIFO with the fallback stated. This is the portable alternative to runner CLIs: a ticket-queue contract any harness can follow, proven running real maintenance queues.

## Installation

### skills.sh installer (recommended)

```bash
npm exec --package=skills@1.5.7 -- skills add Thingscorp/skills --skill ralph-loop
```

### Manual install (any agent)

```bash
git clone https://github.com/Thingscorp/skills.git
cp -R skills/ralph-loop ~/.claude/skills/ralph-loop
```

Project-local instead of global: copy to `.claude/skills/ralph-loop` (Claude Code), `.cursor/skills/ralph-loop` (Cursor), or `.codex/skills/ralph-loop` (Codex CLI).

## Source

Upstream skill: https://github.com/Thingscorp/skills/tree/main/skills/ralph-loop — part of the MIT-licensed Thingscorp/skills library (15 operational SKILL.md playbooks). Companion skills: ralph-plan (verified plans + items, the upstream of this loop), ralph-swarm (parallel lanes), to-spec, quality-loop.
