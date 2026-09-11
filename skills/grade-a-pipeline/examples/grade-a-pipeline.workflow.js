// =============================================================================
// GRADE-A-PIPELINE — a test-sandwiched, map-anchored, multi-agent SWE pipeline
// =============================================================================
// Reads the whole codebase, builds a structured MAP (files/funcs/classes/...),
// injects that MAP into every working agent, decomposes the requested work into
// a DEPENDENCY GRAPH (parallel where independent, serial where dependent), and
// drives a proper SWE pipeline whose every wave is SANDWICHED BETWEEN TESTS of
// all types (baseline -> per-wave regression -> full battery), ending in an
// A**** RUBRIC GATE that hard-caps the grade on any disqualifying defect.
//
// IN-REPO, NO /tmp: all work happens INSIDE the target repo via git WORKTREES.
// Bootstrap opens an integration branch + worktree; every implementer gets its
// OWN branch + worktree (gap/<run>/task-<id>-<variant>) under
// <repo>/.gap-worktrees/<run>/; the integrator commits accepted changes onto the
// integration branch, TAGS each wave, and (optionally) pushes to origin. Because
// worktrees share the repo's ref store, every agent's branch is a real ref in
// the live repo the moment it commits — nothing is cloned to /tmp. Worktrees are
// removed at the end; branches and tags persist for you to diff and merge.
//
// Topology (read top-to-bottom; [* ] = subgraph, ~> = feedback edge):
//
//   BOOTSTRAP  ──► integration branch + worktree IN-REPO + detect commands
//     │
//   CARTOGRAPHY [*] ──► N readers over file shards ──► synth ──► MAP.md (committed + at repo root)
//     │                                                 └─ MAP string injected downstream
//   PLAN [*]  ──► 2 isolated planners ──► arbiter ──► task DAG (single-owner file scopes)
//     │
//   BASELINE  ──► run existing full suite (read-only worktree)  ── bottom slice of the sandwich
//     │
//   for each WAVE (topo-sorted, file-disjoint batches):
//     BUILD [*] ─ per task: 2 TDD implementers, EACH IN ITS OWN WORKTREE+BRANCH ──► verify ──► adversary
//        │       (each agent: worktree off integration → commit → push? → remove worktree, branch stays)
//        INTEGRATE+REGRESS ─ commit accepted diffs onto integration branch, run FULL suite,
//        │                   tag wave, push checkpoint to origin (checkpoint as we go)
//        │                   gate: a wave that reddens the suite blocks the next wave
//   TEST BATTERY ──► unit · integration · e2e · property · lint/type · security  (top slice)
//     │
//   REVIEW/HARDEN [*] ─ code-review pyramid + adversary; harden commits+tags on integration branch
//     │
//   A**** GRADE GATE ─ rubric panel + deterministic defect pre-scan; defect ⇒ hard cap
//     │
//   CLEANUP ─ remove worktrees (branches + tags persist) ──► RETURN integration branch, tags, grade
//
// Launch:
//   Workflow({ scriptPath: ".../grade-a-pipeline.workflow.js",
//              args: { repoPath: "/abs/path/to/repo",
//                      request: "what to build/fix/refactor",
//                      maxWaves: 8, gradeBar: "A****",
//                      push: true, pushAgentBranches: true } })
// =============================================================================

export const meta = {
  name: 'grade-a-pipeline',
  description: 'Map the codebase, decompose work into a parallel/serial DAG, and run a test-sandwiched multi-agent SWE pipeline (baseline -> per-wave regression -> full battery) ending in an A**** rubric gate. Works in-repo via git worktrees; never /tmp.',
  whenToUse: 'Building/fixing/refactoring real software where you want maximum parallelism, regression safety between every wave, in-repo branch tracking, and a hard quality gate rather than vibes.',
  phases: [
    { title: 'Bootstrap' },
    { title: 'Cartography' },
    { title: 'Plan' },
    { title: 'Baseline' },
    { title: 'Build' },
    { title: 'Integrate' },
    { title: 'Battery' },
    { title: 'Review' },
    { title: 'Grade' },
  ],
}

// ---------------------------------------------------------------------------
// CONFIG
// ---------------------------------------------------------------------------
const REPO = args?.repoPath || '.'   // the TARGET repo (defaults to the current repo) — all work happens inside it
const REQUEST = args?.request || 'Harden the codebase: fix obvious bugs, add missing tests, tidy.'
const MAX_WAVES = args?.maxWaves || 8
const GRADE_BAR = args?.gradeBar || 'A****'
const MAX_REVIEW_ROUNDS = args?.maxReviewRounds || 3
const SHARD_SIZE = args?.shardSize || 40        // files per cartographer
const MAX_CARTOGRAPHERS = args?.maxCartographers || 16

// --- Git tracking / checkpointing (everything already lands locally in REPO; these govern REMOTE pushes) ---
const PUSH = args?.push === true                              // remote mutation is explicit opt-in
const PUSH_AGENT_BRANCHES = args?.pushAgentBranches === true  // remote mutation is explicit opt-in

// A**** RUBRIC — the explicit definition the grade gate scores against.
const RUBRIC =
  GRADE_BAR + ' software means ALL of: (1) the requested work is COMPLETE and does what was asked; ' +
  '(2) the FULL test suite is green and meaningfully covers the change (no vacuous/always-pass tests, ' +
  'no skipped/xfail hiding failures); (3) tests of every relevant type exist — unit, integration, and ' +
  'end-to-end/contract where applicable, plus property/edge cases for non-trivial logic; (4) lint, ' +
  'type-check, and a security scan are clean; (5) no dead code, no TODO/FIXME left in the change, no ' +
  'leaked secrets, no debug prints; (6) the diff is minimal, readable, and matches surrounding style.';

// DEFECT DOCTRINE — disqualifying defects CAP the grade; substance cannot buy them back.
const GATE_DOCTRINE =
  'GRADING GATE (non-negotiable): if ANY disqualifying defect is CONFIRMED — a failing/red test, a ' +
  'test that is skipped/xfail/commented-out to dodge a failure, a vacuous always-pass test, a left-in ' +
  'TODO/FIXME/HACK/XXX or debug print in the change, a leaked secret, a lint/type/security failure, or ' +
  'requested work left incomplete — the grade is HARD-CAPPED at C regardless of how strong the rest is, ' +
  'and you MUST attach the flag explaining which defect fired. Do not average a defect into a soft deduction.';

