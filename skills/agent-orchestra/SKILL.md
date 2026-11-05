---
name: "Agent Orchestra"
slug: "agent-orchestra"
description: "Design and compose multi-agent graphs for correctness, coverage, or creativity. Use when a task benefits from isolated proposals, explicit arbitration, adversarial verification, committees, recursive review, cross-modal checks, or saturation loops. Applies across agent runtimes; the included JavaScript workflow is one adapter."
category: "Templates & Workflows"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/agent-orchestra"
---

# Agent Orchestra

A catalog of multi-agent coordination structures and how to map them onto an orchestration
runtime. The goal: be *creative and deliberate* about topology — pick (or invent)
the structure that fits the task, not reflexively reach for one shape.

> **Token-efficient variant:** when budget matters, apply `token-efficient-orchestra` on top of
> any graph here — economical models for redundant workers and stronger models for supervision
> chokepoints (arbiter/adversary/integrator/gate). The rule of thumb:
> *redundancy downgrades, chokepoints upgrade.*

---

## 0. Prime directives

1. **Isolation is sacred.** Independent agents MUST NOT see each other's output. Separate
   spawns, separate dirs, identical specs. A peek through the wall wastes N−1 agents.
2. **The adversary is always on.** Every produced artifact gets a skeptic whose job is to
   *refute* it, defaulting to "does not hold" when unsure. This catches failure classes a verifier
   may pass — a corrupt patch, a vacuous test, a cosmetic timeout. Never ship a
   pyramid without the refutation stage.
3. **The orchestrator integrates; it does not draft.** You (the caller) apply/merge results.
   The pyramid's named agents produce content. Never also draft a layer yourself.
4. **Name every agent.** Greek pantheon or any structured convention — never "Worker A". Names
   make integration legible and the topology readable from a label.
5. **Receipts/provenance.** Every spawn is logged (who, what topology, which model). The result
   carries the decision trail (verdict, gaps, adversary holds/severity).
6. **Anti-averaging (Hecate Axiom 5).** Synthesis adjudicates disagreement — picks winners,
   preserves dissent, strips fabrications. It never smooths conflict into mush.

### Filesystem-safety directives (for code-producing structures)

7. **Agents clone from a DISPOSABLE source, never the live tree.** Make a throwaway copy first
   (`git clone --no-hardlinks <live> /tmp/<proj>-source`) and point agents at *that*. Assume an
   agent can escape its intended working directory. The disposable source limits the resulting
   damage to a throwaway copy rather than the live repo.
8. **Redact absolute live paths from any doc agents read** (e.g. SPEC.md). An agent that reads
   "local at <workspace>" may still reveal location cues. Don't hand them the address.
9. **Create a recoverable backup before every wave.** Push to a remote only when the operator has
   already approved that destination and content. Otherwise make a local bundle or verified clone;
   recoverability is mandatory, publication is not.
10. **Disjoint file ownership per wave.** Two agents editing the same file produce diffs that
    collide on apply. Give each item a single-owner file set; if items must touch a shared file,
    serialize them across waves or fold the shared edit into one item. New-capability modules land
    standalone; you hand-wire them at integration.
11. **Agents return diffs as text; you apply them.** `git add -A && git diff --cached` →
    `git apply --recount <patch>` on the live tree (recount tolerates wrong hunk counts, a common
    model error). Verify `.git` is intact and run the suite before committing.

---

## 1. Execution substrate and adapters

The graph grammar is runtime-neutral. Preserve isolation, typed outputs, dependency edges,
concurrency barriers, and filesystem boundaries when porting it. The code skeletons below use a
JavaScript workflow adapter exposing `agent`, `parallel`, and `pipeline`; that API is one adapter,
not a requirement of the pattern.

### JavaScript workflow adapter mechanics

- Scripts are **plain JavaScript**. No TypeScript — `: string[]`, interfaces, generics fail to parse.
- **No raw backticks inside template-literal briefs.** A backtick in a `\`...\`` brief closes the
  string early and breaks parsing. Use plain quotes inside briefs; escape backticks (`\\\``) only
  in the prompt-builder functions.
