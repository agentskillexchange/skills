# Visual QA

An Agent Skill for finding visible interface problems through independent, evidence-backed screenshot reviews.

A screen can look convincing at one width, in one theme, with a short name and a full list. The useful question is what happens when the name wraps, the list is empty, the request fails, or the user switches to dark mode. Visual QA starts by making those states visible, then gives reviewers different jobs so the audit is not just several versions of the same opinion.

Use it before a release, after a layout change, or when a UI needs a concrete review rather than “make it look better.” For a checkout flow, that might mean capturing mobile and desktop layouts with long addresses, loading buttons, validation errors, and both themes—then tying each finding to the exact frame and region that demonstrates it.

## How it works

```text
capture matrix → validate manifest → isolated reviews → adversarial refutation
               → prioritized synthesis → optional fix → recapture
```

Each expert gets one lens and a negative constraint: a typography reviewer looks at wrapping and alignment, not wording; a responsive-layout reviewer looks at clipping and reflow, not desktop brand taste. Reviewers do not see one another's findings. A skeptic then challenges critical, high, and medium findings before synthesis, with “not proven” as the default when the evidence is insufficient.

The [roster](roster.md) offers a five-lens `quick` tier, a twelve-lens `full` tier, and additional `deep` specialists for evidence such as localization or data displays. The default is `full`, but use the smallest committee the risk warrants. Independent review requires a host that can actually isolate the reviewers; this repository does not create those agents itself.

## What you get

The workflow produces a screenshot manifest and a prioritized review: each finding identifies its lens, screenshot label, visible region, evidence, severity, confidence, and proposed fix. Synthesis removes duplicates without erasing meaningful dissent, and requests additional captures where a conclusion cannot yet be supported.

`review` is the default and does not authorize implementation. With explicit `fix` authority, the workflow assigns disjoint implementation scopes, applies reviewed changes, and recaptures the affected states to check improvement and regression. Humans retain brand, taste, and golden-image approval.

## What is included

- an Agent Skill operating contract in [SKILL.md](SKILL.md);
- a compact, public-safe [expert roster](roster.md);
- a generic [project adapter template](adapters/_template.md);
- a dependency-free [manifest validator](scripts/validate_manifest.py) with tests.

Visual QA intentionally does not bundle a browser driver or agent framework. It discovers and uses the project's existing capture command and the host's available image-inspection tools. If those capabilities are absent, it reports that limitation instead of pretending a review occurred.

The validator checks manifest structure, duplicate labels/paths, and—when requested—whether image files exist within the selected root. It does not inspect pixels, prove that a screenshot is current, or establish that the requested state matrix is complete. Those remain review responsibilities.

## Quick start

1. Install the skill: `npx skills add AntreasAntoniou/visual-qa`.
2. Copy `adapters/_template.md` to an adapter owned by your project.
3. Fill in the capture command, deterministic controls, flows, states, breakpoints, themes, and test commands.
4. Run capture.
5. Validate the gallery from the skill checkout, setting `--root` to the project whose repository-relative image paths appear in the manifest:

```bash
python3 scripts/validate_manifest.py path/to/qa-shots/manifest.json --root path/to/project --check-files
```

6. Invoke the skill in `review` mode with the adapter and desired tier.

## Visual QA and executable tests

Visual QA asks whether the rendered interface communicates clearly and holds up across the captured states. It cannot prove DOM semantics, keyboard behavior, screen-reader output, backend correctness, network behavior, or runtime performance from screenshots.

[Heimdall](https://github.com/AntreasAntoniou/heimdall) serves a different role: it runs browser/API test plans against explicit assertions, including automated accessibility and pixel-diff checks. A pixel match does not decide whether a design is good; a visual review does not prove that a transaction works. Use the appropriate evidence for each claim. No automatic integration between these packages is assumed.

## Privacy

Screenshots can contain names, messages, access tokens, account identifiers, and other personal data. Capture synthetic fixtures for repeatable audits. Keep real-account captures outside version control and follow the project's deletion and retention policy.

The validator reads local JSON and optionally verifies local image paths. It performs no network requests. That does not make the whole review local: screenshots opened by a hosted agent may be processed by its model provider. Choose approved capture and review environments for sensitive material. See [SECURITY.md](SECURITY.md).

## Development

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q scripts tests
```

The automated suite creates temporary manifests and commits no screenshots.

## License

MIT. See [LICENSE](LICENSE).
