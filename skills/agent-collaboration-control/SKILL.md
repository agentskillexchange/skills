---
name: "Agent Collaboration Control"
slug: "agent-collaboration-control"
description: "Establish, actively monitor, and operate project-agnostic collaboration control for multi-agent programmes, research campaigns, live experiments, long-running automation, consequential artifact production, incident recovery, evidence promotion, and cross-agent handoffs. Use when work needs ongoing agent support, a recurring independent watch, proactive anomaly or ambiguity reporting, explicit human authority, one writer per mutable surface, risk-scaled Agent Orchestra topology, transition journals, liveness proof, adversarial review, provenance, succession rules, or calibrated claim states across any project."
category: "Templates & Workflows"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/agent-collaboration-control"
---

# Agent Collaboration Control

Govern a project as a single-writer control system with independent evidence
review. Use Agent Orchestra to choose the graph; use this skill to control who
may act, what evidence authorizes transitions, and how results earn promotion.

## Orient before acting

1. Read the repository's agent instructions and current mission.
2. Locate the canonical collaboration contract, numerical or product gates,
   transition journal, resource budget, and evidence records.
3. Read the latest journal event, but treat it as historical evidence.
4. Re-measure actual processes, artifacts, revisions, outputs, and ownership
   before mutation.
5. Gate substantial autonomous, multi-agent, or resource-heavy work with the
   project's budget authority, such as `$butler`.

Never infer authority from a terminal pane, generated plan, old queue, or this
skill. If the project has no explicit role binding, remain read-only until the
human authority binds it.

## Bootstrap the project contract

When no contract exists:

1. Copy `assets/COLLABORATION_FRAMEWORK.template.md` into the project.
2. Copy `assets/collaboration-policy.example.json` beside the append-only
   transition journal.
3. Replace every bracketed placeholder and bind real identities to:
   - **human authority** — mission, budget policy, public, irreversible, and
     destructive decisions;
   - **controller** — sole writer for live operations and queue order;
   - **executor** — performs explicit controller directives and returns
     receipts;
   - **auditor** — independently checks validity, evidence, and provenance;
   - **integrator** — adjudicates supported positions and preserves dissent.
4. Map every mutable surface to exactly one current writer.
5. Define mission gates, claim states, journal path, evidence modes, succession
   conditions, escalation triggers, and canonical artifacts.
6. Obtain human approval before the contract authorizes live mutations.

Do not copy a project-specific threshold or identity into the generic contract.
The project's canonical mission and gate documents own those values.

## Scale topology to decision risk

| Decision | Minimum topology |
|---|---|
| Deterministic read or lookup | One agent |
| Routine reversible operation | Controller → executor → measured verification |
| Correctness-critical bounded step | Two isolated witnesses → arbiter |
| New design or experiment | Independent drafts → cross-examination → discriminating test or arbiter |
| Data, substrate, or instrument gate | Producer → isolated validity and instrument-intent auditor |
| Result interpretation or promotion | Result card → independent audit → refutation as risk rises |
| Champion, release, public, or irreversible decision | Evidence pyramid → provenance audit → human authority |

Apply these invariants:

- isolate independent first passes;
- give every consequential artifact an adversary;
- keep drafting, adversarial review, and integration distinct;
- adjudicate disagreement instead of averaging it;
- preserve unresolved dissent and provide an escalation path;
- use schemas for machine-processed outputs;
- give concurrent writers disjoint surfaces or serialize them;
- scale redundancy and cost to uncertainty and bits at risk.

Read `$agent-orchestra` when implementing a multi-agent graph. Use disposable
copies for code-producing waves and never expose a live tree to competing
writers.

## Gate execution

Evaluate work in this order:

1. **Admissibility:** authority, lineage, substrate, instruments, configuration,
   safety, and budget.
2. **Primary objective:** the project's exact success and kill criteria.
3. **Scorecard:** quality, cost, latency, risk, maintainability, and other
   declared trade-offs.
4. **Readiness:** frozen artifacts, provenance, independent review, named
   owners, reproducibility, and external validation where needed.

Predeclare the claim or intended transition, config diff, revisions, cost,
checkpoints, admissible evidence, stop rule, owner, and verifier. Activity is
not progress unless it moves a declared predicate. Keep ready resources
productive, but never invent filler work.

## Control live transitions

Before an authorized mutation:

1. Confirm the current writer and budget gate.
2. Create and validate an intent event.
3. Confirm exact process, arguments, revision, manifest, checkpoint, output,
   log destination, and named execution surface.
4. Execute one explicit stage. Do not use implicit stage chains.
5. Verify actual state with the evidence appropriate to the transition.
6. Append a receipt with measured evidence, limitations, owner, verifier,
   holds, cost, and one next transition.