// ---------------------------------------------------------------------------
// SCHEMAS
// ---------------------------------------------------------------------------
const SYMBOL = { type: 'object', properties: {
  kind: { type: 'string' }, name: { type: 'string' }, signature: { type: 'string' }, line: { type: 'number' },
}, required: ['kind', 'name'] }

const FILEMAP = { type: 'object', properties: {
  path: { type: 'string' }, language: { type: 'string' }, role: { type: 'string' },
  symbols: { type: 'array', items: SYMBOL }, depends_on: { type: 'array', items: { type: 'string' } },
}, required: ['path', 'role'] }

const BOOTSTRAP = { type: 'object', properties: {
  ok: { type: 'boolean' }, files: { type: 'array', items: { type: 'string' } },
  test_command: { type: 'string' }, build_command: { type: 'string' }, lint_command: { type: 'string' },
  language_summary: { type: 'string' }, notes: { type: 'string' },
  run_id: { type: 'string' }, base_branch: { type: 'string' }, integration_branch: { type: 'string' },
  repo_is_git: { type: 'boolean' }, origin_url: { type: 'string' },
  // Greenfield signal: how much real code exists vs a repo that is empty / docs-only / scaffold-only.
  // Drives whether the pipeline treats the run as BUILD-from-target (greenfield) or MODIFY-existing (brownfield).
  code_file_count: { type: 'number' }, total_file_count: { type: 'number' }, is_greenfield: { type: 'boolean' },
}, required: ['ok', 'files', 'test_command', 'run_id', 'integration_branch'] }

const SHARDMAP = { type: 'object', properties: {
  file_maps: { type: 'array', items: FILEMAP },
}, required: ['file_maps'] }

const MAP_SYNTH = { type: 'object', properties: {
  map_markdown: { type: 'string' }, wrote_map_file: { type: 'boolean' },
  entry_points: { type: 'array', items: { type: 'string' } },
  architecture_summary: { type: 'string' },
}, required: ['map_markdown', 'architecture_summary'] }

const TASK = { type: 'object', properties: {
  id: { type: 'string' }, title: { type: 'string' }, brief: { type: 'string' },
  files: { type: 'array', items: { type: 'string' } },
  deps: { type: 'array', items: { type: 'string' } },
  test_types: { type: 'array', items: { type: 'string' } },
}, required: ['id', 'title', 'brief', 'files', 'deps'] }

const PLAN = { type: 'object', properties: {
  tasks: { type: 'array', items: TASK }, rationale: { type: 'string' },
}, required: ['tasks'] }

const SUITE = { type: 'object', properties: {
  passed: { type: 'boolean' }, total: { type: 'number' }, failed: { type: 'number' },
  summary: { type: 'string' }, tail: { type: 'string' },
}, required: ['passed', 'summary'] }

const IMPL = { type: 'object', properties: {
  variant: { type: 'string' }, summary: { type: 'string' }, diff: { type: 'string' },
  branch: { type: 'string' }, pushed: { type: 'boolean' }, commit: { type: 'string' },
  tests_added: { type: 'array', items: { type: 'string' } }, tests_passed: { type: 'boolean' },
  test_tail: { type: 'string' }, files_touched: { type: 'array', items: { type: 'string' } },
}, required: ['variant', 'summary', 'diff', 'tests_passed'] }

const VERDICT = { type: 'object', properties: {
  chosen_variant: { type: 'string' }, diff: { type: 'string' }, rationale: { type: 'string' },
  gaps: { type: 'array', items: { type: 'string' } }, confidence: { type: 'number' },
}, required: ['chosen_variant', 'diff', 'confidence'] }

const ADVERSARY = { type: 'object', properties: {
  holds: { type: 'boolean' }, problems: { type: 'array', items: { type: 'string' } }, severity: { type: 'string' },
}, required: ['holds', 'problems'] }

const INTEGRATE = { type: 'object', properties: {
  applied: { type: 'array', items: { type: 'string' } }, rejected: { type: 'array', items: { type: 'string' } },
  suite_passed: { type: 'boolean' }, suite_tail: { type: 'string' }, notes: { type: 'string' },
  branch: { type: 'string' }, tag: { type: 'string' }, head_commit: { type: 'string' },
  pushed_refs: { type: 'array', items: { type: 'string' } }, push_errors: { type: 'array', items: { type: 'string' } },
}, required: ['applied', 'suite_passed'] }

const BATTERY = { type: 'object', properties: {
  kind: { type: 'string' }, passed: { type: 'boolean' }, findings: { type: 'array', items: { type: 'string' } }, tail: { type: 'string' },
}, required: ['kind', 'passed'] }

const REVIEW = { type: 'object', properties: {
  findings: { type: 'array', items: { type: 'object', properties: {
    file: { type: 'string' }, issue: { type: 'string' }, severity: { type: 'string' }, fix: { type: 'string' },
  }, required: ['issue', 'severity'] } },
}, required: ['findings'] }

const GRADE = { type: 'object', properties: {
  grade: { type: 'string' }, meets_bar: { type: 'boolean' }, gate_fired: { type: 'boolean' },
  gate_reason: { type: 'string' }, blockers: { type: 'array', items: { type: 'string' } },
  strengths: { type: 'array', items: { type: 'string' } }, rationale: { type: 'string' },
}, required: ['grade', 'meets_bar', 'gate_fired'] }

// ---------------------------------------------------------------------------
// MUTABLE GIT STATE — assigned after bootstrap, read by the prompt builders.
// ---------------------------------------------------------------------------
let INTEGRATION_BRANCH = 'gap/run/integration'   // the running checkpoint branch (checked out in INTEGRATION_WT)
let BASE_BRANCH = 'main'                          // what the integration branch forked from
let BRANCH_PREFIX = 'gap/run'                     // namespace for all run branches/tags
let WT_ROOT = REPO + '/.gap-worktrees/run'        // all worktrees for this run live here (inside the repo)
let INTEGRATION_WT = WT_ROOT + '/integration'     // the persistent worktree holding the integration branch
let ORIGIN_URL = ''                               // the repo's 'origin' remote (empty if none)
let HAS_ORIGIN = false
let REPO_IS_GIT = true
const safeId = (id) => String(id).replace(/[^A-Za-z0-9_.-]/g, '-')
const agentBranch = (id, v) => BRANCH_PREFIX + '/task-' + safeId(id) + '-' + v
const agentWtName = (id, v) => 'task-' + safeId(id) + '-' + v
const wtPath = (name) => WT_ROOT + '/' + name
const waveTag = (n) => BRANCH_PREFIX + '/wave-' + n

