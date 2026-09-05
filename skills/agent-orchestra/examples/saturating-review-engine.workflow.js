// =============================================================================
// SATURATING REVIEW ENGINE — a worked custom graph (NOT paper-specific)
// =============================================================================
// A reusable demonstration that a "reviewer" is not one agent but a whole
// SUBGRAPH, that a visual stage can be CONDITIONED on the same reviewer's text
// verdict, and that two pyramids can run in a FEEDBACK LOOP until the artifact
// stops yielding new findings (saturation).
//
// The artifact under review is GENERIC: a paper, a slide deck, a README, a
// landing page, a design doc, a data report, a plan — anything that renders to
// (text + page/screen images). Swap REVIEWERS / DIMENSIONS / VISUAL_LENSES for
// your domain; the topology is the point, not the personas.
//
// Graph shape (read top-to-bottom; [* ] = recursive subgraph, ~> = feedback edge):
//
//   INGEST  ──► render(text + page images) + deterministic surface-defect scan
//     │
//     ├──►[*] REVIEWER PYRAMID  (one per persona, run in parallel)
//     │        └─ orthogonal lenses × Byzantine-2 → reviewer synthesis  ── textReview
//     │           (the inner structure is PLUGGABLE — see DIMENSIONS note below)
//     │              │
//     │              └──► VISUAL QA  (sees page images AND this reviewer's textReview)
//     │                     └─ N orthogonal lenses → adversary → fuse  ── reconciledReview
//     │                            (SURFACE-DEFECT GATE applied here)
//     │
//     ├──► PANEL INTEGRATION  (anti-averaging synth of all reconciledReviews) + adversary
//     │        └─ panelReview { must_fix[], gate, dissent }
//     │
//     └──► REWRITE PYRAMID  (mode:'fix')  N integrators → synth → adversary  ── newArtifact
//              │
//              ~> re-ingest newArtifact and loop ─────────────────────────────┐
//                 STOP when: K rounds with no new must_fix  AND  no surface    │
//                 defects remain  AND  rewrite adversary holds  (= SATURATION) ┘
//
// Launch:  Workflow({ scriptPath: ".../saturating-review-engine.workflow.js",
//                     args: { artifactPath: "/abs/path/to/thing", mode: "fix" } })
// =============================================================================

export const meta = {
  name: 'saturating-review-engine',
  description: 'Recursive human-reviewer graph: each reviewer is a pyramid+visual-QA subgraph; a rewrite pyramid improves the artifact; both loop until findings saturate. Generic artifact.',
  whenToUse: 'Reviewing/hardening any rendered artifact where obvious surface defects must hard-gate the score and the review must be verified, not vibes.',
  phases: [
    { title: 'Ingest' },
    { title: 'Review' },
    { title: 'Visual' },
    { title: 'Panel' },
    { title: 'Rewrite' },
  ],
}

// ---------------------------------------------------------------------------
// CONFIG — everything below the meta block is plain editable JS.
// ---------------------------------------------------------------------------
const ARTIFACT = args?.artifactPath || '/tmp/artifact-under-review'
const MODE = args?.mode || 'fix'            // 'fix' = improve the artifact; 'review' = stop at the panel review
const MAX_ROUNDS = args?.maxRounds || 4     // hard ceiling on the saturation loop
const DRY_STREAK_TO_STOP = args?.dryStreak || 1  // consecutive no-new-finding rounds that count as saturated

