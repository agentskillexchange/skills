---
name: "Multi-Lens Review"
slug: "multi-lens-review"
description: "Review a PR or diff through three independent focused lenses (correctness, security, test coverage), then deduplicate and validate findings before persisting. Catches more real bugs than a single general review pass while producing less noise."
category: "Code Quality & Review"
framework: "Claude Code"
verification: listed
source: "https://github.com/TimeToBuildBob/bob"
---

# Multi-Lens Review

Review a diff through multiple focused lenses, then converge the results into one durable output.

**Core principle**: One general review pass catches obvious stuff. Independent focused passes catch the real bugs. But only persist findings that survive deduplication and evidence checks.

A multi-lens review works because each lens creates a different cognitive frame. A security reviewer notices different things than a correctness reviewer, even on the same code. Running three focused passes surfaces the intersection of what each frame misses — which is where real bugs hide.

## When to Use

**Use** when:
- The diff is non-trivial or risky
- You need findings, not a vibe-check summary
- Security, correctness, or missing tests all plausibly matter
- A single-pass review feels likely to miss something

**Skip** when:
- The diff is tiny and mechanical
- The user asked for a lightweight summary, not findings
- You already have a good human-reviewed finding set and just need to restate it

## Installation

### Claude Code

```bash
cp -R skills/multi-lens-review ~/.claude/skills/multi-lens-review
```

Invoke with `/multi-lens-review` when starting a rigorous PR or diff review.

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/multi-lens-review ~/.agent-skills/multi-lens-review
```

## Default Lenses

Use these three unless the task clearly needs a different set:

1. **Correctness** — logic bugs, broken invariants, requirement mismatches
2. **Security** — unsafe input handling, secret leakage, authz/authn drift
3. **Test Coverage** — missing regression tests, unverified edge cases

Do not add more lenses in the first pass unless the task explicitly justifies it.

## Inputs To Gather

Before reviewing, collect:

- the diff or changed-file list (`git diff` or `gh pr diff`)
- the PR / issue description if relevant
- the repo README, package structure, and recent related changes
- any existing known issues or findings for this area of the code

If you skip this prep, the lenses will waste time rediscovering repo context.

## Finding Schema

Every lens output must include a structured findings block. This enables deduplication without guesswork:

````md
## Findings

```json
[
  {
    "category": "security",
    "severity": "high",
    "file_path": "src/foo.py",
    "line": "42-49",
    "title": "User-controlled input reaches shell=True",
    "description": "Brief statement of the bug.",
    "evidence": "Concrete code evidence tied to file + line.",
    "confidence": 0.82,
    "fix_hint": "Optional repair hint."
  }
]
```
````

**No evidence, no finding.** A finding without a specific file path and line reference is an opinion, not a finding.

## Procedure

1. **Prepare shared context**
   - Create a working directory for this review run (e.g. `review-runs/<repo>/<timestamp>/`)
   - Write an `input.md` summarizing: what changed, what the PR claims to do, scope
   - Read it before reviewing — shared context prevents redundant re-discovery

2. **Run the three lens passes**
   - If the runtime supports parallel subagents, fan them out
   - Otherwise run sequentially, keeping each pass narrow
   - Keep each pass narrow: if a security pass starts talking about style, it is drifting

3. **Normalize the findings**
   - Convert each lens output to the shared schema above
   - Drop claims without file-specific evidence
   - Drop findings below confidence 0.6 unless a follow-up pass rescues them

4. **Deduplicate**
   - Merge same-problem findings across lenses
   - Keep the strongest wording and highest-confidence evidence
   - Preserve lens origin as tags, e.g. `lens:security`
   - Resolve duplicates by majority confidence, not by taking both

5. **Validate survivors**
   - Re-read the relevant code for each surviving finding
   - If still uncertain, use a cheap clarification pass before escalating
   - Only escalate to an expensive deep-review pass for findings that still look material

6. **Persist confirmed survivors**
   - Record findings in a JSON file or your project's tracking system
   - Tag with lens origin and review run identifier for traceability

7. **Write the review output**
   - Present findings ordered by severity (critical → high → medium → low)
   - State explicitly what you checked and what you did not check
   - A review that says "I checked X, not Y" is more useful than one that implies completeness

## Suggested Artifact Layout

```txt
review-runs/<repo_slug>/<run_id>/
├── input.md            ← shared context for all lenses
├── lens-correctness.md ← lens 1 findings with JSON block
├── lens-security.md    ← lens 2 findings with JSON block
├── lens-test-cov.md    ← lens 3 findings with JSON block
├── candidates.jsonl    ← deduplicated candidates before validation
└── summary.md          ← final confirmed findings + review narrative
```

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Run three generic reviews and call them "lenses" | Give each pass a distinct job with an explicit scope constraint. |
| Persist every raw finding | Only persist confirmed survivors after dedup + validation. |
| Let every lens re-read the whole repo | Build a tight shared context packet first — one input.md for all lenses. |
| Add 6-7 lenses immediately | Start with 3. If they miss something important, add a 4th targeted lens. |
| Use expensive deep-review on every candidate | Cheap validation (re-read the code, spot-check the claim) before escalating. |
| Treat "no evidence" findings as low-severity | No evidence = not a finding. Demote to a note or discard. |

## Outcome

A good multi-lens review:
- catches more real bugs than a single pass
- produces less duplicated noise than ad hoc repeated reviews
- leaves a durable artifact: the run directory is resumable across sessions
- reports what was checked, so future reviewers know the coverage boundary