- `agent(prompt, {schema, label, phase, model, effort, agentType, isolation})` — with `schema`
  (a JSON Schema), the agent is forced to return a validated object. **Always use a schema** for
  anything you'll machine-process (diffs, verdicts, scores).
- `parallel([thunks])` — barrier; awaits all; a thrown thunk becomes `null` → `.filter(Boolean)`.
- `pipeline(items, stage1, stage2, …)` — **the default.** No barrier between stages; each item
  flows independently. Use `parallel` *inside* a stage for the fan-out, and pass `phase:` on each
  `agent()` to avoid races on the global `phase()` state.
- Concurrency is capped at `min(16, cores−2)`; pass up to 4096 items and they queue.
- `isolation: 'worktree'` only works if the session cwd is itself a git repo. When it isn't (common),
  use the disposable-`/tmp`-source pattern instead (directive 7).
- `budget` / loop-until-dry / loop-until-count patterns exist for unknown-size work.

---

## 2. Structure catalog

Each entry: **shape · when · adapter skeleton.** Compose freely; these are primitives, not a menu.

> **The default move is to COMPOSE a custom graph, not to pick one row.** The named structures
> below (pyramid, committee, Hecate, cross-review…) are *nodes and motifs*, not the unit of work.
> The real unit is **the graph you wire for this task** — sequential where there are dependencies,
> parallel where there aren't, multi-agent where one witness isn't enough, multi-type where
> different roles (builder / researcher / visual / adversary / integrator) belong on different
> nodes. A bespoke topology is *expected*, never exotic — you should reach for "what graph does
> this task want?" before reaching for any single skill or command. The worked example
> [`examples/saturating-review-engine.workflow.js`](examples/saturating-review-engine.workflow.js)
> is a custom graph for *any* reviewable artifact (paper, deck, README, landing page, design doc,
> dataset report) — read it as a template for how to compose, not as a paper tool.

### 2.0 The graph grammar (how to compose any custom topology)

Think in **nodes** and **edges**, then build it with the substrate from §1.

- **Node = an agent call** (`agent(...)`) with a role. Role types: DRAFTER, SYNTHESIZER,
  VERIFIER, ADVERSARY, VISUAL, INTEGRATOR, COORDINATOR. Pick the type per node — a graph is
  **multi-type** when nodes play different roles, which is the common case.
- **A node can itself be a subgraph (recursion).** A "reviewer" need not be one agent — it can be
  a whole pyramid+visual subgraph that *returns* a single review. Wrap it in an `async function`
  that runs its internal `parallel`/`pipeline` and returns the validated object (see §2.11). This
  is how you get arbitrarily deep graphs without arbitrarily complex top-level code.
- **Edge = a data dependency.** Sequential edge → put the consumer in a later `pipeline` stage or
  `await` it after the producer. Parallel (no edge) → same `parallel([...])` batch. **A
  modality-conditioned edge** feeds one node's *output* into a node working in a *different
  modality* — e.g. a visual node that receives the text node's verdict and checks pixels against
  it (see §2.12). That edge is where contradictions surface.
- **Feedback edge = a loop.** Route a later node's output back to an earlier stage and iterate
  until a stop condition (a quality bar, or **saturation** — K rounds with nothing new). Two
  pyramids in a feedback loop (produce → critique → improve → re-examine) is the saturation
  engine of §2.13.
- **Wire it, then sanity-check:** every produced artifact has an adversary (directive 2); every
  machine-read output has a schema (§1); independent nodes never share context (directive 1).

### 2.1 Byzantine 2+1 — the floor
**Shape:** 2 isolated workers → 1 arbiter. **When:** any single correctness-critical step.
```js
const drafts = await parallel([
  () => agent(spec, {label:'work:A', schema:S}),
  () => agent(spec, {label:'work:B', schema:S}),  // identical spec, different label only
])
const verdict = await agent(arbitratePrompt(drafts.filter(Boolean)), {schema:VERDICT})
```
Arbiter decision matrix: full agreement → apply (conf 90+); minor diffs → pick cleaner (80+);
structural → analyze+merge (60–85); fundamental → escalate (<40).

