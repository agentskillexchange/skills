---
name: "Grade-A Pipeline"
slug: "grade-a-pipeline"
description: "Map a codebase, decompose requested work into a dependency graph, and run a test-sandwiched multi-agent software pipeline with isolated worktrees, per-wave regression checks, adversarial review, and an explicit quality rubric. Use for substantial builds, fixes, or refactors that benefit from parallel implementation and conservative integration."
category: "Code Quality & Review"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/grade-a-pipeline"
---

# Grade-A Pipeline

An opinionated software-engineering workflow that composes `agent-orchestra` for the build case. It maps the repository, plans a dependency graph, isolates implementers in worktrees, tests every integration wave, and subjects accepted work to independent review. The rubric is evidence about the run, not a guarantee of software quality.

> This is the build-side sibling of `live-test` (which exercises a running system through the browser) and `saturating-review-engine` (which hardens a rendered artifact). Use this one when the deliverable is *code in a repo*.

## What it does (the test sandwich)

```
BOOTSTRAP    open integration branch + worktree IN-REPO (no /tmp) + detect commands
CARTOGRAPHY  N readers over file shards → synth → MAP.md (committed + at repo root)  ← the MAP
PLAN         2 isolated planners → arbiter → task DAG (disjoint single-owner files)
BASELINE     run the existing full suite (read-only worktree)                     ← sandwich ▽
BUILD waves  per wave: file-disjoint batches; each task = 2 TDD impl → verify → adversary
             ↳ each implementer works in ITS OWN worktree+branch (gap/<run>/task-<id>-<variant>), commits
INTEGRATE    commit accepted diffs onto the integration branch, re-run FULL suite,← sandwich ▽ (every wave)
             tag gap/<run>/wave-N, push checkpoint to origin = a checkpoint you can revert to
BATTERY      unit · integration · e2e · property · lint/type · security in parallel ← sandwich △
REVIEW       code-review pyramid (5 lenses) + harden (commits+tags), loop until no blocking findings
GRADE        A**** rubric panel + deterministic defect pre-scan → hard gate
CLEANUP      remove worktrees; branches + tags persist in the repo
```

Tests are **sandwiched at three depths**: a baseline before any change, a full-suite regression gate after *every* wave, and a full battery of all test types at the end. The MAP built in Cartography is **injected into every downstream worker** so no agent re-derives the codebase.

### Greenfield builds, not just modifications

The pipeline **builds systems from scratch**, not only edits existing ones. Bootstrap classifies the repo (`code_file_count` / `is_greenfield`): an empty, docs-only, or thin-scaffold repo is flagged **greenfield**, and that `MODE` is injected into the MAP and both planners. The planners then **plan the delta from the request's *target end-state*, not the inventory of existing files** — net-new files are first-class task outputs, and in greenfield mode the planners are explicitly barred from the classic failure of anchoring on a design doc and scoping "reconcile/polish the docs" or "add a docs-consistency suite" instead of actually building the requested modules. Design/spec files are treated as the *source of the target*, never the thing to edit.

Two things still help a large greenfield build land cleanly: (1) phrase `request` as the **target end-state** ("the package must contain modules X/Y/Z with these interfaces and tests"), and (2) for tightly-coupled cores, optionally **seed a typed skeleton first** (fully-built shared types/interfaces + stubbed modules + failing tests + an `INTERFACES.md`) so the parallel implementers build against fixed seams — interface-first, then fan out. The pipeline works without the seed; the seed mainly buys integration coherence on big multi-module systems.

### In-repo by design — git worktrees, never `/tmp`

All work happens **inside the target repo** via git **worktrees** — no disposable clone, nothing in `/tmp`:

- **One worktree + branch per agent.** Every implementer runs `git worktree add -b gap/<run>/task-<id>-<variant> <repo>/.gap-worktrees/<run>/… <integration>`, works in that isolated directory, commits, and removes its worktree — **the branch stays as a real ref in your repo**. Because worktrees share the repo's object/ref store, each agent's full attempt (including the *losing* variant) is a branch you can `git diff` the instant it commits. No clone, no diff-shuttling.
- **The integration branch is the curated result**, held in its own persistent worktree. The integrator commits each *accepted* change onto `gap/<run>/integration`, one commit per task.
- **Each wave is a tagged checkpoint** (`gap/<run>/wave-N`); the branch + tag are pushed to `origin` if one exists (push failures are non-fatal and reported). Everything already exists locally in the repo regardless — pushing is just the remote mirror.
- **Your working tree is never touched.** Agents only ever `cd` into their own worktree under `.gap-worktrees/` (added to `.git/info/exclude` so it stays out of your `git status`); the base branch and your uncommitted changes are left alone. Worktrees are removed at the end; branches and tags remain.
- `<run>` is a sortable timestamp (`date +%Y%m%d-%H%M%S`) so runs never collide. If the target isn't a git repo, bootstrap `git init`s it (noted loudly) since the whole design is git-native.