// VERY HUMAN reviewers — each anchored to a pet peeve and an ACKNOWLEDGED bias,
// because rich annoyed personas catch what a polite "expert reviewer" waves through.
// Generic across artifact types; edit for your domain.
const REVIEWERS = args?.reviewers || [
  {
    id: 'desk-editor',
    persona: 'A managing/desk editor of 20 years who has rejected thousands of submissions on first impression. You anchor your whole judgement to the first ugly thing you see and you do not recover. A placeholder, a title in the wrong place, a figure that says one thing and a caption that says another reads to you as contempt for the reader. ACKNOWLEDGED BIAS: you under-weight brilliant content if the packaging is sloppy, and you are proud of it because sloppy packaging predicts sloppy thinking.',
  },
  {
    id: 'figure-hawk',
    persona: 'An obsessive who reads every figure, caption, axis label and number before reading a word of prose. You treat an [insert figure here] / [TODO] / placeholder / low-res / mislabelled-axis / figure-number-mismatch as near-fatal: at best a student forgot to paste the figures, at worst the whole thing was produced by an automated process that never looked at its own output. ACKNOWLEDGED BIAS: you will tank an otherwise strong piece over a single broken figure, on purpose.',
  },
  {
    id: 'overclaim-skeptic',
    persona: 'A grumpy senior reviewer who assumes every strong claim is overclaimed until evidence is shown on the page. You hate hedge-words, undefended superlatives, and conclusions the body does not support. ACKNOWLEDGED BIAS: you read generously for modest claims and savagely for grand ones.',
  },
  {
    id: 'first-time-reader',
    persona: 'An intelligent but impatient reader from an adjacent field encountering this cold. You get annoyed by undefined jargon, things that assume context you do not have, broken cross-references (see Section ?), and structure that makes you hunt. ACKNOWLEDGED BIAS: if you are confused by paragraph two you assume the author is confused, and you say so.',
  },
]

// The inner structure of a reviewer is PLUGGABLE — this is ONE pattern of many.
// Here: orthogonal lenses by NEGATIVE CONSTRAINT (so presentation is never drowned
// out by substance). Equally valid swaps: a plain Byzantine-2 with no lenses, a
// rich persona panel, a single pass for cheap reviewers, or a different decomposition
// entirely. Pick what the artifact wants; nothing here mandates this particular split.
const DIMENSIONS = [
  { key: 'substance',    brief: 'Judge ONLY the ideas, argument, correctness and contribution. You MAY NOT comment on formatting, figures, typos, layout, or presentation — assume those are perfect.' },
  { key: 'presentation', brief: 'Judge ONLY surface and presentation: placeholders, figure/table integrity, captions, numbering, title placement, cross-references, typos, layout, rendering. You MAY NOT comment on whether the ideas are good — assume the ideas are brilliant. Flag every obvious defect a human would notice in three seconds.' },
  { key: 'rigor',        brief: 'Judge ONLY claims vs evidence: over/under-claiming, missing controls, unsupported numbers, statistical or logical gaps. You MAY NOT praise anything and MAY NOT discuss style or formatting.' },
  { key: 'positioning',  brief: 'Judge ONLY positioning vs the wider field: novelty, prior-art collisions, who already did this. You MAY NOT consider execution quality or presentation.' },
]

// Orthogonal VISUAL lenses for the text-conditioned visual QA stage.
const VISUAL_LENSES = [
  { key: 'finish-quality',  brief: 'Look ONLY for embarrassment tells in the rendered pixels: leaked placeholder/[insert ... here]/lorem/TODO text, broken or default-grey figures, misalignment, a title sitting at the BOTTOM of a page, inconsistent fonts/shades. You MAY NOT discuss the ideas. If the text review did not catch a tell you can SEE, that is your headline.' },
  { key: 'figure-truth',    brief: 'Look ONLY at whether each figure/table actually shows what its caption and the surrounding text CLAIM. Mismatched figure numbers, an axis that contradicts the caption, a figure referenced in text but absent on the page, a chart whose bars contradict the stated result. Cross-check the text review: where it asserts the figures are fine, prove or refute it from the pixels.' },
  { key: 'layout-integrity', brief: 'Look ONLY at page-level layout truth: overflow, clipped content, broken columns, orphaned headings, content cut off at margins, a page that looks unfinished. You MAY NOT discuss wording or ideas.' },
]

// ---------------------------------------------------------------------------
// THE SURFACE-DEFECT DOCTRINE (the user's core complaint, encoded as a GATE).
// Obvious disqualifying defects do NOT get averaged into a soft deduction; they
// CAP the score. A report with [insert figure here] cannot score 68%.
// ---------------------------------------------------------------------------
const GATE_DOCTRINE =
  'SCORING GATE (non-negotiable): if ANY obvious disqualifying defect is CONFIRMED on the page — ' +
  'a placeholder like [insert figure here] / [TODO] / lorem ipsum, a missing or broken figure that is ' +
  'referenced in the text, a title in the wrong place, an unrendered equation/citation (\\ref, ??), or a ' +
  'figure-number mismatch — the score is HARD-CAPPED at 40/100 regardless of how good the content is, and you ' +
  'MUST attach the flag: "at best the author forgot to include material; at worst this was produced by an ' +
  'automated process that never inspected its own output." Do not let strong substance buy back the cap.'

