---
name: token-efficient-orchestra
description: Assign model capability tiers deliberately across an Agent Orchestra graph. Use when redundant workers can be economical but arbiters, adversaries, integrators, and irreversible actions need stronger judgment. Provider-neutral; map the tier names to models available in the current host.
---

# Token-Efficient Orchestra

Apply model allocation as a second pass after choosing the graph. The topology decides what each
node does; this overlay decides how much capability and reasoning budget each node receives.

## Core assignment

- **Mechanical tier:** deterministic extraction, listing, and normalization with a tight schema.
- **Worker tier:** redundant drafters, code writers, test authors, and reviewers whose outputs will
  be independently checked.
- **Advanced tier:** difficult single workers and medium-stakes comparators.
- **Supervisor tier:** arbiters, adversaries, integrators, escalation decisions, and final gates.

The one-line rule: **redundancy can economize; chokepoints should upgrade.**

## Why the asymmetry works

Workers are redundant by design, so the graph can reject a weak attempt. A supervisor is singular:
its judgment selects what survives. An error at that chokepoint becomes the output. The verifier
should therefore be at least as capable as the worker it evaluates, and preferably use a different
model family when correlated blind spots matter.

| Role | Suggested tier | Reasoning effort |
|---|---|---|
| Mechanical extraction | mechanical | low |
| Redundant worker or test author | worker | normal |
| Difficult single worker | advanced | high |
| Comparator | advanced or supervisor | normal to high |
| Adversary or arbiter | supervisor | high |
| Integrator or irreversible-action gate | supervisor | high |

## Adapter example

Map these symbolic tiers to models offered by your runtime and tag every node explicitly:

```js
const MODELS = {
  worker: process.env.ORCHESTRA_WORKER_MODEL,
  advanced: process.env.ORCHESTRA_ADVANCED_MODEL,
  supervisor: process.env.ORCHESTRA_SUPERVISOR_MODEL,
}

const drafts = await parallel([
  () => agent(spec, {label: 'worker:hector', model: MODELS.worker, schema: PATCH}),
  () => agent(spec, {label: 'worker:prometheus', model: MODELS.worker, schema: PATCH}),
])
const verdict = await agent(arbitrate(drafts), {
  label: 'arbiter:athena', model: MODELS.supervisor, effort: 'high', schema: VERDICT,
})
```

Omitting a model may inherit an expensive or underpowered session default. In this overlay, an
untagged node is a configuration error.

## Do not economize

- Single-agent tasks, where one call is both worker and judge.
- Security-critical or irreversible operations such as migrations, deletion, deployment, or
  publication.
- Final prose when the shipped artifact is writing.
- Repeated worker failures: upgrade once instead of buying more rejected attempts.

Provider price and model quality change. Benchmark the models available to you and treat this
assignment as a decision framework, not a permanent leaderboard.
