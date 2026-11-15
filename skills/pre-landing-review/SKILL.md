---
name: "Pre-Landing Self-Review"
slug: "pre-landing-review"
description: "Structured self-review checklist to run before committing substantial code changes. Covers edge cases, error paths, test coverage, documentation, and code quality — so CI is a last resort, not your first reviewer."
github_stars: 14
verification: "listed"
source: "https://github.com/gptme/gptme-contrib"
author: "gptme"
category: "Code Quality & Review"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "gptme/gptme-contrib"
  github_stars: 14
---

# Pre-Landing Self-Review

Before committing significant changes, run through this checklist. Catch issues before CI catches them — or worse, before users do.

## When to Use

**Run this skill when any of these are true:**

- Changed >100 lines of code
- Modified >5 files
- Touched core infrastructure (executor, storage, main dispatch loops)
- Introduced new abstractions or public APIs
- Uncertain about edge cases or design choices

**Quick gate:**
```shell
git diff --stat HEAD | tail -5  # How much changed?
git diff --name-only HEAD | wc -l  # How many files?
```

## Skip If

- Trivial change (≤50 lines, ≤3 files)
- Pure documentation or lesson updates
- Test-only changes (tests are their own review)
- Simple one-liner bug fix with obvious, limited scope
- Mechanical refactoring with no logic changes

## The Checklist

### 1. Edge Cases
```
- [ ] Null/empty inputs handled?
- [ ] Boundary conditions tested (off-by-one, empty lists, zero)?
- [ ] Concurrent access or race conditions considered?
- [ ] Unicode/encoding issues if processing text?
```

### 2. Error Paths
```
- [ ] All exceptions caught at the right level (not too broad)?
- [ ] Error messages informative (what failed, why, what to do)?
- [ ] Failure modes fail gracefully, not silently?
- [ ] No bare `except:` or swallowed errors?
```

### 3. Test Coverage
```
- [ ] Critical paths have tests?
- [ ] Edge cases identified above have tests?
- [ ] Tests actually run and pass?
- [ ] No test stubs left at `pass` or `...`?
```

### 4. Documentation
```
- [ ] Docstrings/comments match current behavior?
- [ ] README updated if public interface changed?
- [ ] Commit message captures what changed and why?
- [ ] Relevant architecture docs still accurate?
```

### 5. Code Quality
```
- [ ] Naming is clear and consistent with surrounding code?
- [ ] No obvious code smells (God functions, magic numbers, hardcoded paths)?
- [ ] Follows existing patterns in the file/package?
- [ ] Static analysis / typecheck passes?
```

## One-Liner Smoke Test

```bash
# Run before committing (adapt to your stack):
make format && make typecheck && pytest -x -q && echo "✅ Clean to land"
```

If any step fails, fix it before committing. Don't ship red.

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| "CI will catch it" | CI is a last resort, not a substitute for your own judgment. Catch it first. |
| "I'll add tests later" | Later doesn't come. Write the test now or accept the gap permanently. |
| "It worked when I tested manually" | Manual tests aren't reproducible. Write an automated test so future sessions can verify it too. |
| "The error message is a TODO" | TODO error messages ship as TODO error messages. Write the real message now. |
| "I can see from the code it handles this case" | If it's not tested, a future refactor will break it invisibly. |

## Why This Matters

Autonomous agents are trained to produce outputs good enough to avoid correction. Without a structured review gate, autonomous code commits bypass the human-in-the-loop check that normally catches regressions and edge cases. This skill acts as that gate — five targeted lenses run in sequence so nothing obvious slips through.

The payoff compounds: each review pass that catches a real issue is a CI round-trip saved, a user bug avoided, and a revert PR not needed.

## Related

- [Self-Push skill](../self-push/SKILL.md) — quality/laziness check that complements this structural review
- [Multi-Lens Review skill](../multi-lens-review/SKILL.md) — deeper parallel review for high-stakes changes
