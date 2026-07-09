---
name: "Self-Push: Lazy-Check Before Submitting"
slug: "self-push"
description: "Run a structured lazy-check on any significant output before submitting. Forces root-cause analysis, alternative consideration, and outcome verification — especially critical in autonomous runs where no human reviewer will catch lazy shortcuts."
category: "Code Quality & Review"
framework: "Claude Code"
verification: listed
source: "https://github.com/TimeToBuildBob/bob"
---

# Self-Push: Lazy-Check Before Submitting

After any significant first-pass output, run a **lazy-check** before submitting: "Is this my best work, or did I take the easy path?"

AI models are trained to produce outputs good enough to avoid correction — this optimizes for satisficing, not maximizing. The model has higher capability than its default mode; it needs a push. In interactive sessions, humans provide that push. In autonomous sessions, this skill is the push.

## When to Use

- After writing any analysis, plan, code, or decision that will ship
- Especially in autonomous runs — no human reviewer will catch lazy parts
- When output feels "complete enough" but came together faster than expected
- Before committing changes where you didn't explicitly reject alternative approaches

**Skip** for: trivial config edits, journal date stamps, mechanical metadata updates.

## Installation

### Claude Code

Copy this skill directory into your agent's skill folder:

```bash
cp -R skills/self-push ~/.claude/skills/self-push
```

Then invoke with `/self-push` when you want to trigger a lazy-check.

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/self-push ~/.agent-skills/self-push
```

## The Lazy-Check (3 Questions)

Run these before submitting any significant output:

```
1. Did I stop at the first plausible explanation, or did I verify the root cause?
2. Can I name an alternative I considered and rejected, and why?
3. Did I actually verify the outcome, or am I assuming it worked?
```

If you can't answer all three with evidence → redo, don't just add words.

## Anti-Rationalization Table

| Rationalization | Reality |
|---|---|
| "I'll fix the root cause later — for now let me address the symptom" | Later never comes in autonomous sessions. Fix the root cause now — symptoms are just verification it's still active. |
| "This analysis is good enough — no one is reviewing it live" | The absence of pushback is why you must push harder. Autonomous runs have no reviewer; the quality burden is entirely on your own lazy-check. |
| "I already checked, no need to double-check" | Single checks miss subtle state: dirty submodules, uncommitted worktrees, unseen stderr, false negatives from stale caches. |
| "The first approach worked, so it's the best one" | First plausible solution is rarely optimal. List 2-3 alternatives before committing. If you can't name a trade-off you rejected, you didn't consider alternatives. |
| "This is just a quick fix — not worth deep analysis" | Quick fixes that skip root-cause analysis compound into tech-debt avalanches. If it's worth doing, it's worth understanding why it needed doing. |
| "Tests pass, so the code is correct" | Passing tests don't catch architecture drift, silent edge cases, security regressions, or gaps in the tests themselves. |
| "I'll explain the reasoning in the commit message" | Commit messages say *what* changed; they rarely capture *why I chose this over the alternative I rejected*. Write the trade-off decision before committing. |
| "I already ran that command once — it'll be the same result" | Filesystem state may have changed. Commands with side effects produce different results on subsequent runs. Re-verify if the outcome matters. |

## Red Flags

- Can't articulate what alternatives were considered and rejected
- "Fixing" a symptom without tracing it to its root cause
- Commands described as "verified" but no output evidence in the conversation
- Commit messages that describe *what* changed but not *why this approach*
- Output feels structurally correct but thin — surface-level engagement
- Same command run twice without intervening state changes
- Bug fixes without a reproduction path or regression test

## Verification Checklist

Before every significant commit:

```
- [ ] Root cause identified (not just symptom)
- [ ] At least one alternative considered and rejected with reason
- [ ] All asserted outcomes actually verified (not assumed)
- [ ] No command re-run without intervening state change
- [ ] If a bug was fixed, there's a reproduction path or regression test
- [ ] The commit message captures the *why*, not just the *what*
```

## Why This Matters

The training objective for LLMs optimizes for "produce output good enough to avoid correction" — not "maximize quality." That gradient is fine when a human is in the loop. In autonomous agents, there is no correction signal until the work has already shipped. This skill injects an explicit quality gate before submission, shifting the effective optimization target from "avoid correction" to "maximize correctness."