// ---------------------------------------------------------------------------
// WORKTREE PREAMBLE for READ-ONLY testers (baseline/battery): a detached
// checkout of the current integration state, inside the repo, cleaned up after.
// ---------------------------------------------------------------------------
const READ_WT = (name) =>
  'WORKTREE RULES (absolute): operate ONLY inside your own worktree. Create it now — a read-only checkout at the ' +
  'current integration state, INSIDE the repo (never /tmp):\n' +
  '  git -C ' + REPO + ' worktree add -f --detach ' + wtPath(name) + ' ' + INTEGRATION_BRANCH + ' && cd ' + wtPath(name) + '\n' +
  '  (if "worktree add" fails on a lock, wait 2s and retry once.)\n' +
  'You MUST NOT touch anything outside ' + wtPath(name) + ' — not the base branch, not other worktrees, not .git internals. ' +
  'Set up a venv/deps as the project requires. When finished, REMOVE your worktree: ' +
  'git -C ' + REPO + ' worktree remove --force ' + wtPath(name) + '.';

const mapBlock = (MAP) => '\n\n===== CODEBASE MAP (authoritative; do not re-derive) =====\n' + MAP + '\n===== END MAP =====\n';
// Build vs modify framing, set from the bootstrap greenfield signal. Injected into the planners so a sparse/docs-only
// repo is treated as "build the target" instead of "reconcile what exists".
let MODE = 'brownfield';
const modeBlock = () => MODE === 'greenfield'
  ? '\n===== MODE: GREENFIELD (BUILD FROM TARGET) =====\n' +
    'This repo is empty, docs-only, or a thin scaffold. There is little or no existing code to modify. Your job is to ' +
    'BUILD the system the request describes. Treat any existing spec/design/README as the SOURCE of the target end-state, ' +
    'never as the deliverable to edit. The bulk of your tasks CREATE net-new source files and their tests.\n' +
    '===== END MODE =====\n'
  : '\n===== MODE: BROWNFIELD (MODIFY EXISTING) =====\n' +
    'A real codebase exists. Plan the delta the request asks for; reuse and extend existing modules; still create net-new ' +
    'files where the request needs them.\n===== END MODE =====\n';

// ---------------------------------------------------------------------------
// PROMPT BUILDERS  (no raw backtick characters inside any brief)
// ---------------------------------------------------------------------------
const bootstrapPrompt = () =>
  'You are the BOOTSTRAP scout for an SWE pipeline. The TARGET repo is at ' + REPO + '. We work INSIDE this repo using ' +
  'git WORKTREES — never /tmp, never a separate clone. Make NO commits to the base branch and do not push.\n' +
  '1) RUN_ID = output of: date +%Y%m%d-%H%M%S (a sortable timestamp). Return it as run_id.\n' +
  '2) If ' + REPO + ' is NOT a git repo (git -C ' + REPO + ' rev-parse --is-inside-work-tree fails): ' +
  '   git -C ' + REPO + ' init && git -C ' + REPO + ' add -A && git -C ' + REPO + ' commit -m "gap: initial commit" — note this loudly in notes. Set repo_is_git true after.\n' +
  '3) base_branch = git -C ' + REPO + ' branch --show-current (fall back to main). ' +
  '   origin_url = git -C ' + REPO + ' remote get-url origin 2>/dev/null (empty string if there is no origin).\n' +
  '4) Keep the pipeline out of the user status: ensure the line ".gap-worktrees/" is in ' + REPO + '/.git/info/exclude (append if missing).\n' +
  '5) Create the INTEGRATION BRANCH and its worktree off the base, at the EXACT path ' + REPO + '/.gap-worktrees/RUN_ID/integration ' +
  '   (substitute the real RUN_ID):\n' +
  '     git -C ' + REPO + ' worktree add -b gap/RUN_ID/integration ' + REPO + '/.gap-worktrees/RUN_ID/integration <base_branch>\n' +
  '   Return integration_branch=gap/RUN_ID/integration. Name it EXACTLY that so per-agent branches gap/RUN_ID/task-* never path-collide with it.\n' +
  '6) files[] = git -C ' + REPO + ' ls-files (tracked source files; this naturally excludes the worktrees and build output).\n' +
  '7) Detect the exact commands to TEST, BUILD, and LINT/TYPE-CHECK this project (read package.json / pyproject / Makefile / etc). ' +
  '   Prefer the real suite command (pytest, npm test, go test, cargo test, ...). If none exists, say so in notes.\n' +
  '8) GREENFIELD SIGNAL — classify the repo so the planner knows whether it is BUILDING or MODIFYING. Count real code/source ' +
  '   files vs docs/config: code_file_count = files that are actual program source (exclude .md/.txt/.rst docs, LICENSE, ' +
  '   .gitignore, bare config). total_file_count = all tracked files. Set is_greenfield=true when the repo is empty, docs-only, ' +
  '   or a thin scaffold (rule of thumb: code_file_count <= 3, OR the request describes a system far larger than what exists). ' +
  '   When true, the work is to BUILD the target described in the request, NOT to reconcile the few existing files.\n' +
  'Return BOOTSTRAP.';

const cartographerPrompt = (shard, idx) =>
  'You are CARTOGRAPHER ' + idx + '. Read ONLY these files inside ' + INTEGRATION_WT + ' (a clean checkout of the repo). Do NOT modify anything.\n' +
  'Files (relative to that worktree):\n' + shard.map(f => '  - ' + f).join('\n') + '\n\n' +
  'For each file return: path, language, one-line role, and its top-level SYMBOLS (functions, classes, methods, ' +
  'exported constants, routes/endpoints, CLI commands) with kind+name+signature+line, plus the modules it depends on. ' +
  'Be precise and complete; this map is injected into every downstream worker. Return SHARDMAP.';

