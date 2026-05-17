---
name: "Review visual regression diffs and publish snapshot baselines in CI with reg-suit"
slug: "review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit"
description: "Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots."
github_stars: 1260
verification: "security_reviewed"
source: "https://github.com/reg-viz/reg-suit"
author: "reg-viz"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "reg-viz/reg-suit"
  github_stars: 1260
---

# Review visual regression diffs and publish snapshot baselines in CI with reg-suit

Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots.

## Prerequisites

Node.js, npm, screenshot-producing test artifacts, and an optional publisher plugin such as S3 or GCS

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install --save-dev reg-suit
```

## Documentation

- https://github.com/reg-viz/reg-suit#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit/)
