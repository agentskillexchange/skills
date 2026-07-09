---
name: "Five-Element Spec: Scope Before Coding"
slug: "five-element-spec"
description: "Translate a vague request or GitHub issue into a concrete, testable spec using five structured elements (problem, scope, acceptance criteria, edge cases, success criterion) before writing any code. Prevents scope creep, PR churn, and mid-implementation pivots."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed
source: "https://github.com/TimeToBuildBob/bob"
---

# Five-Element Spec: Scope Before Coding

Translate a vague request or GitHub issue into a concrete, actionable spec before writing any code.

**Core principle**: If you can't write down what "done" looks like in two sentences, you're not ready to start.

The five-element spec is a lightweight planning format that forces explicit scope boundaries, testable acceptance criteria, and a binary done/not-done signal. It takes 5 minutes for small tasks and prevents hours of rework from scope mismatches, PR churn, and "I thought we wanted X" surprises.

## When to Use

**Always** before:
- Starting work on a GitHub issue that hasn't been scoped into a task
- Implementing a feature where acceptance criteria aren't obvious
- Any task that will take >30 minutes (if you can't spec it in 5 minutes, the scope is unclear)
- Work that will produce a PR (scope ambiguity creates PR churn)

**Skip** for:
- Bug fix with a clear reproduction path and obvious scope
- Mechanical tasks (update a config value, rename a symbol, bump a version)
- Work already described in a task with a `success_criterion` field

## Installation

### Claude Code

```bash
cp -R skills/five-element-spec ~/.claude/skills/five-element-spec
```

Invoke with `/five-element-spec` before starting any non-trivial implementation task.

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/five-element-spec ~/.agent-skills/five-element-spec
```

## The 5-Element Spec

A complete spec answers five questions:

```
1. PROBLEM — What is broken or missing? What pain does this cause?
2. SCOPE — What is in scope? What is explicitly out of scope?
3. ACCEPTANCE CRITERIA — What must be true when this is done? (testable)
4. EDGE CASES — What unusual inputs or states must be handled?
5. SUCCESS CRITERION — One sentence: how will we know it's done?
```

## Spec Template

```markdown
## Problem
[1-2 sentences: what is broken/missing and why it matters]

## Scope
**In scope:**
- [Specific thing 1]
- [Specific thing 2]

**Out of scope (explicitly):**
- [Thing someone might expect but we're not doing]

## Acceptance Criteria
- [ ] [Testable condition 1 — "X works when Y" or "CI passes for Z"]
- [ ] [Testable condition 2]
- [ ] [Testable condition 3]

## Edge Cases
- [Input or state that needs explicit handling]
- [Boundary condition]

## Success Criterion
[One sentence. "When [action], [outcome] happens, verified by [test/check]."]
```

## From Issue to Spec

### Step 1: Read the issue

```bash
gh issue view OWNER/REPO#NUM
```

Look for: what's the complaint? what does the reporter expect? what's missing?

### Step 2: Write the spec

Use the 5-element template above. If you can't fill it in, the issue needs more information — file a comment asking for clarification rather than guessing.

### Step 3: Create a task

Record the spec as a task or ticket in your tracking system of choice, with the `success_criterion` as a first-class field. The binary done/not-done signal from the success criterion is what enables autonomous completion without mid-task re-planning.

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| "I'll figure out the scope as I go" | Figure out the scope before you start. Scope discovered mid-implementation causes rework. |
| "The issue title is clear enough" | Issue titles describe the symptom. Acceptance criteria describe what done looks like. These are different. |
| "I'll add acceptance criteria to the PR" | PR acceptance criteria are retrospective. Spec first, then implementation, then PR. |
| "This is small, I don't need a spec" | If it's small enough to skip a spec, it's small enough to write the spec in 3 minutes. Do it. |
| "The issue has a lot of comments, I'll read them later" | Read them now. The thread often contains the acceptance criteria, edge cases, and out-of-scope decisions already worked out. |
| Implementing everything in the issue | Issues are wishlists. Specs are commitments. Pick the minimum slice that closes the issue. |

## Red Flags (spec is insufficient)

- Acceptance criteria use words like "better", "improved", "faster" without a measurable threshold
- No explicit out-of-scope list (scope creep guaranteed)
- Success criterion references "user will be happy" — not testable
- Spec lists 8+ acceptance criteria (too big for one task; break it down)
- Edge cases section is empty (they exist; you just haven't thought about them)

## Outcome

A good spec:
- Prevents starting the wrong thing
- Enables autonomous completion without mid-task re-planning
- Creates clear done/not-done signal for the success criterion field
- Reduces PR review churn (reviewer and author agree on scope upfront)
- Makes parallel agent sessions safe (clear scope = no convergent duplicate work)
