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
  npm_package: "reg-suit"
  npm_weekly_downloads: 499438
---

# Review visual regression diffs and publish snapshot baselines in CI with reg-suit

Use reg-suit when an agent needs to compare screenshot outputs against a stored baseline and publish a human-reviewable diff report. The skill is for visual regression review loops, not for general frontend tooling, because the agent’s job is to manage the compare, publish, and notify cycle around image snapshots.

## Prerequisites

Node.js, npm, screenshot-producing test artifacts, and an optional publisher plugin such as S3 or GCS

## Installation

Use the upstream install or setup path that matches your environment:
- $ npm install -g reg-suit
- --use-yarn-ws : If you use yarn workspace, turn this option on.
- npm i
- npx reg-suit run

Requirements and caveats from upstream:
- name: Use Node.js v10
- uses: actions/setup-node@v1
- node-version: "10.x"

Basic usage or getting-started notes:
- sh
- $ cd path-to-your-project
- $ reg-suit init

- Source: https://github.com/reg-viz/reg-suit
- Extracted from upstream docs: https://raw.githubusercontent.com/reg-viz/reg-suit/HEAD/README.md

## Documentation

- https://github.com/reg-viz/reg-suit#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-visual-regression-diffs-and-publish-snapshot-baselines-in-ci-with-reg-suit/)
