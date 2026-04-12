---
title: "Review visual regression diffs and publish snapshot baselines in CI with reg-suit"
slug: "review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
source: "https://github.com/reg-viz/reg-suit"
---

# Review visual regression diffs and publish snapshot baselines in CI with reg-suit

Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit/)
