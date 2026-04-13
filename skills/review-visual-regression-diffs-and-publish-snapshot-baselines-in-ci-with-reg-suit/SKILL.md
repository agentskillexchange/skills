---
title: "Review visual regression diffs and publish snapshot baselines in CI with reg-suit"
description: "Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots."
verification: "security_reviewed"
source: "https://github.com/reg-viz/reg-suit"
category: ["Code Quality &amp; Review"]
framework: ["Multi-Framework"]
---

# Review visual regression diffs and publish snapshot baselines in CI with reg-suit

Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit/)