// ---------------------------------------------------------------------------
// SCHEMAS
// ---------------------------------------------------------------------------
const FINDING = { type: 'object', properties: {
  page: { type: 'string' }, issue: { type: 'string' }, severity: { type: 'string', enum: ['blocker','major','minor','nit'] }, evidence: { type: 'string' },
}, required: ['issue','severity','evidence'] }

const MANIFEST = { type: 'object', properties: {
  page_count: { type: 'number' },
  image_paths: { type: 'array', items: { type: 'string' } },
  text_path: { type: 'string' },
  surface_defects: { type: 'array', items: { type: 'object', properties: { page: { type: 'string' }, pattern: { type: 'string' }, snippet: { type: 'string' } }, required: ['pattern','snippet'] } },
  notes: { type: 'string' },
}, required: ['image_paths','surface_defects'] }

const DIMREVIEW = { type: 'object', properties: {
  dimension: { type: 'string' }, findings: { type: 'array', items: FINDING }, note: { type: 'string' },
}, required: ['dimension','findings'] }

const TEXTREVIEW = { type: 'object', properties: {
  reviewer_id: { type: 'string' }, score: { type: 'number' }, summary: { type: 'string' }, findings: { type: 'array', items: FINDING },
}, required: ['reviewer_id','score','findings'] }

const VISUAL = { type: 'object', properties: {
  reviewer_id: { type: 'string' },
  visual_findings: { type: 'array', items: { type: 'object', properties: {
    page: { type: 'string' }, issue: { type: 'string' }, severity: { type: 'string', enum: ['blocker','major','minor','nit'] }, evidence: { type: 'string' }, contradicts_text: { type: 'boolean' },
  }, required: ['issue','severity','evidence','contradicts_text'] } },
  surface_defects_confirmed: { type: 'array', items: { type: 'object', properties: { page: { type: 'string' }, type: { type: 'string' }, snippet: { type: 'string' } }, required: ['type','snippet'] } },
}, required: ['visual_findings','surface_defects_confirmed'] }

const ADVERSARY = { type: 'object', properties: {
  holds: { type: 'boolean' }, problems: { type: 'array', items: { type: 'string' } }, severity: { type: 'string', enum: ['none','low','medium','high'] },
}, required: ['holds','problems','severity'] }

const RECONCILED = { type: 'object', properties: {
  reviewer_id: { type: 'string' }, score: { type: 'number' }, gate_applied: { type: 'boolean' }, gate_reason: { type: 'string' },
  findings: { type: 'array', items: FINDING }, contradictions: { type: 'array', items: { type: 'string' } },
}, required: ['reviewer_id','score','gate_applied','findings'] }

const PANEL = { type: 'object', properties: {
  overall_score: { type: 'number' }, gate_applied: { type: 'boolean' },
  must_fix: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, page: { type: 'string' }, issue: { type: 'string' }, severity: { type: 'string' }, evidence: { type: 'string' } }, required: ['id','issue','severity'] } },
  strengths: { type: 'array', items: { type: 'string' } }, dissent: { type: 'array', items: { type: 'string' } }, stripped: { type: 'array', items: { type: 'string' } },
}, required: ['overall_score','must_fix'] }

const REWRITE = { type: 'object', properties: {
  variant: { type: 'string' }, summary: { type: 'string' }, addressed_ids: { type: 'array', items: { type: 'string' } },
  edits: { type: 'array', items: { type: 'object', properties: { where: { type: 'string' }, change: { type: 'string' } }, required: ['where','change'] } },
  new_artifact_path: { type: 'string' },
}, required: ['variant','addressed_ids','new_artifact_path'] }