### 2.2 Triple-verified research (A+B+C)
**Shape:** 2 independent researchers (zero shared context) → 1 cross-reference verifier that
*manually investigates disagreements*. **When:** facts/predictions where only triple-verified data
should survive. Scale 3 → 6–9 → 12+ by widening the researcher pool.

### 2.3 Pyramid Byzantine (the workhorse)
**Shape:** N drafters → comparator/synthesizer → proportional verifiers → adversary → integrator.
**When:** hallucination-prone or high-stakes one-shots. Verifiers per cluster ≈ `floor(N/2)`.
Label outputs ✅ VERIFIED (unanimous) / ⚠️ CONTESTED (resolved disagreement) / ❌ STRIPPED
(confirmed fabrication). See the hardened build pattern in §4.

### 2.4 Committee review (N×M)
**Shape:** N reviewers × M rounds until a quality bar is met, each committee with distinct criteria.
**When:** quality iteration (papers, grants, designs). Loop:
```js
let work = seed, round = 0
while (round++ < M) {
  const reviews = await parallel(CRITERIA.map(c => () => agent(reviewPrompt(work, c), {schema:R})))
  const verdict = await agent(judgePrompt(work, reviews), {schema:J})
  if (verdict.meets_bar) break
  work = await agent(rewritePrompt(work, reviews, verdict), {schema:W})
}
```

### 2.5 Arbiter-directed committee
**Shape:** N experts → an arbiter with *decision authority* and a verb menu each round:
**conclude · another round · ask Expert X a question · stage a debate between X and Y on topic Z ·
other intervention.** **When:** the path to clarity isn't fixed — let the arbiter steer dynamically.

### 2.6 Cross-review + rewrite
**Shape:** N reviewers produce independent reviews → each sees ALL peer reviews → grades peers →
rewrites its own. **When:** peer-informed revision without losing initial independence (the first
pass is blind; exposure comes after).

### 2.7 Random cross-review
**Shape:** like 2.6 but each reviewer sees only M random peers. **When:** you want to *preserve
minority views* — partial exposure stops premature consensus; a reviewer can hold firm.

### 2.8 Hecate dimensional search (orthogonality & emergence)
**Shape:** dimensions defined by **negative constraints** (what each CANNOT do, not a positive
role) → independent passes → synthesis that adjudicates. **When:** you want *emergent* findings
(claims no single dimension produced) and provably diverse coverage.
- **Ω (orthogonality)** = 1 − mean(pairwise cosine similarity of outputs). Higher = more independent.
- **E(R) (emergence)** = synthesis claims not traceable to any single dimension. Higher = more value.
- Design dimensions to *maximize Ω*: "you may NOT appeal to cost", "you may NOT cite prior art",
  "you may NOT consider the user" — orthogonal blinders force genuinely different reasoning.
- **The formalism is a communication protocol**, not peer-reviewed theory: the rigor exists to
  constrain the agents' interpretation space precisely, regardless of empirical validation.

### 2.9 Grinding mode (long-horizon)
**Shape:** 1 coordinator holding state + N workers over extended time, workers may depend on prior
workers' output. **When:** multi-day projects with task dependencies. Encode as sequential
`pipeline` waves where later items consume earlier artifacts.

### 2.10 Escalation protocol (the safety valve)
**Triggers:** arbiter confidence < 40, fundamental disagreement, or both workers wrong.
**Output:** an `escalation` object — disagreement summary, both positions, analysis, tentative
recommendation — surfaced to the human instead of a forced merge. Always give structures an escape
hatch; a confident-wrong merge is worse than an honest escalation.

