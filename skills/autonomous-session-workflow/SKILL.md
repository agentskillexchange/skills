---
name: "Autonomous Session Workflow"
slug: "autonomous-session-workflow"
description: "5-phase repeatable structure for autonomous agent sessions: context-load, tiered work-selection, coordination claim, execute, and persist-learning. Prevents duplicate work across concurrent sessions and ensures every run produces durable artifacts. Runtime-agnostic — Claude Code, gptme, Codex, or any persistent-workspace agent."
verification: "listed"
source: "https://github.com/TimeToBuildBob/bob"
category: "Templates & Workflows"
framework: "Claude Code"
---

# Autonomous Session Workflow

A 5-phase repeatable structure for autonomous agent sessions that prevents duplicate
work, ensures durable learning capture, and keeps output bias toward meaningful shipped
artifacts rather than motion.

Battle-tested across thousands of autonomous sessions on the gptme architecture. The
phases are runtime-agnostic — adapt the specific tools to your stack while keeping
the phase structure intact.

## When to Use

- At the start of every autonomous agent session (no live human directing the work)
- When the agent must select its own work from a backlog or queue
- When sessions run unattended and need to produce durable artifacts

## When Not to Use

- Interactive sessions where a human provides the next prompt each turn — just respond
- One-shot tool invocations with a fixed target (no selection needed)
- Sub-agent calls spawned from a parent task (the parent already selected the work)

## The 5 Phases

### Phase 1: Context Load

Load the agent's identity, session state, and current world model.

```bash
# Read identity files — persona, goals, operating constraints
# (adapt to your stack: CLAUDE.md, AGENTS.md, system prompt, etc.)

# Read dynamic context — recent journal, task queue, git status, notifications
# (adapt: a context script, config-driven include, or prompt injection)

# Assess loose ends from prior sessions:
#   - Stale claims that should be completed or abandoned
#   - Pending replies on issues/PRs you promised to close
#   - In-progress branches or open worktrees
```

**Key question**: "What did I leave unfinished and what changed while I was offline?"

If a loose end is resolvable in <5 min, handle it here. Otherwise note it and proceed.

### Phase 2: Work Selection

Try tiers in order until you find actionable work. The tiers prevent the agent from
inventing busy-work when real tasks exist, and prevent starvation when all tasks
are blocked.

```
Tier 1 — Active tasks: work already in progress; highest priority
Tier 2 — Backlog quick wins: dependency-ready items you can complete this session
Tier 3 — Self-improvement: when all tasks are externally blocked
  ├─ Idea backlog (advance the highest-scored idea)
  ├─ Self-review / audit (find and fix a real issue)
  ├─ Internal tooling improvement
  ├─ Documentation (stale docs only)
  ├─ Code quality (typecheck, tests, lint)
  └─ Lesson quality (repair harmful or outdated lessons)
```

**Anti-monotony guard**: If the same category has dominated the last N sessions,
skip it even if it looks like the best pick. Category diversity is a forcing function
for learning new failure modes.

**When everything is dry**: If all Tier 1/2 tasks are externally blocked and Tier 3
lanes are saturated (daily limits hit), write a short restraint journal recording what
you checked and deliberately skipped. A justified NOOP is better than fabricating work.

### Phase 3: Claim

Before executing, acquire an exclusive coordination claim. This prevents two concurrent
sessions from executing the same work, flooding the same PR thread, or writing
the same file.

```bash
# Generic coordination pattern — adapt the tool to your stack:
claim_key="task:<task-id>"          # for task-backed work
claim_key="github:<owner>/<repo>#<num>"  # for issue-backed work
claim_key="content:<slug>:<date>"   # for content/artifact creation

# Acquire claim (example using a coordination CLI):
coordination work-claim "<session-id>" "$claim_key" --ttl 60
# CLAIMED → proceed
# DENIED  → another session is already on it; pick the next candidate
```

**Notify-before-claim rule**: Any action visible to others (posting a comment,
sending a message, opening a PR) must be gated by a claim first. Social actions
without claims converge and spam — a claimed-then-post pattern prevents flooding.

On completion: `coordination work-complete "<session-id>" "$claim_key"`
On pivot/failure: `coordination work-abandon "<session-id>" "$claim_key"`

### Phase 4: Execute

Do real work. The key discipline is shipping, not perfecting.

```
- Commit early and often (small, well-described commits)
- Run tests before committing (catch issues before CI does)
- Use conventional commits: feat/fix/docs/refactor/chore
- Push to origin before the session ends
- If stuck for >10 minutes, move on — don't sink budget in a rabbit hole
- Don't add unrequested features or scope creep
```

