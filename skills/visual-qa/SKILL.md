---
name: "Visual QA"
slug: "visual-qa"
description: "Review a rendered interface with an isolated committee of orthogonal visual experts. Use for UI audits, responsive and theme checks, edge-state coverage, screenshot-based accessibility review, adversarial finding validation, and optional fix-and-recapture loops."
category: "Code Quality & Review"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/visual-qa"
---

# Visual QA

Visual QA is a review protocol. The project adapter owns capture; the skill supplies the state matrix, independent expert lenses, refutation, synthesis, and optional verified fixes.

## Inputs

Infer these when safe; otherwise ask.

- **adapter**: project-specific capture and test instructions in `adapters/<project>.md`
- **tier**: `quick`, `full`, or `deep`; default `full`
- **mode**: `review` or `fix`; default `review`
- **scope**: flows and screens; default to the adapter's declared flows
- **focus**: optional lens or risk to emphasize

## Capability discovery

Before capture:

1. Inspect the adapter and project scripts for an existing screenshot command.
2. Inventory actually available browser, device, native-UI, and image-reading tools.
3. Prefer the project's deterministic capture harness. Do not assume Playwright, a browser MCP, or a particular agent runtime exists.
4. If capture or image inspection is unavailable, stop and name the missing capability. Never fabricate screenshots or visual findings.

This repository does not ship a universal browser driver. Start from [`adapters/_template.md`](adapters/_template.md) when a project has no adapter.

## Pipeline

1. **Capture** — render a deterministic matrix of flows, states, breakpoints, and themes; add a clearly marked exploratory pass.
2. **Validate** — run `python3 scripts/validate_manifest.py path/to/manifest.json --check-files`.
3. **Review** — give each selected expert only its lens, negative constraint, manifest, and images. Experts do not see one another's findings.
4. **Refute** — assign a skeptic to every critical/high/medium finding. The default verdict is “not proven” unless pixels or interaction evidence support it.
5. **Synthesize** — deduplicate, preserve dissent, and rank by severity, confidence, independent votes, and user impact.
6. **Fix** — only in `mode: fix`, with explicit authority. Give disjoint file scopes to isolated implementers and apply reviewed diffs once.
7. **Re-verify** — recapture affected states and compare before/after for improvement and regression.

## Capture contract

The matrix should cover:

- flows: the core user journeys;
- states: default, empty, long-content, loading, error/offline, disabled, and first-run;
- breakpoints: project-specific, with narrow/mobile, medium, and wide coverage;
- themes: every supported theme;
- transitions: pending, focus, hover, pressed, open/close, and success/failure where relevant.

Pin time, timezone, locale, randomness, animation policy, and fixtures where the project permits. Deterministic fixtures should be purpose-built and non-sensitive. Exploratory screenshots are useful evidence but are not goldens.

`manifest.json` is an array of:

```json
{
  "label": "checkout-error-mobile-dark",
  "path": "qa-shots/checkout-error-mobile-dark.png",
  "flow": "checkout",
  "state": "error",
  "breakpoint": 320,
  "theme": "dark"
}
```

Paths must be repository-relative and use forward slashes.

## Finding contract

Each finding must contain:

- expert slug and lens;
- manifest label and exact visible region;
- issue and governing principle;
- pixel or interaction evidence;
- severity: `critical`, `high`, `medium`, `low`, or `nit`;
- concrete proposed fix;
- confidence from 0 to 1;
- any additional capture required.

Silence beats weak findings. Aesthetic preference is not an objective defect. Preserve minority opinions when they are high-confidence and clearly labeled as taste.

## Severity

- **critical**: data loss, unintended irreversible action, unreadable core content, or sensitive information exposed in-frame
- **high**: blocks or badly degrades a core task, fails a required accessibility criterion, or breaks a required state
- **medium**: material friction, inconsistency, or ambiguous affordance
- **low/nit**: polish with limited user impact

## Guardrails

- Isolation is mandatory during review.
- Validate capture coverage before judging design.
- Real-account or sensitive screenshots are ephemeral: keep them outside version control and remove them according to project policy.
- Never commit raw captures by default. Only synthetic goldens may be committed after human ratification.
- The human owns final taste, brand direction, and golden-image approval.
- A screenshot cannot prove DOM semantics, keyboard behavior, screen-reader output, performance, or network correctness. Route those claims to appropriate tests.

Select experts from [`roster.md`](roster.md). Keep the committee as small as the risk permits.

## Installation and upstream provenance

The upstream skill identifier is `visual-qa`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/visual-qa --skill visual-qa --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/visual-qa#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`db009836bcd3`](https://github.com/AntreasAntoniou/visual-qa/tree/db009836bcd3137ce4b507f629c743afcbe8fdbd). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