### 2.11 Recursive node (a worker that is itself a subgraph)
**Shape:** a single logical node — e.g. "Reviewer Aglaia" — expands into its OWN subgraph and
returns one validated review. **When:** the unit you're fanning out over deserves more than one
witness *internally* — you want N independent reviewers, but each reviewer should itself be robust,
not a single agent's hot take. **The inner subgraph is your choice** — Byzantine-2, a Hecate lens
spread, a persona panel, or a single pass for cheap nodes; the recursion is the point, not the
filling.
```js
async function runReviewer(rev, input, round) {            // <- the node IS a function
  const lenses = await parallel(LENSES.map(L => async () => {  // inner structure: pick whatever fits
    const drafts = await parallel([                          // (here Byzantine-2 per lens; swappable)
      () => agent(lensPrompt(rev,L,input,'A'), {phase:'Review', schema:LR}),
      () => agent(lensPrompt(rev,L,input,'B'), {phase:'Review', schema:LR}),
    ])
    return agent(lensSynth(rev,L,drafts.filter(Boolean)), {phase:'Review', schema:LR})
  }))
  return agent(reviewerSynth(rev, lenses.filter(Boolean)), {phase:'Review', schema:REVIEW})  // one node out
}
const reviews = (await parallel(REVIEWERS.map(r => () => runReviewer(r, input, 1)))).filter(Boolean)
```
The top level stays legible (a `parallel` over reviewers) while each "reviewer" hides a full
subgraph. Compose this to any depth; just return one schema-validated object per level.

### 2.12 Modality-conditioned stage (cross-modal contradiction hunting)
**Shape:** a node working in modality B receives a node's verdict from modality A and is tasked to
*confirm or refute it against B's evidence*. The canonical case: a **VISUAL** committee that reads
the rendered page images AND the **textual** review of the same reviewer, hunting where the words
and the pixels disagree. **When:** text alone is blind to surface truth — a title at the bottom of
the page, an `[insert figure here]` placeholder, a figure whose bars contradict its caption, an
unrendered equation. The text review can score 68% while the page is visibly unfinished; only the
cross-modal edge catches it.
```js
const text   = await agent(reviewerSynth(...), {phase:'Review', schema:TEXTREVIEW})
const visual = await parallel(VISUAL_LENSES.map(L => () =>
  agent(visualPrompt(L, manifest.image_paths, text), {phase:'Visual', schema:VISUAL})))  // sees text + pixels
const adv    = await agent(visualAdversary(visual), {phase:'Visual', schema:ADVERSARY})  // inverted bias: obvious defects default HOLD
return agent(reconcile(text, visual, adv), {schema:RECONCILED})   // pixels win on contradiction
```
Key inversion: the visual adversary defaults **holds=true** for obvious surface defects (humans DO
penalise them) and **holds=false** for taste. Same byzantine machinery, flipped prior.

### 2.13 Saturation loop (two pyramids in feedback until dry)
**Shape:** a PRODUCE pyramid and an IMPROVE pyramid wired in a feedback loop — produce a verdict →
improve the artifact to clear it → re-ingest the improved artifact → repeat. **Stop on
saturation:** K consecutive rounds with no *new* findings (dedup against a `seen` set), no gate
fired, and the improver's adversary holding. **When:** "review and harden X until it stops getting
better" — and X is any artifact, not just a paper.
```js
const seen = new Set(); let dry = 0, manifest = await agent(ingest(ARTIFACT), {schema:MANIFEST})
for (let round = 1; round <= MAX; round++) {
  const reviews = (await parallel(REVIEWERS.map(r => () => runReviewer(r, manifest, round)))).filter(Boolean)
  const panel   = await agent(panelSynth(reviews), {schema:PANEL})        // anti-averaging integrate
  const fresh   = panel.must_fix.filter(m => { const k = m.page+'|'+m.issue; return seen.has(k)?false:(seen.add(k),true) })
  if (!fresh.length && !panel.gate_applied && !panel.must_fix.length) { if (++dry >= 1) break } else dry = 0
  const fix = await parallel([() => agent(rewrite(manifest,panel,'A'),{schema:REWRITE}),
                              () => agent(rewrite(manifest,panel,'B'),{schema:REWRITE})])
  const chosen = await agent(rewriteArbiter(panel, fix.filter(Boolean)), {schema:VERDICT})
  manifest = await agent(ingest(chosen.new_artifact_path), {schema:MANIFEST})   // <- feedback edge
}
```
Full runnable version (recursive reviewers + modality-conditioned visual QA + this loop, all three
composed): [`examples/saturating-review-engine.workflow.js`](examples/saturating-review-engine.workflow.js).

---

## 3. Persona & model engineering (where real diversity comes from)