const REWRITE_VERDICT = { type: 'object', properties: {
  chosen_variant: { type: 'string' }, rationale: { type: 'string' }, addressed_ids: { type: 'array', items: { type: 'string' } },
  regressions: { type: 'array', items: { type: 'string' } }, new_artifact_path: { type: 'string' }, confidence: { type: 'number' },
}, required: ['chosen_variant','addressed_ids','new_artifact_path','confidence'] }

// ---------------------------------------------------------------------------
// PROMPT BUILDERS  (keep all prose backtick-free — a raw backtick closes the brief)
// ---------------------------------------------------------------------------
const ingestPrompt = (path) => [
  'You are the INGEST node of a review graph. Render the artifact for both textual and VISUAL review.',
  'Artifact path: ' + path + ' (could be a PDF, .md/.html, .pptx/.key, an image set, or a URL — detect and adapt).',
  'Do ALL of this with bash and save outputs under a sibling _review_assets/ directory:',
  ' 1. Produce a plain-text extraction (pdftotext / pandoc -t plain / strip HTML) at text_path.',
  ' 2. Produce one PNG per page or screen (pdftoppm -png, or render md/html via a headless browser or pandoc+weasyprint, or screenshot the URL). Return their absolute paths in page order.',
  ' 3. Run a DETERMINISTIC surface-defect scan over the text with grep -nE for: \\[insert[^]]*here\\], \\[TODO\\], TKTK, lorem ipsum, \\?\\?, Figure \\?, Table \\?, \\\\ref|\\\\cite (unrendered LaTeX), citation needed, [object Object], undefined. Record every hit as {page, pattern, snippet}.',
  'Return the manifest. Do not review anything — just render and scan.',
].join('\n')

const dimPrompt = (rev, dim, manifest, variant) => [
  'You are reviewer "' + rev.id + '", dimension "' + dim.key + '", independent draft ' + variant + '.',
  'PERSONA: ' + rev.persona,
  'DIMENSION CONSTRAINT: ' + dim.brief,
  'Read the extracted text at ' + manifest.text_path + '. A deterministic pre-scan already flagged these surface defects (treat as ground truth, do not re-litigate their existence): ' + JSON.stringify(manifest.surface_defects),
  'List concrete findings with page, severity (blocker/major/minor/nit) and on-page evidence. Stay strictly inside your dimension constraint. Do not soften severity to be polite.',
].join('\n')

const dimSynthPrompt = (rev, dim, drafts) => [
  'You are reviewer "' + rev.id + '" consolidating two independent drafts for dimension "' + dim.key + '".',
  'PERSONA: ' + rev.persona,
  'Drafts: ' + JSON.stringify(drafts),
  'Keep every finding at least one draft is confident about; drop only the clearly wrong. Do not average severities — take the higher when the evidence supports it.',
].join('\n')

const reviewerSynthPrompt = (rev, dimReviews, manifest) => [
  'You are reviewer "' + rev.id + '". Fuse your per-dimension findings into ONE textual review with a 0-100 score.',
  'PERSONA: ' + rev.persona,
  GATE_DOCTRINE,
  'Per-dimension findings: ' + JSON.stringify(dimReviews),
  'Pre-scanned surface defects: ' + JSON.stringify(manifest.surface_defects),
  'Score as the HUMAN in your persona actually would — anchored, annoyed, gate-aware. Return reviewer_id, score, summary, findings.',
].join('\n')

const visualPrompt = (rev, lens, manifest, textReview) => [
  'You are a VISUAL reviewer for reviewer "' + rev.id + '", lens "' + lens.key + '". You can SEE the rendered pages.',
  'Use the Read tool on EACH of these page images: ' + JSON.stringify(manifest.image_paths),
  'LENS CONSTRAINT: ' + lens.brief,
  'CRITICAL — you also get this reviewer\'s TEXT review, and your job includes CROSS-CHECKING it against the pixels: ' + JSON.stringify(textReview),
  'Where the text review and the pixels DISAGREE (e.g. text gave a high score / called the figures fine, but a page literally shows a placeholder or a broken figure), report it with contradicts_text=true — those are your most valuable findings.',
  'Also list every surface defect you can confirm by eye. Return visual_findings and surface_defects_confirmed.',
].join('\n')

