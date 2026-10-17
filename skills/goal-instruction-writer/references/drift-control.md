# Drift Control Reference

Use this reference for Goals that run for more than a few iterations, cross
phases, touch several artifacts, or invite exploratory side quests. Drift is a
change in direction that is not justified by the Goal Anchor, even when the
new work is technically useful.

## Freeze a Goal Anchor

Write this short block before the first work unit and carry it through every
checkpoint:

```text
Goal Anchor: <one sentence describing the user/system outcome>
Success criteria: C1 <...>; C2 <...>; C3 <...>
Frozen scope: <invariants, protected behavior, and forbidden side effects>
Allowed authority: <tools, files, systems, and approvals available>
Current phase: <phase or milestone>
```

The Anchor is an invariant, not a plan. Plans may change when evidence changes.
The outcome, acceptance criteria, frozen scope, or authority may change only
through an explicit owner decision, a durable scope-change record, or a new Goal
version. Never rewrite them to justify work that already happened.

## Use an iteration alignment record

Before acting, write:

```text
Iteration: <number>
Target criterion: <C1/C2/...>
Expected delta: <observable evidence that should change>
Scope reason: <why this is inside the frozen boundary now>
```

After verifying, append:

```text
Actual evidence: <test, diff, artifact, source, or decision>
Alignment: ON_TARGET | SIDE_QUEST | DRIFTED
Decision: continue | defer | replan | pause
Next cursor: <single next work unit or unblock>
```

The three alignment labels have different behavior:

- **ON_TARGET:** the named criterion moved and the evidence supports a
  justified next step. Continue.
- **SIDE_QUEST:** the work may be useful but is not required by this Goal.
  Record it in a deferred list and return to the next unmet criterion.
- **DRIFTED:** no criterion moved, the work changed the Goal or scope, or the
  next action cannot be justified from the Anchor. Stop and realign.

## Detect drift early

Treat any of these as a drift signal:

- The agent cannot name which criterion the current action advances.
- The expected evidence is replaced by activity, volume, or elapsed time.
- A new issue becomes the main work without a recorded link to the outcome.
- Allowed files, systems, sources, or side effects expand silently.
- The baseline or acceptance criteria are rewritten to fit completed work.
- Two consecutive iterations produce no acceptance progress or repeat the same
  hypothesis without new information.
- The plan keeps generating “one more” improvement after all criteria are
  already verified.

The default no-progress threshold is two materially equivalent iterations; use
a smaller threshold for high-risk or expensive work and a larger one only when
the task's evidence is naturally sparse.

## Run phase gates

Run a phase gate every 3–5 iterations by default, at each milestone, and before
an irreversible or high-cost action. A phase gate should:

1. Re-read the Goal Anchor and compare it with the current state.
2. Mark each criterion `open`, `verified`, or `blocked` with evidence.
3. Review the diff or artifact list against Allowed and Frozen scope.
4. Move side quests to the deferred list with a reason and revisit condition.
5. Record one justified next action, its target criterion, and expected delta.

If there is no justified next action, finish as complete or stop as blocked;
do not invent work to keep the loop alive.

## Recover from drift

When a drift trigger fires:

1. Stop the current loop before taking another action.
2. Write the alignment record and preserve the last durable cursor.
3. Compare current changes with the baseline and classify them as aligned,
   deferred side quest, or unauthorized scope change.
4. Keep aligned evidence. Isolate or revert side-quest changes only when the
   authority and repository safety rules allow it; never discard external work
   silently.
5. Re-plan one next action from the Anchor, or ask the owner for a scope or
   objective decision.
6. Resume only after the checkpoint records `ON_TARGET` and an expected delta.

Use `GOAL PAUSED: realignment required` as the default control stop. Report the
last aligned criterion, the drift trigger, preserved evidence, deferred work,
and the exact decision needed to resume.

## Minimal prompt block

```markdown
## Goal anchor
- Outcome: <one immutable sentence>
- Criteria: <C1, C2, C3>
- Frozen scope: <invariants and forbidden side effects>
- Current phase: <phase or milestone>

## Drift control
Before each iteration, name one target criterion, expected evidence delta, and
scope reason. After verification, label the result `ON_TARGET`, `SIDE_QUEST`, or
`DRIFTED`. Park side quests. Re-read the Anchor every 3–5 iterations, at phase
gates, and before irreversible work. If no criterion moves for two equivalent
iterations or the Anchor/scope changes without approval, stop and emit
`GOAL PAUSED: realignment required`; record the cursor and exact re-alignment
decision needed before resuming.
```