- **Rich personas (100+ attributes) beat "you are an expert in X".** Specify professional role +
  experience, background/mentors, demeanour (confidence, risk tolerance, contrarian tendency),
  nuances (blind spots, unusual expertise), quirks, and *acknowledged biases*. Surface variation
  ("be diverse") produces fake diversity; rich personas produce real disagreement.
- **Negative constraints > positive roles.** "Must NOT do X" is a harder boundary than "You ARE a Y."
  This is the Hecate insight and the single highest-leverage persona move.
- **Worker preamble types:** BUILDER / RESEARCHER / CREATIVE / INTEGRATOR — inject different
  behavioural DNA per role.
- **Model diversity** catches model-specific blindness: run the same persona across model tiers
  (`model:` on `agent()`). Two calls to the *same* model are one witness counted twice.
- **N×M → N aggregation:** N personas × M models = N×M outputs; each persona then synthesizes its
  own M versions (self-aggregation preserves persona coherence — don't let an external arbiter do it).
  Very high cost; reserve for maximum-diversity deliverables.

### 3.1 VERY human reviewers + the disqualifying-defect GATE (for any review graph)
Real human reviewers are **annoyed, anchored, and biased** — and that bias *catches things a polite
"expert reviewer" waves through.* Two moves make a review graph behave like real humans:
- **Give each reviewer a pet peeve + an ACKNOWLEDGED bias**, and let it anchor. "A desk editor who
  anchors their whole judgement to the first ugly thing and does not recover." "A figure-hawk who
  reads every axis label before a word of prose and treats an `[insert figure here]` as near-fatal."
  Stated bias is a feature: it makes the reviewer score the way a human actually would.
- **Encode a hard SCORING GATE, don't average.** The failure mode to kill: a report with an obvious
  `[insert figure here]`, a missing/broken figure, a title in the wrong place, or unrendered
  `\ref`/`??` getting **68%** because strong substance bought back a soft deduction. A human doesn't
  do that — an obvious disqualifying defect *caps* the score (e.g. ≤40) and attaches the flag *"at
  best the author forgot to include material; at worst this was produced by an automated process that
  never inspected its own output."* Make the gate a non-negotiable instruction in the synthesis +
  panel prompts, and seed it with a **deterministic pre-scan** (grep for placeholder patterns) so the
  defect's *existence* is ground truth and only its *weight* is judged. Substance must not buy back
  the cap. See `GATE_DOCTRINE` in the worked example.

---

## 4. A hardened build-work pattern (code via pyramid → applyable diffs)

Use this pattern for an "implement or migrate N items" task where independent implementation and
adversarial review justify the overhead.

```js
const SOURCE = '/tmp/proj-source'  // disposable clone of the live repo (directive 7)
// ITEMS: [{id, title, files /* single-owner scope */, brief /* NO raw backticks */}]

const results = await pipeline(ITEMS,
  // Stage 1 — two isolated implementers race the same item in their own /tmp clones.
  (item) => parallel([
    () => agent(implPrompt(item,'A'), {label:`impl:${item.id}:A`, phase:'Build', schema:IMPL, agentType:'general-purpose'}),
    () => agent(implPrompt(item,'B'), {label:`impl:${item.id}:B`, phase:'Build', schema:IMPL, agentType:'general-purpose'}),
  ]).then(impls => ({item, impls: impls.filter(Boolean)})),
  // Stage 2 — Oracle reads both diffs, picks the authoritative one, does gap analysis.
  (p) => agent(verifyPrompt(p.item, p.impls), {label:`verify:${p.item.id}`, phase:'Verify', schema:VERDICT})
           .then(v => ({item:p.item, verdict:v})),
  // Stage 3 — Cassandra tries to REFUTE the chosen diff (default holds=false if unsure).
  (p) => agent(refutePrompt(p.item, p.verdict), {label:`adversary:${p.item.id}`, phase:'Verify', schema:ADVERSARY})
           .then(a => ({id:p.item.id, diff:p.verdict.diff, gaps:p.verdict.gaps, adversary:a})),
)
return results.filter(Boolean)
```
**Implementer brief must:** `rm -rf $WORKDIR && git clone -q $SOURCE $WORKDIR && cd $WORKDIR`; a
SANDBOX RULE forbidding any path outside `$WORKDIR`; touch only `item.files`; set up a venv + run
the full suite; return `git add -A && git diff --cached`. **Schemas:** IMPL `{variant,summary,diff,
tests_passed,test_tail,files_touched}`; VERDICT `{chosen_variant,diff,rationale,gaps,confidence}`;
ADVERSARY `{holds,problems,severity}`.
**Integration (you, on the live tree):** move strays aside → `git apply --recount` each chosen diff
→ run suite → **read the adversary verdicts and fix any holds=false before committing** → dogfood
any linters → commit per-item
provenance → push.

---

## 5. Selection guide

| Structure | Agents | Best for | Overhead |
|---|---|---|---|
| Single agent | 1 | trivial / deterministic | none |
| Byzantine 2+1 | 3 | correctness-critical step | low |
| Triple-verified | 3→12+ | research, predictions | low |
| Pyramid Byzantine | 5–15+ | hallucination-prone one-shots, builds | medium |
| Committee N×M | N×M | quality iteration | medium |
| Arbiter-directed | N+1 | open-ended path to clarity | medium |
| Cross-review | N×2 | peer-informed revision | medium |
| Random cross-review | N×2 | preserving minority views | medium |
| Hecate dimensional | N+Σ | emergence, orthogonality | high |
| Recursive node (§2.11) | node×subgraph | robust per-witness (reviewer = pyramid) | high |
| Modality-conditioned (§2.12) | +visual | text-vs-pixel contradiction hunting | medium |
| Saturation loop (§2.13) | two pyramids ×R | harden any artifact until dry | high |
| Grinding | N+1 | multi-day, dependent tasks | high |
| N×M aggregation | N×M | maximum diversity | very high |

**Scale verification to bits-at-risk**, not by reflex: a zero-entropy step gets one agent; a
high-stakes one gets the full pyramid. Spend tracks uncertainty.

---

## 6. Pre-flight checklist (run before launching any wave)

- [ ] Right structure for the task's stakes/uncertainty? (don't 5+1 a lookup; don't single-agent a migration)
- [ ] Items have **disjoint single-owner file scopes**? (or serialized across waves)
- [ ] Code-producing? → disposable `/tmp` source clone made; live path redacted; recoverable backup verified
- [ ] Every produced artifact has an **adversary/refutation** stage
- [ ] Schemas defined for every machine-processed output
- [ ] Briefs contain **no raw backticks**; script is plain JS
- [ ] Personas use **negative constraints** + rich attributes where diversity matters
- [ ] An **escalation** path exists for low-confidence/fundamental-disagreement
- [ ] Integration plan: how you'll apply (`--recount`), verify (`.git` + suite), and act on adversary holds

---

## 7. Meta-learnings (internalize these)

1. **Formal theory is a communication protocol.** Mathematical structure constrains AI interpretation
   and enables precise behavioural specification — independent of whether the theory is "true".
2. **Negative constraints > positive roles.** Harder boundaries, more orthogonal outputs.
3. **Redundancy catches errors** — agreement validates, disagreement flags investigation.
4. **Emergence requires orthogonality** — perspectives must be genuinely independent to find
   intersection patterns.
5. **Rich personas produce real diversity**; "you are an expert" produces theatre.
6. **Model diversity catches model-specific blindness.**
7. **Self-aggregation preserves persona coherence** — let the persona merge its own multi-model outputs.
8. **The adversary earns its keep** — it is the cheapest insurance against a plausible-but-wrong merge.
9. **The expensive failures are silent** — a diff that applies, tests that pass, and a defect that
   ships anyway. Adversarial refutation + dogfooding + reading the verdicts is how you catch them.

## Installation and upstream provenance

The upstream skill identifier is `agent-orchestra`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/agent-orchestra --skill agent-orchestra --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/agent-orchestra#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`298b9d216019`](https://github.com/AntreasAntoniou/agent-orchestra/tree/298b9d216019def03b075092fbacdd8bd7f858d4). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