## How to launch

The script lives at `examples/grade-a-pipeline.workflow.js`. Invoke it with the **Workflow** tool, pointing `args.repoPath` at the live repo and `args.request` at the work:

```
Workflow({
  scriptPath: "<this-skill-dir>/examples/grade-a-pipeline.workflow.js",
  args: {
    repoPath: "/abs/path/to/repo",       // the live tree (read-only to agents; they clone it)
    request:  "Add pagination to the search endpoint and cover it with tests",
    maxWaves: 8,                          // ceiling on dependency waves
    gradeBar: "A****",                    // the bar the grade gate must clear
    maxReviewRounds: 3,                   // review→harden loop ceiling
    shardSize: 40,                        // files per cartographer
    // --- remote checkpointing (work always lands locally in the repo; these govern PUSHES to origin) ---
    push: false,                          // remote mutation is opt-in
    pushAgentBranches: false              // remote mutation is opt-in
  }
})
```

`repoPath` is the target repository. All work happens in isolated worktrees and never on the base branch. Remote pushes are disabled by default and require explicit user authority for the exact repository and refs.

## What it returns — and what you (the caller) must do

The work lands on the **`integration_branch`** inside your repo as it goes (worktrees commit straight into the repo's ref store); the workflow never touches your working tree or your base branch. It returns `integration_branch`, `base_branch`, `wave_tags`, `pushed_refs`, `grade`, `test_history`, `battery`, `unresolved_review`, `escalations`, and a `cumulative_diff` fallback. Per orchestra directive 3 (*the orchestrator integrates; it does not draft*), **you** decide what to land:

1. **Read `grade` and `escalations` first.** If `gate_fired`, the named defect (red test, skipped/vacuous test, left-in TODO, leaked secret, incomplete work) is ground truth — fix it before merging.
2. **Inspect the branch:** `git -C <repo> log --oneline <base_branch>..<integration_branch>` — one commit per task, one tag per wave. Diff any single agent's attempt via its `gap/<run>/task-*` branch.
3. **Run the suite yourself** on the branch — never trust a claimed-green you didn't see.
4. **Act on `unresolved_review`** blocking findings the harden loop didn't close.
5. **Merge when satisfied:** `git -C <repo> checkout <base_branch> && git -C <repo> merge --no-ff <integration_branch>`. The `checkout_instructions` field in the result gives the exact commands. (If a run crashed and left worktrees behind: `git -C <repo> worktree prune` and `rm -rf <repo>/.gap-worktrees`.)

`MAP.md` is committed on the integration branch and copied to the repo root during Cartography — keep it; it's the living map for the next run.

## Tuning the structure (it's a composition, not a monolith)

The script is plain JS — edit it. Common moves:

- **Cheaper:** drop the planner arbiter to a single planner; set `maxReviewRounds: 1`; trim `BATTERY_KINDS`.
- **Harder:** raise verifiers per task, add a second adversary, widen `REVIEW_LENSES`, run implementers across model tiers (`model:` on `agent()`) so two witnesses aren't one model counted twice.
- **Stricter gate:** edit `RUBRIC` / `GATE_DOCTRINE` at the top of the script to encode this project's definition of done (coverage %, perf budget, accessibility, etc.).
- **Different inner build node:** the per-task node is Byzantine-2; swap in a Hecate lens spread or a single pass for trivial tasks (see `agent-orchestra` §2.11).

## Guardrails

- **In-repo, never `/tmp`.** Every agent works in its own git **worktree** under `<repo>/.gap-worktrees/<run>/`, isolated from the others and from your base branch / working tree. This is a deliberate departure from agent-orchestra directive 7 (disposable `/tmp` source): the user wants work in the real repo so it's tracked, so isolation comes from **per-agent branches + worktrees** instead of a throwaway clone. Agents are instructed never to touch anything outside their own worktree (not the base branch, not other worktrees, not `.git` internals).
- **Disjoint file ownership per wave** — `disjointBatches()` guarantees two agents never edit the same file concurrently; tasks that must share a file are serialized via `deps`.
- **Every diff faces an adversary** that defaults to "does not hold"; high-severity refutations are dropped from integration and surfaced as escalations.
- **The regression gate is real** — the integrator must run the suite and report the true exit status; a wave that reddens it is escalated, not silently passed.

See `agent-orchestra` SKILL.md (§4 the proven build pattern, §6 pre-flight checklist) for the doctrine this skill operationalizes (with directive 7 deliberately swapped for in-repo worktrees, per user preference).

## Installation and upstream provenance

The upstream skill identifier is `grade-a-pipeline`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/grade-a-pipeline --skill grade-a-pipeline --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/grade-a-pipeline#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`b416225c7a90`](https://github.com/AntreasAntoniou/grade-a-pipeline/tree/b416225c7a90eba57fe80a21f400dabe9f9d03bf). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