For running jobs, require monotonic progress evidence such as a fresh cursor,
log, artifact size, completed work unit, or output-byte delta over a meaningful
interval. A live process, allocated memory, or one utilization sample proves
neither health nor death. Monitors report discrepancies; they do not compete
with the controller or silently auto-heal.

Never edit an appended event. Supersede it with a conformant event that names
the old ID. Timestamps and journals do not replace re-measurement.

## Maintain an active support watch

When the user requests ongoing monitoring or support, create or maintain an
actual recurring process. A framework, promise, or one-time handoff does not
constitute active support.

1. Inspect existing watches first and update or consolidate them instead of
   creating overlapping pollers.
2. Gate the autonomous cost, bind the watch to its read-only auditor identity,
   and name the controller and human escalation authority.
3. Make every cold invocation self-contained with four blocks:
   **TAG + CONTEXT**, **CHECK**, **REPORT**, and **STOP**. Include absolute
   paths, host and pane identities, exact commands or APIs, expected states,
   report destination, and side-effect limits.
4. Choose a cadence that matches meaningful state change, offset it from round
   times, and state any platform expiry or renewal requirement.
5. Persist observations and alert fingerprints in a single state file so
   reports are delta-based, idempotent, and deduplicated.
6. Verify the watch is active, its next run is scheduled, and the state file is
   usable before claiming ongoing support.

Measure health with workload-specific independent signals. For a suspected
hang, combine absence of logical progress, absence of artifact or output
growth, and repeated resource-state samples over an appropriate interval.
Never generalize one signal into a universal death test.

Speak up proactively when measurements conflict with the journal or plan, a
gate is missing, a claim exceeds its evidence, work is unsafe or stuck, or a
genuine ambiguity blocks the next safe transition. Send the controller one
concise, deduplicated advisory containing timestamped evidence, the hold, and a
precise question or cheapest discriminating check. Use an empty prompt or a
safe message channel; never clear or overwrite another agent's active input.
If the controller cannot receive it safely, report to the human authority.

The watch may observe, recommend, question, and hold. It must not mutate live
work, compete with the controller, silently auto-heal, or broaden authority.
Stop only on the user's request or a defined terminal condition. Renew an
expiring watch when the monitored campaign remains active and the request for
ongoing support still applies.

## Validate event packets

Customize the policy asset once, then validate each candidate:

```bash
python3 scripts/validate_transition_event.py \
  --policy /project/path/collaboration-policy.json \
  /project/path/candidate-event.json
```

Append only after `PASS`. The validator fails closed on policy drift, missing or
unknown fields, enum violations, malformed IDs or UTC timestamps, and empty
evidence. Extend the policy and validator deliberately before introducing new
event fields.

## Promote evidence conservatively

Define a monotonic project-specific ladder. A useful default is:

`observed → provisional → replicated → validated → claim-ready`

For every gate, state what it establishes and what it does not establish. Match
evidence to the question: use census evidence for population claims,
independent repeats for stability, frozen evaluation for final comparison, and
provenance plus adversarial review for public claims.

Completed work is not automatically a validated result. Negative, null, and
demoted results are first-class outputs. An adversarial hold persists until
evidence resolves it; silence is not assent.

## Handle controller loss narrowly

Leave healthy work running when the controller is unreachable. Permit
restorative succession only when the approved contract specifies:

- recorded lease expiry and a continuous unreachable interval;
- proof of death from process and progress evidence;
- an exact frozen restart manifest;
- an open safety and budget gate;
- an intent before restart and receipt afterward;
- a cooldown after recorded kill or completion.

The restorative lease must enumerate permitted actions. It never silently
grants new work, configuration changes, destructive actions, queue changes, or
reboots.

## Resolve disagreement and hand off

Resolve disagreement through the cheapest discriminating empirical check, then
the canonical document, then conservative claim retention. Let the active
controller decide reversible operational ties. Escalate mission, public,
irreversible, destructive, low-confidence, or still-underdetermined high-risk
choices to the human authority.

Finish with:

- decision class and current single writer;
- measured state and timestamp;
- exact artifact, config, revision, or process identity;
- evidence mode and claim state;
- unresolved holds, dissent, and uncertainty;
- resource or budget reference;
- one explicit next transition.

If ongoing support was requested, also report the watch identity, cadence,
state path, next scheduled run, expiry or renewal condition, and any alert that
still needs acknowledgement.

Update the smallest canonical artifacts. Preserve durable decisions and
evidence using the workspace's archival protocol, such as `$argus`.

## Installation and upstream provenance

The upstream skill identifier is `agent-collaboration-control`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/agent-collaboration-control --skill agent-collaboration-control --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/agent-collaboration-control#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`a4cc88589ed0`](https://github.com/AntreasAntoniou/agent-collaboration-control/tree/a4cc88589ed09955bd67bbc609747d1885e551c3). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