const visualAdversaryPrompt = (rev, visuals) => [
  'You are the ADVERSARY for reviewer "' + rev.id + '"\'s visual findings. Try to REFUTE each finding from the pixels.',
  'INVERTED BIAS for surface defects: a human DOES penalise obvious defects, so for placeholder/broken-figure/wrong-title-placement findings, default holds=true unless you can prove the defect is not actually on the page. For taste/aesthetic complaints, default holds=false unless backed by pixel evidence.',
  'Findings: ' + JSON.stringify(visuals),
  'Return holds (does the body of findings stand), problems (which specific ones are weak), severity.',
].join('\n')

const reconcilePrompt = (rev, textReview, visuals, adversary) => [
  'You are reviewer "' + rev.id + '" producing your FINAL reconciled review by fusing your text review with the verified visual findings.',
  'PERSONA: ' + rev.persona,
  GATE_DOCTRINE,
  'Text review: ' + JSON.stringify(textReview),
  'Verified visual findings: ' + JSON.stringify(visuals),
  'Adversary on the visual findings: ' + JSON.stringify(adversary),
  'Where pixels contradicted text, the PIXELS win. Apply the scoring gate if any disqualifying defect is confirmed. Return reviewer_id, score, gate_applied, gate_reason, findings (merged), contradictions.',
].join('\n')

const panelPrompt = (reconciled) => [
  'You are the PANEL INTEGRATOR. Synthesise all reviewers\' final reviews into one verdict.',
  'ANTI-AVERAGING: adjudicate disagreement — pick winners, PRESERVE dissent (do not smooth it away), STRIP any finding no reviewer can evidence. If ANY reviewer\'s gate fired, the panel gate fires and the overall_score is capped at 40.',
  'Reviews: ' + JSON.stringify(reconciled),
  'Produce overall_score, gate_applied, a deduplicated must_fix list (each with a stable id), strengths, dissent, stripped.',
].join('\n')

const rewritePrompt = (manifest, panel, variant) => [
  'You are a REWRITE integrator, independent variant ' + variant + '. Improve THE ARTIFACT to clear the panel must_fix list.',
  'Work on a disposable copy: cp the artifact and its sources to a fresh /tmp workdir, edit there, never touch the original path.',
  'Artifact text: ' + manifest.text_path + ' ; pages: ' + JSON.stringify(manifest.image_paths),
  'Must-fix list: ' + JSON.stringify(panel.must_fix),
  'Fix EVERY blocker and major — especially any surface defect / placeholder / broken figure (those are the cheap, score-capping ones). Re-render the artifact after editing and return new_artifact_path pointing at the rebuilt file.',
  'Return variant, summary, addressed_ids, edits, new_artifact_path.',
].join('\n')

const rewriteVerdictPrompt = (panel, variants) => [
  'You are the REWRITE ARBITER. Two integrators each produced an improved artifact. Pick the one that fixes the most must_fix items with the fewest regressions, verify it actually re-renders, and report.',
  'Must-fix list: ' + JSON.stringify(panel.must_fix),
  'Variants: ' + JSON.stringify(variants),
  'Return chosen_variant, rationale, addressed_ids, regressions, new_artifact_path, confidence.',
].join('\n')

// ---------------------------------------------------------------------------
// ONE REVIEWER = ONE SUBGRAPH  (recursion: a node that is itself a pyramid)
// ---------------------------------------------------------------------------
async function runReviewer(rev, manifest, round) {
  const ph = (p) => p + ' R' + round
  // Inner structure (pluggable): orthogonal lenses × Byzantine-2, all lenses concurrent.
  const dimReviews = await parallel(DIMENSIONS.map(dim => async () => {
    const drafts = await parallel([
      () => agent(dimPrompt(rev, dim, manifest, 'A'), { label: rev.id + ':' + dim.key + ':A', phase: ph('Review'), schema: DIMREVIEW }),
      () => agent(dimPrompt(rev, dim, manifest, 'B'), { label: rev.id + ':' + dim.key + ':B', phase: ph('Review'), schema: DIMREVIEW }),
    ])
    return agent(dimSynthPrompt(rev, dim, drafts.filter(Boolean)), { label: rev.id + ':' + dim.key + ':synth', phase: ph('Review'), schema: DIMREVIEW })
  }))
  const textReview = await agent(reviewerSynthPrompt(rev, dimReviews.filter(Boolean), manifest),
    { label: rev.id + ':text', phase: ph('Review'), schema: TEXTREVIEW })

  // VISUAL QA conditioned on this reviewer's own text verdict, then adversary-verified.
  const visuals = await parallel(VISUAL_LENSES.map(lens => () =>
    agent(visualPrompt(rev, lens, manifest, textReview), { label: rev.id + ':vis:' + lens.key, phase: ph('Visual'), schema: VISUAL })))
  const mergedVisual = visuals.filter(Boolean)
  const adversary = await agent(visualAdversaryPrompt(rev, mergedVisual), { label: rev.id + ':vis-adv', phase: ph('Visual'), schema: ADVERSARY })

  return agent(reconcilePrompt(rev, textReview, mergedVisual, adversary),
    { label: rev.id + ':reconciled', phase: ph('Visual'), schema: RECONCILED })
}