const mapSynthPrompt = (fileMaps) =>
  'You are the CARTOGRAPHY SYNTHESIZER. Merge these per-file maps into one coherent MAP.md for the repo.\n' +
  'Input file maps (JSON): ' + JSON.stringify(fileMaps).slice(0, 120000) + '\n\n' +
  (MODE === 'greenfield'
    ? 'NOTE — this is a GREENFIELD run: the files below are all that exist so far (likely just specs/scaffold). The MAP ' +
      'documents the CURRENT state truthfully, but MUST open with a one-line banner "> STATE: greenfield — the target ' +
      'system described in the request does not exist yet; the plan BUILDS it." Then, if a design/spec file is present, ' +
      'add a short "## Target architecture (to build)" section summarising the module tree the request/spec calls for, ' +
      'so downstream planners build toward it rather than editing the existing files. Do NOT invent detail beyond the spec.\n\n'
    : '') +
  'Produce map_markdown: a clean MAP.md with sections — Overview/architecture, Entry points, ' +
  'a per-directory table of files with their key functions/classes/signatures, and a dependency sketch. ' +
  'Then WRITE it to ' + INTEGRATION_WT + '/MAP.md and commit it on the integration branch ' +
  '(git -C ' + INTEGRATION_WT + ' add MAP.md && git -C ' + INTEGRATION_WT + ' commit -m "docs: add MAP.md"), ' +
  'and ALSO copy it to ' + REPO + '/MAP.md for immediate visibility. Set wrote_map_file=true. ' +
  'Also return entry_points and a short architecture_summary. Keep map_markdown self-contained — it is the shared context for all workers.';

const planPrompt = (MAP, variant) =>
  'You are PLANNER ' + variant + '. Decompose the requested work into an executable DEPENDENCY GRAPH of tasks.\n' +
  'REQUEST:\n' + REQUEST + '\n' + modeBlock() + mapBlock(MAP) + '\n' +
  'PLAN THE DELTA, NOT THE INVENTORY. Your tasks are the difference between the TARGET END-STATE described in the ' +
  'REQUEST and what currently EXISTS. The MAP describes only what already exists — it is context, NOT the boundary of ' +
  'the work. Files that do not exist yet are FIRST-CLASS task outputs: name them in files[] and instruct the task to ' +
  'CREATE them. Derive the target file tree from the request (the modules/endpoints/tests/config it says must exist ' +
  'when done), then scope one task per coherent net-new unit plus tasks for any real modifications.\n' +
  'GREENFIELD DISCIPLINE (applies when MODE=greenfield): you are BUILDING a system from little or nothing. Do NOT ' +
  'anchor on the handful of existing files; do NOT scope tasks as "reconcile/polish the docs", "make files consistent ' +
  'with the spec", or "add a docs-consistency/CI suite" UNLESS the request explicitly asks for that. The spec/design ' +
  'docs are the SOURCE of the target, not the thing to edit. If the request describes a package with modules X/Y/Z, ' +
  'your tasks CREATE X, Y, Z and their tests — that is the whole job.\n' +
  'DO NOT INVENT WORK the request did not ask for (no speculative refactors, no unrequested CI/docs/tooling). ' +
  'DO NOT under-scope: every capability the request enumerates must map to at least one task.\n' +
  'Rules: (a) Each task owns a DISJOINT set of files (files[]); two tasks that must edit/create the same file MUST be ' +
  'merged or chained via deps so they never run in the same wave. (b) deps[] lists task ids that must finish first. ' +
  '(c) Maximize PARALLELISM — only add a dep when there is a real data/interface dependency (e.g. leaf modules depend ' +
  'on the shared types/interfaces task; wiring/daemon tasks depend on the modules they compose). (d) Each task brief is ' +
  'self-contained and test-first: state what to build, the acceptance check, and which test_types apply ' +
  '(unit/integration/e2e/property). (e) New-capability modules land standalone and get wired by a later integration task. ' +
  'Return PLAN with 3-20 tasks.';

const planArbiterPrompt = (MAP, plans) =>
  'You are the PLAN ARBITER. Two planners independently produced task DAGs for the same request. Merge them into ONE ' +
  'superior plan: take the better decomposition, keep file ownership DISJOINT within every wave, preserve real ' +
  'dependencies, and drop redundant or speculative tasks. If they fundamentally disagree on approach, pick the one ' +
  'that is safer to test incrementally and note why in rationale.\nREQUEST:\n' + REQUEST + '\n' + modeBlock() + mapBlock(MAP) + '\n' +
  'The plan must cover the DELTA from what exists to the target end-state in the request: net-new files are first-class, ' +
  'and (in greenfield MODE) do NOT keep any task that merely reconciles/polishes existing docs or adds unrequested ' +
  'CI/docs suites — drop those in favour of tasks that actually BUILD the requested system. Every capability the request ' +
  'enumerates must be covered by at least one task.\n' +
  'PLAN A: ' + JSON.stringify(plans[0]).slice(0, 60000) + '\nPLAN B: ' + JSON.stringify(plans[1]).slice(0, 60000) + '\n' +
  'Return the final PLAN.';

const baselinePrompt = (testCmd) =>
  'You are the BASELINE tester. Establish the pre-change test result on a read-only worktree.\n' +
  READ_WT('baseline') + '\n' +
  'Run the full test suite: ' + testCmd + '\nReturn SUITE (passed, total, failed, summary, tail). ' +
  'If the suite is already red, report exactly which tests fail — that is the baseline the pipeline must not worsen.';

const agentPushClause = (br) => (PUSH && PUSH_AGENT_BRANCHES && HAS_ORIGIN)
  ? ' Then push your branch to origin for tracking: git -C ' + REPO + ' push -u origin ' + br + ' (non-fatal if it fails). Set pushed=true on success, else false.'
  : ' (No remote push; your branch ' + br + ' already lives in the repo locally.) Set pushed=false.';

