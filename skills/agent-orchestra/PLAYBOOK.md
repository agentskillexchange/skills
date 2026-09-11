# Multi-Agent Orchestration Playbook

This is the compact operating reference for the graph grammar in `SKILL.md`.

**The first principle:** the patterns below are *primitives, not a menu.* You compose them into
**arbitrary configurations — in parallel, in series, and nested within each other** (any node can
itself be a whole sub-graph). Composing a bespoke topology for the task is the norm; reflexively
reaching for one named pattern is the anti-pattern.

## Decision Tree — Which Pattern?

```
Is it a simple task (< 5 min, no ambiguity)?
  → Single agent. Don't over-engineer.

Is correctness critical (code, data, research claims)?
  → Byzantine 2+1 (2 workers + 1 arbiter)

Is it research or prediction (facts must be verified)?
  → Triple-Verified A+B+C (2 researchers + 1 cross-reference verifier)

Is hallucination the primary risk (paper reading, technical summaries)?
  → Pyramid Byzantine (N workers → comparator → verifiers → integrator)
  → Tag outputs: ✅ VERIFIED / ⚠️ CONTESTED / ❌ STRIPPED

Does it need iterative quality improvement?
  → Committee Review N×M (N reviewers × M rounds until quality bar met)

Is it a multi-day project with task dependencies?
  → Grinding Mode (1 coordinator + N workers, shared state)

Do I need genuinely diverse perspectives (strategy, creative, controversial)?
  → Hecate Dimensional Search (dimensions defined by NEGATIVE constraints)
  → Or: Rich Personas (100+ attributes per persona)

Do I need maximum coverage against model-specific blindness?
  → N×M Aggregation (N personas × M model backends → self-aggregation)

None of these fits cleanly?
  → Compose your own graph. Nest a pyramid inside a committee node; run two
    pyramids in a feedback loop; condition a visual stage on a text verdict.
    The grammar (parallel / series / nested) is the product, not the catalog.
```

## Pattern Quick Reference

| Pattern | Agents | When | Overhead |
|---|---|---|---|
| **Single** | 1 | Simple tasks | None |
| **Byzantine 2+1** | 3 | Correctness-critical | Low |
| **Triple-Verified** | 3 | Research, predictions | Low |
| **Pyramid** | 5-15+ | Hallucination-prone | Medium |
| **Committee N×M** | N×M | Quality iteration | Medium |
| **Cross-Review** | N×2 | Peer-informed revision | Medium |
| **Grinding** | N+1 | Multi-day projects | High |
| **Hecate** | N+Σ | Emergence, orthogonality | High |
| **N×M Aggregation** | N×M | Maximum diversity | Very High |

## Invariants (Every Pattern)

1. **Workers NEVER see each other's output** — isolation is what makes redundancy meaningful. A
   peek through the wall wastes N−1 agents.
2. **Identical specs** — only the output path differs between workers.
3. **Arbiter decides, orchestrator doesn't override** — trust the process.
4. **Name every agent** — Hector, Prometheus, Athena. Names give weight and accountability.
5. **Stage in git branches, NEVER /tmp** — Each worker gets a dedicated git branch:
   `byzantine/{task-id}/{agent-name}` (e.g., `byzantine/eudaemon-ui-spec/prometheus`). Workers
   commit all outputs to their branch. The orchestrator/arbiter merges or cherry-picks from
   branches. **NEVER use `/tmp` for Byzantine *outputs*** — `/tmp` gets cleared on reboot and all
   work is lost. Git branches are durable, diffable, and auditable. If no git repo exists for the
   task, create one or use the project repo with branches. (Distinct from giving agents a disposable
   `/tmp` *source clone* to protect the live tree — that's about the input, not the output.)

## Byzantine 2+1 Protocol (Default for Most Work)

```
1. Spawn Worker-A and Worker-B with identical prompts + isolated output dirs
2. Both work independently — zero shared context
3. Spawn Arbiter-C with both outputs
4. Arbiter applies decision matrix:
     Full agreement      → Apply directly (confidence 90-100)
     Minor differences   → Pick cleaner (confidence 80-95)
     Structural diffs    → Analyze, merge (confidence 60-85)
     Fundamental dissent → Escalate to human (confidence 0-40)
5. Arbiter's output is the deliverable
```

## Pyramid Byzantine (When Hallucination Is the Risk)

```
1. Spawn N workers independently
2. Comparator receives all N outputs
3. Spawn floor(N/2) verifiers per disputed cluster
4. Tiebreaker for remaining disputes
5. Integrator produces final output with labels:
     ✅ VERIFIED   — unanimous agreement
     ⚠️ CONTESTED  — legitimate disagreement, resolved with reasoning
     ❌ STRIPPED    — confirmed hallucination, removed
```

## Committee Review (When Quality Must Iterate)

```
1. N reviewers produce independent reviews (round 1)
2. Arbiter reads all, decides: conclude / another round / targeted question / debate
3. If another round: reviewers see previous round's feedback, produce revised review
4. Repeat until quality bar met or M rounds exhausted
5. Arbiter synthesizes final output
```

## Hecate Dimensional Search (When You Need Emergence)

```
1. Define N dimensions by NEGATIVE constraints (what they CANNOT do, not what they are)
2. Each dimension produces output independently
3. Measure orthogonality: Ω = 1 - mean(pairwise_cosine_similarity)
4. Synthesis agent adjudicates disagreements — NO AVERAGING
   → Pick winners, preserve dissent, strip fabrications
5. Measure emergence: E(R) = claims in synthesis not traceable to any single dimension
```

**Axiom 5 is sacred:** Synthesis MUST adjudicate, not smooth. Averaging destroys the signal.

## Rich Persona Design (When Diversity Matters)

100+ attributes per persona across:

- **Professional** (role, methodology, achievements)
- **Background** (education, mentors, trajectory)
- **Demeanor** (communication style, risk tolerance, contrarian tendency)
- **Nuances** (pet peeves, blind spots, unusual expertise)
- **Quirks** (humor, habits)
- **Biases** (acknowledged weaknesses)

Surface variation ("You are an expert in X") produces surface diversity. Rich personas produce
genuine diversity. For review graphs, an *annoyed, anchored, biased* reviewer catches what a polite
"expert" waves through — and obvious disqualifying defects (placeholders, broken figures) should
**hard-cap** the score, never average into a soft deduction.

## Escalation Protocol

When confidence < 40 or fundamental disagreement:

1. Generate `escalation.md` with: disagreement summary, both positions, analysis, tentative
   recommendation
2. Surface to the human with clear framing
3. Never silently pick a side on low-confidence disputes

## Meta-Principles

- **Formal theory as communication protocol** — Mathematical structure constrains AI interpretation.
  The rigor is for transmission fidelity, not peer review.
- **Negative constraints > positive roles** — "Must NOT do X" creates harder boundaries than
  "You ARE a Y."
- **Redundancy catches errors** — Independent execution surfaces agreement (validation) and
  disagreement (investigation).
- **Emergence requires orthogonality** — Diverse perspectives must be genuinely independent to
  discover intersection patterns.
- **Self-aggregation preserves coherence** — Let the persona synthesize its own multi-model outputs,
  not an external arbiter.
- **Compose freely** — arbitrary configurations in parallel, in series, and nested within one
  another. The named patterns are building blocks for the graph you actually need.