// ---------------------------------------------------------------------------
// THE SATURATION LOOP — two pyramids in feedback until the artifact runs dry.
// ---------------------------------------------------------------------------
let manifest = await agent(ingestPrompt(ARTIFACT), { label: 'ingest', phase: 'Ingest', schema: MANIFEST })
const seen = new Set()
const history = []
let dryStreak = 0

for (let round = 1; round <= MAX_ROUNDS; round++) {
  phase('Review')
  log('Round ' + round + ' — ' + REVIEWERS.length + ' reviewer subgraphs over ' + (manifest.image_paths || []).length + ' pages')

  // Each reviewer is a full subgraph; run them in parallel.
  const reconciled = (await parallel(REVIEWERS.map(rev => () => runReviewer(rev, manifest, round)))).filter(Boolean)

  phase('Panel')
  const panel = await agent(panelPrompt(reconciled), { label: 'panel:R' + round, phase: 'Panel', schema: PANEL })

  // Saturation accounting — count must_fix items not seen in a prior round.
  const fresh = panel.must_fix.filter(m => { const k = (m.page || '') + '|' + m.issue; if (seen.has(k)) return false; seen.add(k); return true })
  log('Round ' + round + ': score ' + panel.overall_score + (panel.gate_applied ? ' (GATE FIRED)' : '') + ' — ' + fresh.length + ' new must-fix, ' + panel.must_fix.length + ' total')
  history.push({ round, score: panel.overall_score, gate: panel.gate_applied, new_findings: fresh.length, total_findings: panel.must_fix.length })

  if (MODE === 'review') return { mode: 'review', panel, history }

  // SATURATED? no new findings, no gate, nothing left to fix.
  if (fresh.length === 0 && !panel.gate_applied && panel.must_fix.length === 0) {
    dryStreak++
    if (dryStreak >= DRY_STREAK_TO_STOP) { log('SATURATED after round ' + round); return { mode: 'fix', final_manifest: manifest, panel, history, saturated: true } }
  } else { dryStreak = 0 }
  if (round === MAX_ROUNDS) { log('Hit MAX_ROUNDS without full saturation'); return { mode: 'fix', final_manifest: manifest, panel, history, saturated: false } }

  // REWRITE PYRAMID — two integrators race to fix the artifact, arbiter picks.
  phase('Rewrite')
  const variants = (await parallel([
    () => agent(rewritePrompt(manifest, panel, 'A'), { label: 'rewrite:A:R' + round, phase: 'Rewrite', schema: REWRITE, agentType: 'general-purpose' }),
    () => agent(rewritePrompt(manifest, panel, 'B'), { label: 'rewrite:B:R' + round, phase: 'Rewrite', schema: REWRITE, agentType: 'general-purpose' }),
  ])).filter(Boolean)
  const chosen = await agent(rewriteVerdictPrompt(panel, variants), { label: 'rewrite:arbiter:R' + round, phase: 'Rewrite', schema: REWRITE_VERDICT })

  // Feedback edge: re-ingest the improved artifact and loop.
  manifest = await agent(ingestPrompt(chosen.new_artifact_path), { label: 'ingest:R' + (round + 1), phase: 'Ingest', schema: MANIFEST })
}