const implPrompt = (task, MAP, variant, testCmd) => {
  const br = agentBranch(task.id, variant);
  const wt = wtPath(agentWtName(task.id, variant));
  return 'You are IMPLEMENTER ' + variant + ' for task ' + task.id + ': ' + task.title + '.\n' +
    'WORKTREE RULES (absolute): operate ONLY inside ' + wt + '. Create YOUR OWN branch + worktree off the integration branch, ' +
    'INSIDE the repo (never /tmp):\n' +
    '  git -C ' + REPO + ' worktree add -b ' + br + ' ' + wt + ' ' + INTEGRATION_BRANCH + ' && cd ' + wt + '\n' +
    '  (if "worktree add" fails on a lock, wait 2s and retry once.)\n' +
    'You MUST NOT touch anything outside ' + wt + ' — not the base branch, not other worktrees, not .git internals.' +
    mapBlock(MAP) + '\n' +
    'TASK BRIEF:\n' + task.brief + '\n' +
    'You may ONLY touch these files (create them if missing): ' + task.files.join(', ') + '\n' +
    'WORK TEST-FIRST (TDD): (1) write failing tests of the required types [' + (task.test_types || ['unit']).join(', ') + '] ' +
    'that pin the acceptance criteria; (2) implement until they pass; (3) run the FULL suite (' + testCmd + ') to confirm no regression. ' +
    'Keep the diff minimal and in the surrounding style. No TODO/FIXME, no debug prints, no skipped tests.\n' +
    'CHECKPOINT: git add -A && git commit -m "gap ' + task.id + ' (' + variant + '): ' + task.title + '". ' +
    'Capture the diff: git -C ' + REPO + ' diff ' + INTEGRATION_BRANCH + '...' + br + '. Record the short commit hash.' +
    agentPushClause(br) + '\n' +
    'FINALLY remove your worktree (the branch ' + br + ' STAYS in the repo): git -C ' + REPO + ' worktree remove --force ' + wt + '.\n' +
    'Return IMPL with: branch=' + br + ', pushed, commit, the unified diff, tests_added, tests_passed, test_tail, files_touched.';
};

const verifyPrompt = (task, impls) =>
  'You are the VERIFIER (Oracle) for task ' + task.id + '. Two implementers produced diffs for the SAME task. ' +
  'Read both, pick the authoritative one (or merge the better parts), and do a gap analysis against the brief.\n' +
  'BRIEF:\n' + task.brief + '\nVariant A: ' + JSON.stringify(impls[0]).slice(0, 50000) +
  '\nVariant B: ' + JSON.stringify(impls[1] || {}).slice(0, 50000) + '\n' +
  'Decision matrix: full agreement -> pick cleaner (conf 90+); minor diffs -> cleaner (80+); structural -> merge (60-85); ' +
  'fundamental/both-wrong -> low confidence + list gaps. Return VERDICT (chosen_variant, the final diff, rationale, gaps, confidence).';

const adversaryPrompt = (task, verdict) =>
  'You are the ADVERSARY (Cassandra) for task ' + task.id + '. Try to REFUTE the chosen diff. Default holds=false when ' +
  'unsure. Hunt for: vacuous/always-pass tests, tests that assert nothing, a fix that only papers over the symptom, ' +
  'silent breakage of files outside scope, a diff that will not apply, left-in TODO/debug, or acceptance criteria not ' +
  'actually met.\nBRIEF:\n' + task.brief + '\nCHOSEN: ' + JSON.stringify(verdict).slice(0, 60000) + '\n' +
  'Return ADVERSARY (holds, problems[], severity).';

const pushCheckpoint = (tag) => {
  if (!PUSH || !HAS_ORIGIN) return 'No remote to push to (push disabled or the repo has no origin remote). The integration ' +
    'branch and tag ' + tag + ' already exist locally in ' + REPO + '. Leave pushed_refs empty.';
  return 'PUSH THE CHECKPOINT TO ORIGIN (push failures are NON-FATAL — record them in push_errors and keep going):\n' +
    '  git -C ' + REPO + ' push origin ' + INTEGRATION_BRANCH + ' && git -C ' + REPO + ' push origin ' + tag + '\n' +
    'List every ref you successfully pushed in pushed_refs (e.g. "origin ' + INTEGRATION_BRANCH + '").';
};

const integratePrompt = (batch, accepted, testCmd, waveNo) => {
  const tag = waveTag(waveNo);
  return 'You are the INTEGRATOR for wave ' + waveNo + '. You commit the accepted changes onto the INTEGRATION BRANCH in its ' +
    'worktree at ' + INTEGRATION_WT + ', run the FULL suite as a REGRESSION GATE, tag the wave, and push the checkpoint.\n' +
    'STEPS:\n' +
    '1) cd ' + INTEGRATION_WT + '  (the integration branch is checked out here — work ONLY in this worktree).\n' +
    '2) For each accepted task diff below: apply it with git apply --recount (tolerates wrong hunk counts), then ' +
    '   git add -A && git commit -m "checkpoint w' + waveNo + ': <task_id>". If a patch fails to apply, record the id in ' +
    '   rejected[] and CONTINUE with the others (never abort the batch). Put applied ids in applied[].\n' +
    '   Diffs (task_id -> diff):\n' + JSON.stringify(accepted.map(a => ({ id: a.id, diff: a.diff }))).slice(0, 150000) + '\n' +
    '3) Run the full suite as the regression gate: ' + testCmd + '. suite_passed MUST reflect the REAL exit status — ' +
    '   never claim green without running it. Record suite_tail.\n' +
    '4) Tag this checkpoint: git -C ' + REPO + ' tag -f -a ' + tag + ' -m "gap wave ' + waveNo + ' checkpoint".\n' +
    '5) ' + pushCheckpoint(tag) + '\n' +
    'Return INTEGRATE (applied[], rejected[], suite_passed, suite_tail, branch=' + INTEGRATION_BRANCH + ', tag=' + tag + ', ' +
    'head_commit, pushed_refs[], push_errors[], notes).';
};