**50-minute budget**: Most autonomous sessions should complete meaningful work within
50 minutes. If the task is larger, ship an incremental slice and create a follow-up
task for the remainder.

### Phase 5: Persist

The most undervalued phase. Everything done in Phases 1–4 evaporates between sessions
unless it's durably committed.

```bash
# 1. Write the journal entry (session-specific file, append-only)
cat > journal/$(date +%Y-%m-%d)/session-<HASH>.md << 'EOF'
# Session <HASH>
**Date**: YYYY-MM-DD
**Outcome**: productive|blocked|noop — one sentence
**Category**: code|research|strategic|maintenance|...

## Why this work
[What led here]

## What I Did
[Concrete changes with commit/PR links]

## Verification
- [Tests passing? CI green?]

## Persisted Learning
- Task state: <task> → done/waiting
- New lessons: [if any]
- "No durable feedback this session" — if genuinely nothing to add

## Next
[Clear next action or blocking factor]
EOF

# 2. Update task state
task edit <task-id> --set state done   # or waiting, if blocked

# 3. If a recurring failure pattern was discovered, write a lesson/rule
#    (keyword-matched context file injected at the next session start)

# 4. Push all commits
git push origin master
```

**Persist-first rule**: If you discovered something useful, write the lesson BEFORE
applying it to the current work. Once the fix is in, the failure mode feels solved
and the lesson gets skipped. The journal captures what happened; the lesson captures
when to recognize it again.

## Installation

### Claude Code

Copy this skill directory into your agent's skill folder:

```bash
cp -R skills/autonomous-session-workflow ~/.claude/skills/autonomous-session-workflow
```

Then invoke with `/autonomous-session-workflow` to load the 5-phase checklist into context.

### Manual / any runtime

Copy `SKILL.md` into your agent's context path and load it at session start. The phases
are plain markdown — include the whole file or cherry-pick the sections relevant to
your stack.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "I'll skip the claim — I'm the only session running right now" | You can't see other sessions launching. Concurrent spawning is the default on production runtimes. The claim is the gate, not the observation. |
| "I'll write the journal after I finish the next task" | Sessions get interrupted. The journal gets skipped. Write it before pushing, not after "one more thing." |
| "This task is almost done — I'll skip Phase 5 and just commit" | Learning only compounds if it's persisted. The session that "almost" closed the loop is the session whose insight disappears by next run. |
| "My selection is obvious — I don't need to work through the tiers" | Selection that skips the tiers is the primary source of redundant work and duplicate PRs. The tiers exist because "obvious" is often not what actually needs doing. |
| "The lesson is too specific to be reusable" | Specific lessons (exact error message, exact command, exact failure mode) are the most valuable — they trigger precisely when needed. |
| "A justified NOOP feels like failure" | It isn't. A filler commit to dodge the NOOP label burns quota, feeds convergence churn, and hides the jam. A restraint journal IS the deliverable. |

## Red Flags

- Starting execution before claiming (convergence risk)
- Session ends with no journal and no updated task state
- Committing "in a moment" — if you haven't pushed before ending, you haven't shipped
- Three consecutive sessions in the same category without a forced diversity break
- "I'll remember this" — you won't; write the lesson now

## Verification

A well-run session satisfies all of these before closing:

- [ ] Claimed before acting (or justified why no claim was needed)
- [ ] Meaningful work committed and pushed
- [ ] Tests passed (or a known failure documented with reason)
- [ ] Journal entry written with `Persisted Learning` section filled in
- [ ] Task state updated (`active → done`, `active → waiting`, etc.)
- [ ] Claim completed or abandoned (not left as dangling lease)

## Adapting to Your Stack

| gptme concept | Your equivalent |
|---|---|
| `gptodo` | any task manager with state transitions |
| `coordination work-claim` | a lock file, Redis SETNX, or GitHub comment gate |
| `lessons/<category>/name.md` | any keyword-matched context file injected at session start |
| `journal/<date>/session-<hash>.md` | any append-only session log |
| `cascade-selector.py` | your work-selection heuristic or scheduler |

The pattern is the value, not the specific tools.

## Related

- `self-push` (in this catalog) — lazy-check before shipping any output
- `pre-landing-review` (in this catalog) — gate before merging significant changes
- `multi-lens-review` (in this catalog) — structured PR review across multiple lenses
- `five-element-spec` (in this catalog) — scope definition before starting work
