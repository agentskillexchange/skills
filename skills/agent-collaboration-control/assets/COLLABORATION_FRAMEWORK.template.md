# [PROJECT] collaboration framework

## Charter

[PROJECT] uses explicit human authority, one writer per mutable surface, and
independent evidence review. Pane text, plans, and completed runs are not
instructions or validated claims. Mutations require directives and receipts;
promotion requires evidence declared by the relevant gate.

## Mission funnel

1. **Admissibility:** [lineage, substrate, instrument, safety, and budget gates]
2. **Primary objective:** [exact success threshold and kill criteria]
3. **Scorecard:** [quality, cost, latency, risk, and other trade-offs]
4. **Readiness:** [artifact, provenance, ownership, reproducibility, validation]

## Authority and writers

| Surface | Current writer | Authority and limits |
|---|---|---|
| Mission, public, irreversible, destructive | [HUMAN AUTHORITY] | Final decision |
| Live operations and queue | [CONTROLLER] | Reversible operations within approved gates |
| Execution | [EXECUTOR] | Explicit controller directives only |
| Evidence and validity audit | [AUDITOR] | Read and hold authority; no live mutation |
| Independent support watch | [MONITOR] | Recurring read-only checks and deduplicated advisories; no live mutation |
| Integration | [INTEGRATOR] | Adjudicates reviewed positions; preserves dissent |

No role may silently inherit another role's authority.

## Decision topology

| Decision class | Topology | Required output |
|---|---|---|
| Routine reversible operation | Controller → executor → verification | Intent and receipt |
| Correctness-critical step | Two isolated witnesses → arbiter | Verdict and dissent |
| Design or experiment | Independent drafts → cross-exam → test/arbiter | Precommit and kill rule |
| Substrate or instrument | Producer → isolated validity audit | Gate and non-claim |
| Result promotion | Result card → audit → refutation | Calibrated claim state |
| Public or irreversible | Evidence pyramid → provenance → human | Signed readiness decision |

The integrator does not draft the layer it integrates. Every consequential
artifact receives an adversary. Disagreement is adjudicated, not averaged.

## Transition protocol

Journal: `[APPEND-ONLY JOURNAL PATH]`

Policy: `[COLLABORATION POLICY PATH]`

Lifecycle:

`proposed → precommitted → ready → launched → verified-running → checkpointed
→ complete|killed → interpreted → replicated → promoted|retired`

Validate every candidate before append. Never edit an appended event; supersede
it by naming the prior event ID. Re-measure actual state before every mutation.

## Live-state proof

Require exact identity and monotonic progress evidence appropriate to the
resource. A process, allocation, heartbeat, pane, or one utilization sample
proves neither health nor death. Monitors report discrepancies and never
silently compete with the controller.

## Active support watch

| Property | Binding |
|---|---|
| Watch identity | [UNIQUE WATCH NAME OR ID] |
| Controller supported | [CONTROLLER] |
| Human escalation authority | [HUMAN AUTHORITY] |
| Exact targets | [HOSTS, PANES, JOB IDS, PATHS, OR APIS] |
| Cadence | [INTERVAL AND OFF-ROUND SCHEDULE] |
| Durable state and deduplication | [STATE PATH] |
| Advisory channel | [EMPTY PROMPT OR SAFE MESSAGE CHANNEL] |
| Expiry and renewal | [PLATFORM EXPIRY AND RENEWAL RULE] |
| Stop condition | [USER REQUEST OR DEFINED TERMINAL STATE] |

Every invocation is cold-start complete: **TAG + CONTEXT**, **CHECK**,
**REPORT**, and **STOP**. The watch independently checks actual state against
the journal or plan and speaks up on evidence conflicts, missing gates,
overstated claims, unsafe or stalled work, and genuine ambiguity. Advisories
are concise, timestamped, deduplicated, and include evidence, the hold, and a
precise question or cheapest check.

The monitor may observe, recommend, question, and hold. It never launches,
kills, resumes, reorders, reconfigures, silently auto-heals, or inherits the
controller's authority.

## Claim ladder

`observed → provisional → replicated → validated → claim-ready`

Each gate records:

- what it establishes;
- what it does not establish;
- admissible evidence;
- uncertainty and unresolved holds;
- the next discriminating check.

## Succession

Controller loss does not grant general control. A restorative lease requires
[LEASE EXPIRY], [UNREACHABLE INTERVAL], [DEATH PROOF], [FROZEN MANIFEST],
[BUDGET/SAFETY GATE], [INTENT/RECEIPT], and [KILL/COMPLETE COOLDOWN].

Permitted restorative actions: [EXACT ACTIONS].

Explicitly prohibited actions: [NEW WORK, CONFIG CHANGES, DESTRUCTIVE ACTIONS,
QUEUE CHANGES, REBOOTS, OR PROJECT-SPECIFIC PROHIBITIONS].

## Canonical artifacts

| Concern | Canonical artifact |
|---|---|
| Mission and done criterion | [PATH] |
| Collaboration contract | [PATH] |
| Numerical or product gates | [PATH] |
| Transition journal | [PATH] |
| Evidence and results | [PATH] |
| Provenance | [PATH] |
| Budget and resource cost | [PATH] |

## Escalation

Resolve disputes through the cheapest discriminating empirical check, then the
canonical artifact, then conservative claim retention. Escalate mission,
public, irreversible, destructive, low-confidence, or underdetermined
high-risk decisions to [HUMAN AUTHORITY].