const batteryPrompt = (kind, MAP, testCmd, lintCmd) => {
  const how = {
    unit: 'Run the unit tests only and report coverage of the changed code. ' + testCmd,
    integration: 'Run integration tests that exercise modules together / real boundaries. Identify gaps where modules are only unit-tested.',
    e2e: 'Run (or, if absent, author and run) an end-to-end / contract test that drives the system the way a real client does.',
    property: 'Add and run property-based / fuzz / edge-case tests for the non-trivial logic in the change.',
    lint: 'Run lint + type-check + formatter check: ' + lintCmd + '. Report every violation in the change.',
    security: 'Run a security scan: hunt for injection, secrets, unsafe deserialization, path traversal, missing authz, vulnerable deps.',
  }[kind];
  return 'You are the ' + kind.toUpperCase() + ' battery tester. Exercise the CURRENT integration state on a read-only worktree.\n' +
    READ_WT('battery-' + kind) + mapBlock(MAP) + '\n' + how + '\n' +
    'Be adversarial: a green run with no meaningful assertions is a FAIL. Return BATTERY (kind, passed, findings[], tail).';
};

const reviewPrompt = (lens, MAP, diff) =>
  'You are a CODE REVIEWER with the ' + lens + ' lens. Review ONLY the cumulative diff below against the map. Find real, ' +
  'specific defects in this lens; do not invent nits. ' + mapBlock(MAP) +
  '\nCUMULATIVE DIFF:\n' + diff.slice(0, 150000) + '\nReturn REVIEW (findings[] with file, issue, severity, fix).';

const hardenPrompt = (MAP, findings, testCmd, round) => {
  const tag = waveTag('harden-' + round);
  return 'You are the HARDENER (review round ' + round + '). Work in the integration worktree and checkpoint like a wave.\n' +
    'cd ' + INTEGRATION_WT + ' (the integration branch is checked out here). Apply these confirmed review findings in place, ' +
    'keeping every test green; do not introduce new public API.' + mapBlock(MAP) +
    '\nFINDINGS:\n' + JSON.stringify(findings).slice(0, 80000) + '\n' +
    'Then: git add -A && git commit -m "harden round ' + round + '"; run the full suite: ' + testCmd + '; ' +
    'git -C ' + REPO + ' tag -f -a ' + tag + ' -m "gap harden ' + round + '".\n' + pushCheckpoint(tag) + '\n' +
    'Return INTEGRATE (applied[], rejected[], suite_passed, suite_tail, branch=' + INTEGRATION_BRANCH + ', tag=' + tag + ', head_commit, pushed_refs[], push_errors[], notes).';
};

const gradePrompt = (MAP, diff, history, battery, reviewLeft) =>
  'You are the GRADE PANEL. Score the finished work against the bar honestly.\n' + RUBRIC + '\n' + GATE_DOCTRINE + '\n' +
  'First do a deterministic PRE-SCAN of the diff for disqualifying patterns (grep the diff for: TODO, FIXME, HACK, XXX, ' +
  'print(/console.log debug, skip/xfail, leaked-secret shapes). Their EXISTENCE is ground truth; you only judge weight.\n' +
  'REQUEST:\n' + REQUEST + mapBlock(MAP) +
  '\nTEST HISTORY: ' + JSON.stringify(history).slice(0, 30000) +
  '\nFULL BATTERY: ' + JSON.stringify(battery).slice(0, 30000) +
  '\nUNRESOLVED REVIEW FINDINGS: ' + JSON.stringify(reviewLeft).slice(0, 30000) +
  '\nCUMULATIVE DIFF (truncated):\n' + diff.slice(0, 120000) + '\n' +
  'Return GRADE (grade, meets_bar for ' + GRADE_BAR + ', gate_fired, gate_reason, blockers[], strengths[], rationale).';

const cumulativeDiffPrompt = () =>
  'Return the cumulative diff of all work on the integration branch. Run: git -C ' + REPO + ' diff ' + BASE_BRANCH + '...' +
  INTEGRATION_BRANCH + ' (every commit since the base). Output ONLY the unified diff as plain text, nothing else.';

const cleanupPrompt = () =>
  'Clean up the pipeline WORKTREES, KEEPING every branch and tag. Run:\n' +
  '  git -C ' + REPO + ' worktree remove --force ' + INTEGRATION_WT + ' 2>/dev/null || true\n' +
  '  git -C ' + REPO + ' worktree prune\n' +
  '  rm -rf ' + WT_ROOT + ' 2>/dev/null || true\n' +
  'Do NOT delete any gap/ branch or tag. Then run git -C ' + REPO + ' worktree list and report it briefly as plain text.';

// ---------------------------------------------------------------------------
// HELPERS — wave computation with disjoint-file batching
// ---------------------------------------------------------------------------
function chunk(arr, n) {
  const out = [];
  for (let i = 0; i < arr.length; i += n) out.push(arr.slice(i, i + n));
  return out;
}

function topoWaves(tasks) {
  const byId = new Map(tasks.map(t => [t.id, t]));
  const done = new Set();
  let remaining = tasks.map(t => t.id);
  const waves = [];
  let guard = 0;
  while (remaining.length && guard++ < 1000) {
    let ready = remaining.filter(id => (byId.get(id).deps || []).every(d => !byId.has(d) || done.has(d)));
    if (!ready.length) ready = remaining.slice(); // dependency cycle — flush everything as one wave
    waves.push(ready.map(id => byId.get(id)));
    ready.forEach(id => done.add(id));
    remaining = remaining.filter(id => !done.has(id));
  }
  return waves;
}

// Split a wave into file-disjoint batches so two agents never edit the same file concurrently.
function disjointBatches(waveTasks) {
  const batches = [];
  for (const t of waveTasks) {
    const tf = new Set(t.files || []);
    let placed = false;
    for (const b of batches) {
      if (!b.files.some(f => tf.has(f))) {
        b.tasks.push(t); (t.files || []).forEach(f => b.files.push(f)); placed = true; break;
      }
    }
    if (!placed) batches.push({ tasks: [t], files: [...(t.files || [])] });
  }
  return batches.map(b => b.tasks);
}

const REVIEW_LENSES = ['correctness/bugs', 'security', 'simplicity/reuse', 'tests-are-real', 'performance'];
const BATTERY_KINDS = ['unit', 'integration', 'e2e', 'property', 'lint', 'security'];

