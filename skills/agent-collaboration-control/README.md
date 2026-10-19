# Agent Collaboration Control

Agent Collaboration Control is a skill for keeping consequential agent work under explicit
human control. It helps a team answer four questions throughout a project: **who may change
what, what actually happened, what the evidence justifies claiming, and what may happen next**.

It supplies an operating protocol, a project-contract template, and a small local JSON validator.
It does not run agents, grant permissions, schedule monitors, or enforce a lock on your systems.
Those capabilities must come from the host and the project's actual access controls.

## Why this exists

A multi-agent project can fail even when each agent is individually useful. Two agents may both
try to recover the same job. An old handoff may be mistaken for a current instruction. A live
process may be reported as healthy despite making no progress. A completed experiment may be
promoted to a validated result without the checks that would justify that claim.

This skill separates responsibilities and evidence states so those mistakes have somewhere to
be caught. One current writer owns each mutable surface. An independent auditor can investigate,
question, and place a hold without silently taking over execution. Human authority retains
mission, budget policy, public, destructive, and irreversible decisions.

It is useful for long-running research campaigns, live experiments, production automation,
consequential artifact work, and handoffs between agents. For a single read-only lookup, the
contract and journal overhead will usually be unnecessary.

## Example: a job looks stuck

Imagine one agent controls an experiment queue while another watches the running jobs. The
watch sees a process still present, but no new work units or output growth across several
appropriate observation intervals.

Under this protocol, the watch records timestamped evidence and sends one deduplicated advisory
to the controller. It does not kill or restart the job. The controller re-measures the state,
checks the approved budget and recovery rules, and either takes an authorized action or asks
the human. If it acts, it records intent first and a measured receipt afterward.

If the controller disappears, the watch does not inherit general control. Recovery is permitted
only under an already-approved, narrowly defined succession contract. The result is a clear
decision trail rather than two well-meaning agents competing over the same process.

## How it works

1. **Bind the project contract.** Name the human authority, controller, executor, auditor, and
   integrator. Assign exactly one writer to each mutable surface. Define budgets, success and
   stop criteria, approval boundaries, evidence requirements, and canonical record locations.
   Until roles are explicitly bound, remain read-only; approve the contract before live mutations.
2. **Check admissibility before performance.** Authority, provenance, instruments, configuration,
   safety, and budget come before optimizing a score. State the intended transition and what
   evidence will count before executing it.
3. **Record intent, act, then measure.** Validate a candidate event, perform one authorized stage,
   inspect actual processes or artifacts, and append the receipt. Never rewrite history to make
   an old event look current; supersede it and re-measure.
4. **Supervise without taking over.** When ongoing support is requested, configure a real
   recurring read-only watch with cold-start instructions, durable deduplication state, a safe
   advisory channel, and a stop condition. Verify its schedule before calling it active.
5. **Promote claims only when their gates are met.** “Observed,” “replicated,” and “claim-ready”
   mean different things. Retain null results, uncertainty, dissent, and unresolved holds.

The distinction between *operational state* and *claim state* matters. A job can be complete
while its result remains provisional. A validator can accept a receipt while the referenced
evidence still needs independent inspection.

## What you get

The protocol is intended to leave a project-specific collaboration contract, an append-only
transition journal, evidence-linked receipts and verdicts, and handoffs with one explicit next
transition. A configured support watch also needs its own identity, state file, cadence, next
run, and expiry or renewal rule. These are artifacts you create in your project, not services
started by installing this repository.

| Included file | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Full operating protocol, including monitoring, escalation, and succession |
| [Contract template](assets/COLLABORATION_FRAMEWORK.template.md) | Project roles, gates, journal, watch, claim ladder, and authority boundaries |
| [Example policy](assets/collaboration-policy.example.json) | Allowed event IDs, actors, event types, decision classes, and operational states |
| [Example event](assets/transition-event.example.json) | Shape of one evidence-bearing transition packet |
| [Validator](scripts/validate_transition_event.py) | Checks a policy and one candidate JSON event locally |

## Install and start

```bash
npx skills add AntreasAntoniou/agent-collaboration-control
```

In an Agent Skills-compatible host, ask to establish the collaboration contract for a named
project before operating it. Copy the template and policy into that project, replace placeholders
with real bindings, and obtain the necessary approval. Example roles and thresholds are not
authority to act on a real system.

From a local checkout, validate the supplied example with Python 3; no third-party Python
packages are needed:

```bash
python3 scripts/validate_transition_event.py \
  --policy assets/collaboration-policy.example.json \
  assets/transition-event.example.json
```

For a project event:

```bash
python3 scripts/validate_transition_event.py \
  --policy /project/path/collaboration-policy.json \
  /project/path/candidate-event.json
```

Append only after `PASS` **and** the project's authority and evidence checks. The helper validates
required and unknown fields, policy enums, ID shape, UTC timestamps, types, and nonempty evidence
references. It does not append to the journal itself.

## Where it fits

[Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra) designs the collaboration
graph. This skill governs authority and evidence across that graph and over time.
[Plus Ultra](https://github.com/AntreasAntoniou/plus-ultra) supplies one bounded independent-plan
and verification loop; [Grade-A Pipeline](https://github.com/AntreasAntoniou/grade-a-pipeline)
applies multi-agent patterns to software delivery. Neither replaces a project's live-operation
contract, and this contract does not replace their task-specific review methods.

## Limits and tests

The validator checks packet structure, not truth: it does not open evidence references,
authenticate actors, enforce allowed state-to-state transitions, verify a budget, or prove the
journal is append-only. Single-writer ownership, liveness checks, and succession rules remain
instructions unless your environment implements them. A process ID or utilization sample is
not a universal health test; define progress signals for the actual workload.

```bash
python3 -m unittest discover -s tests
```

The tests exercise the event validator. They do not prove that a real deployment follows the
collaboration contract or that any recurring watch is active.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Keep credentials and
private operational evidence out of public issues. Licensed under the [MIT License](LICENSE).
