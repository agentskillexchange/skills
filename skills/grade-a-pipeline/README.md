# Grade-A Pipeline

Grade-A Pipeline is a worked multi-agent software-delivery workflow: map the repository, agree
on a dependency-aware plan, build in isolated Git worktrees, test between integration steps,
and return a reviewable branch with the evidence from the run.

It is for changes large enough that “ask several agents to implement it” leaves important
questions unanswered: do they understand the same interfaces, are they editing overlapping
files, did integration break earlier work, and can you inspect the attempts that were rejected?

This repository contains an **Agent Skill and an editable JavaScript workflow adapter**, not a
standalone coding agent, CI service, or guarantee of Grade-A software. The host provides agent
execution and tools; the workflow supplies the organization of the work.

## When it is useful

Use it for a substantial feature, refactor, migration, or new package whose work can be split
into explicit interfaces and file ownership. It is less attractive for a one-file fix: repository
mapping, competing implementations, and several review stages have real token and runtime costs.

For example, adding pagination may require a shared cursor format, data-access changes, an API
contract, client handling, and tests. The useful parallelism is not “all five at once.” Agree on
the cursor interface first, then let independent modules develop against it, then exercise the
whole request path after integration.

For a greenfield repository, describe the target system and acceptance criteria explicitly.
The adapter has greenfield-aware planning prompts so a thin scaffold is treated as something to
build from, not merely documentation to polish. On tightly coupled systems, a shared typed
interface and failing tests can give parallel implementers a firmer starting point.

## How the pipeline works

```text
map repository -> two planners + arbiter -> dependency plan -> baseline tests
    -> build a batch -> review competing diffs -> integrate -> full-suite check
    -> repeat for dependent work
    -> broader test battery -> review/harden rounds -> grade + branch handoff
```

The repository map is shared with downstream workers, reducing repeated discovery and giving
them a common account of modules and interfaces. Tasks are arranged into dependency waves;
declared file overlaps are split into sequential batches.

Each task gets two implementation attempts in separate worktrees and branches. A verifier
compares their diffs, then an adversary tries to refute the selected change. High-severity
refutations are excluded from integration. An integrator applies accepted diffs on a dedicated
integration branch and is instructed to rerun the full suite after each batch.

The final battery requests unit, integration, end-to-end or contract, property or edge-case,
lint/type, and security checks. Reviewers inspect correctness, security, simplicity, test
quality, and performance. A bounded hardening loop addresses new blocking findings, followed
by a rubric-based grade that should not let good work compensate for a disqualifying defect.

This is the “test sandwich”: a pre-change baseline, regression checks throughout integration,
and broader checks at the end. Its value is the evidence and checkpoints, not the letter grade.

## What it leaves behind

The intended durable output is `gap/<run>/integration`, ready for your inspection rather than
automatically merged into the base branch. Per-agent `gap/<run>/task-*` branches retain competing
attempts, and wave tags identify integration checkpoints. Worktrees are removed during cleanup;
branches and tags are retained.

The returned object includes:

- the integration and base branches, task plan, map, and wave tags;
- test history, battery findings, grade and gate reason;
- unresolved review findings and escalations;
- reported pushed refs, cleanup status, and a cumulative diff.

Use those records to investigate the run. Re-run the relevant checks on the final branch and
inspect unresolved issues before deciding to merge. Returned success fields are agent reports,
not independent proof that commands ran or a remote received a push.

## Install and launch

```bash
npx skills add AntreasAntoniou/grade-a-pipeline
```

Read [SKILL.md](SKILL.md), then inspect the
[workflow adapter](examples/grade-a-pipeline.workflow.js) before granting it access to a repository.
It needs Git, the project's build/test environment, and a compatible host exposing a `Workflow`
launcher with `agent`, `parallel`, `phase`, `log`, and `args`. Installing the skill does not
install that host. The JavaScript file is not a standalone Node program.

An example invocation for a compatible host:

```javascript
Workflow({
  scriptPath: "/path/to/grade-a-pipeline/examples/grade-a-pipeline.workflow.js",
  args: {
    repoPath: "/path/to/target-repo",
    request: "Add cursor pagination to the search endpoint. Preserve existing " +
             "default behavior and test empty pages, invalid cursors, and traversal.",
    maxReviewRounds: 3,
    gradeBar: "A****",
    push: false,
    pushAgentBranches: false
  }
})
```

Keep remote mutation disabled unless the user has explicitly authorized the destination and
refs. Both push options default to false. Set a separate host-level budget before launching;
a planning parameter is not a spending cap.

## Read this before running against a real repository

The adapter uses worktrees **inside the target repository**, under `.gap-worktrees/<run>/`.
They share Git objects and refs. This differs from Agent Orchestra's disposable-source pattern:
it preserves inspectable local branches, but is not a security boundary.

The build instructions keep code changes off the base branch, but the workflow is not wholly
read-only toward your existing checkout:

- Bootstrap updates `.git/info/exclude` to hide its worktree directory.
- Cartography commits `MAP.md` on the integration branch **and copies it into the target root**.
  Protect an existing root `MAP.md` before running.
- For a non-Git directory, bootstrap instructs an agent to initialize Git and create an initial
  commit from its contents. Do not point it at an arbitrary directory.
- Cleanup removes run worktrees. Inspect and preserve needed uncommitted artifacts before
  authorizing cleanup after a failed or interrupted run.

Use a recoverable backup and a reviewed target path. A worktree instruction does not prevent an
agent from accessing other files, credentials, networks, or Git refs.

## Current limits: checks are not all enforcement

The adapter is a worked composition, not a hardened transactional build controller. In particular:

- A regression is recorded as an escalation; the JavaScript does **not** automatically stop later
  waves or roll back the failing integration.
- Scheduling relies on the plan's declared dependencies and file lists. Dependency cycles fall
  back to a wave rather than failing closed. Review the plan before consequential execution.
- The review loop deduplicates repeated findings. No *new* blockers is not proof that old ones
  were fixed; inspect the evidence and final branch.
- Test execution, defect scanning, and grading are delegated to agents. Missing tools, weak
  assertions, omitted results, and mistaken reports still need independent attention.
- The `maxWaves` setting is read into configuration but is not used to limit scheduling or
  execution. Only a real host budget can bound spending across all agent calls.
- Worktree separation and declared file ownership are not permission enforcement. The workflow
  does not establish release readiness, deploy software, or authorize merging or publication.

The `A****` label is this workflow's configurable rubric, not an external certification.

## How it differs from related skills

[Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra) is the general vocabulary
for designing collaboration graphs; Grade-A is an opinionated build-side composition.
[Plus Ultra](https://github.com/AntreasAntoniou/plus-ultra) proposes two plans and applies one,
then checks reality; Grade-A produces competing implementations task by task.
[Agent Collaboration Control](https://github.com/AntreasAntoniou/agent-collaboration-control)
adds project authority, evidence-state, and ongoing-supervision rules. It is not supplied by a
high grade or a passing test suite.

## Validate the package

From a local checkout:

```bash
node --check examples/grade-a-pipeline.workflow.js
python3 -m unittest discover -s tests
```

These check JavaScript syntax and package properties, including opt-in push defaults. They do
not run the workflow or test an end-to-end software build.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Licensed under the
[MIT License](LICENSE).