// ===========================================================================
// PIPELINE
// ===========================================================================
phase('Bootstrap');
const boot = await agent(bootstrapPrompt(), { label: 'bootstrap', phase: 'Bootstrap', schema: BOOTSTRAP, agentType: 'general-purpose' });
if (!boot || !boot.ok) { log('Bootstrap failed — cannot proceed'); return { error: 'bootstrap_failed', boot }; }
const TEST_CMD = boot.test_command;
const LINT_CMD = boot.lint_command || 'echo no-lint-configured';
// Assign the mutable git state the prompt builders read.
const RUN_ID = boot.run_id;
BASE_BRANCH = boot.base_branch || 'main';
INTEGRATION_BRANCH = boot.integration_branch || ('gap/' + RUN_ID + '/integration');
BRANCH_PREFIX = 'gap/' + RUN_ID;
WT_ROOT = REPO + '/.gap-worktrees/' + RUN_ID;
INTEGRATION_WT = WT_ROOT + '/integration';
ORIGIN_URL = boot.origin_url || '';
HAS_ORIGIN = !!ORIGIN_URL;
REPO_IS_GIT = boot.repo_is_git !== false;
const wavePushed = [];   // accumulates pushed refs across every checkpoint
// Decide build-vs-modify framing from the greenfield signal (fall back to a heuristic if the scout omitted it).
const codeFiles = typeof boot.code_file_count === 'number' ? boot.code_file_count
  : boot.files.filter(f => !/\.(md|txt|rst)$|(^|\/)(LICENSE|\.gitignore|\.gitattributes)$/i.test(f)).length;
MODE = (boot.is_greenfield === true || codeFiles <= 3) ? 'greenfield' : 'brownfield';
log('Bootstrapped IN-REPO. ' + boot.files.length + ' files (' + codeFiles + ' code). MODE=' + MODE.toUpperCase() +
  ' — planners will ' + (MODE === 'greenfield' ? 'BUILD from the requested target' : 'MODIFY the existing codebase') + '. ' +
  'test=' + TEST_CMD + ' | branch=' + INTEGRATION_BRANCH +
  ' | worktrees under ' + WT_ROOT + ' | remote push=' + (PUSH && HAS_ORIGIN ? 'origin' : 'off (branches stay local in repo)'));

// --- CARTOGRAPHY: fan out readers, synthesize MAP.md ---
phase('Cartography');
let shards = chunk(boot.files, SHARD_SIZE);
if (shards.length > MAX_CARTOGRAPHERS) {
  const per = Math.ceil(boot.files.length / MAX_CARTOGRAPHERS);
  shards = chunk(boot.files, per);
}
const shardMaps = (await parallel(shards.map((s, i) => () =>
  agent(cartographerPrompt(s, i + 1), { label: 'carto:' + (i + 1), phase: 'Cartography', schema: SHARDMAP })
))).filter(Boolean);
const allFileMaps = shardMaps.flatMap(s => s.file_maps || []);
const mapSynth = await agent(mapSynthPrompt(allFileMaps), { label: 'map-synth', phase: 'Cartography', schema: MAP_SYNTH, agentType: 'general-purpose' });
const MAP = mapSynth.map_markdown;
log('MAP built over ' + allFileMaps.length + ' files; MAP.md written=' + (mapSynth.wrote_map_file === true));

// --- PLAN: two isolated planners -> arbiter -> DAG ---
phase('Plan');
const plans = (await parallel([
  () => agent(planPrompt(MAP, 'A'), { label: 'plan:A', phase: 'Plan', schema: PLAN }),
  () => agent(planPrompt(MAP, 'B'), { label: 'plan:B', phase: 'Plan', schema: PLAN }),
])).filter(Boolean);
const finalPlan = plans.length === 2
  ? await agent(planArbiterPrompt(MAP, plans), { label: 'plan:arbiter', phase: 'Plan', schema: PLAN })
  : plans[0];
const tasks = (finalPlan && finalPlan.tasks) || [];
const waves = topoWaves(tasks);
log('Plan: ' + tasks.length + ' tasks across ' + waves.length + ' dependency waves');

// --- BASELINE: bottom slice of the test sandwich ---
phase('Baseline');
const baseline = await agent(baselinePrompt(TEST_CMD), { label: 'baseline', phase: 'Baseline', schema: SUITE, agentType: 'general-purpose' });
const history = [{ stage: 'baseline', passed: baseline?.passed, summary: baseline?.summary }];
log('Baseline suite: ' + (baseline?.passed ? 'GREEN' : 'RED') + ' — ' + (baseline?.summary || ''));

// --- BUILD WAVES: each wave is build -> integrate+regress (sandwich slice) ---
const escalations = [];
for (let w = 0; w < waves.length; w++) {
  const waveNo = w + 1;
  const batches = disjointBatches(waves[w]);
  phase('Build');
  log('Wave ' + waveNo + '/' + waves.length + ': ' + waves[w].length + ' tasks in ' + batches.length + ' file-disjoint batch(es)');

  for (const batch of batches) {
    // Build every task in the batch concurrently: Byzantine-2 -> verify -> adversary.
    const built = (await parallel(batch.map(task => () =>
      parallel([
        () => agent(implPrompt(task, MAP, 'A', TEST_CMD), { label: 'impl:' + task.id + ':A', phase: 'Build', schema: IMPL, agentType: 'general-purpose' }),
        () => agent(implPrompt(task, MAP, 'B', TEST_CMD), { label: 'impl:' + task.id + ':B', phase: 'Build', schema: IMPL, agentType: 'general-purpose' }),
      ]).then(async impls => {
        const ok = impls.filter(Boolean);
        if (!ok.length) return null;
        const verdict = await agent(verifyPrompt(task, ok), { label: 'verify:' + task.id, phase: 'Build', schema: VERDICT });
        const adv = await agent(adversaryPrompt(task, verdict), { label: 'adversary:' + task.id, phase: 'Build', schema: ADVERSARY });
        if (verdict.confidence < 40 || (adv && adv.holds === false && adv.severity === 'high')) {
          escalations.push({ task: task.id, confidence: verdict.confidence, adversary: adv });
        }
        const branches = ok.map(i => i.branch).filter(Boolean);
        return { id: task.id, diff: verdict.diff, confidence: verdict.confidence, gaps: verdict.gaps, adversary: adv, branches };
      })
    ))).filter(Boolean);

    // Accept only diffs the adversary did not high-severity-refute; integrate + regress.
    const accepted = built.filter(b => !(b.adversary && b.adversary.holds === false && b.adversary.severity === 'high'));
    phase('Integrate');
    const integ = await agent(integratePrompt(batch, accepted, TEST_CMD, waveNo), { label: 'integrate:w' + waveNo, phase: 'Integrate', schema: INTEGRATE, agentType: 'general-purpose' });
    history.push({ stage: 'wave' + waveNo, applied: integ?.applied, rejected: integ?.rejected, passed: integ?.suite_passed, tag: integ?.tag, pushed: integ?.pushed_refs });
    if (integ?.pushed_refs) wavePushed.push(...integ.pushed_refs);
    log('Wave ' + waveNo + ' checkpoint: applied=' + (integ?.applied || []).length + ' suite=' + (integ?.suite_passed ? 'GREEN' : 'RED') +
      ' tag=' + (integ?.tag || '-') + ' pushed=' + (integ?.pushed_refs || []).length + (integ?.push_errors?.length ? ' (push errors: ' + integ.push_errors.length + ')' : ''));
    if (integ && integ.suite_passed === false) {
      escalations.push({ stage: 'wave' + waveNo, reason: 'regression', tail: integ.suite_tail });
      log('REGRESSION GATE: wave ' + waveNo + ' reddened the suite — see escalations');
    }
  }
}

// --- FULL TEST BATTERY: top slice — all types in parallel ---
phase('Battery');
const battery = (await parallel(BATTERY_KINDS.map(k => () =>
  agent(batteryPrompt(k, MAP, TEST_CMD, LINT_CMD), { label: 'battery:' + k, phase: 'Battery', schema: BATTERY, agentType: 'general-purpose' })
))).filter(Boolean);
history.push({ stage: 'battery', results: battery.map(b => ({ kind: b.kind, passed: b.passed })) });
log('Battery: ' + battery.filter(b => b.passed).length + '/' + battery.length + ' green');

// --- REVIEW / HARDEN: loop until dry or rounds exhausted ---
let reviewLeft = [];
const seen = new Set();
for (let r = 1; r <= MAX_REVIEW_ROUNDS; r++) {
  phase('Review');
  const curDiff = await agent(cumulativeDiffPrompt(), { label: 'diff:r' + r, phase: 'Review', agentType: 'general-purpose' });
  const reviews = (await parallel(REVIEW_LENSES.map(lens => () =>
    agent(reviewPrompt(lens, MAP, curDiff || ''), { label: 'review:' + lens.split('/')[0] + ':r' + r, phase: 'Review', schema: REVIEW })
  ))).filter(Boolean);
  const findings = reviews.flatMap(rv => rv.findings || []);
  const fresh = findings.filter(f => { const k = (f.file || '') + '|' + f.issue; if (seen.has(k)) return false; seen.add(k); return true; });
  const blocking = fresh.filter(f => ['blocker', 'major', 'high', 'critical'].includes((f.severity || '').toLowerCase()));
  log('Review round ' + r + ': ' + fresh.length + ' new findings (' + blocking.length + ' blocking)');
  if (!blocking.length) { reviewLeft = fresh; break; }
  const harden = await agent(hardenPrompt(MAP, blocking, TEST_CMD, r), { label: 'harden:r' + r, phase: 'Review', schema: INTEGRATE, agentType: 'general-purpose' });
  history.push({ stage: 'harden-r' + r, applied: harden?.applied, passed: harden?.suite_passed, tag: harden?.tag, pushed: harden?.pushed_refs });
  if (harden?.pushed_refs) wavePushed.push(...harden.pushed_refs);
  reviewLeft = fresh;
  if (r === MAX_REVIEW_ROUNDS) log('Review hit MAX_REVIEW_ROUNDS with ' + blocking.length + ' blocking findings still open');
}

// --- A**** GRADE GATE ---
phase('Grade');
const finalDiff = await agent(cumulativeDiffPrompt(), { label: 'diff:final', phase: 'Grade', agentType: 'general-purpose' });
const grade = await agent(gradePrompt(MAP, finalDiff || '', history, battery, reviewLeft), { label: 'grade', phase: 'Grade', schema: GRADE });
log('GRADE: ' + grade.grade + (grade.meets_bar ? ' — meets ' + GRADE_BAR : ' — BELOW ' + GRADE_BAR) + (grade.gate_fired ? ' [GATE FIRED: ' + grade.gate_reason + ']' : ''));

// --- CLEANUP: remove worktrees; branches + tags persist in the repo ---
const cleanup = await agent(cleanupPrompt(), { label: 'cleanup', phase: 'Grade', agentType: 'general-purpose' });
log('Worktrees cleaned; branches + tags remain in ' + REPO);

return {
  request: REQUEST,
  map_markdown: MAP,
  map_written: mapSynth.wrote_map_file === true,
  repo_path: REPO,
  run_id: RUN_ID,
  base_branch: BASE_BRANCH,
  integration_branch: INTEGRATION_BRANCH,
  wave_tags: history.filter(h => h.tag).map(h => h.tag),
  pushed_refs: [...new Set(wavePushed)],
  pushed_to_origin: PUSH && HAS_ORIGIN,
  plan: tasks,
  waves: waves.length,
  test_history: history,
  battery: battery.map(b => ({ kind: b.kind, passed: b.passed, findings: b.findings })),
  unresolved_review: reviewLeft,
  grade,
  escalations,
  cleanup_status: cleanup,
  cumulative_diff: finalDiff,
  checkout_instructions: 'All work is on branch ' + INTEGRATION_BRANCH + ' INSIDE ' + REPO +
    (PUSH && HAS_ORIGIN ? ' (also pushed to origin)' : ' (local only — no origin remote)') +
    '. Review it: git -C ' + REPO + ' log --oneline ' + BASE_BRANCH + '..' + INTEGRATION_BRANCH +
    ' ; each agent has its own gap/' + RUN_ID + '/task-* branch and each wave is tagged gap/' + RUN_ID + '/wave-*. ' +
    'After acting on escalations and any gate_reason, merge it: git -C ' + REPO + ' checkout ' + BASE_BRANCH +
    ' && git -C ' + REPO + ' merge --no-ff ' + INTEGRATION_BRANCH + '. (Stale worktrees, if any: git -C ' + REPO + ' worktree prune.)',
};
