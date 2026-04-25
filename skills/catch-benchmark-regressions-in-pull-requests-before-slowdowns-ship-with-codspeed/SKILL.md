---
title: "Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed"
description: "Use CodSpeed when an agent needs benchmark runs compared in CI and surfaced on pull requests before performance regressions merge."
verification: "security_reviewed"
source: "https://github.com/CodSpeedHQ/codspeed"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "CodSpeedHQ/codspeed"
  github_stars: 143
  npm_package: "@codspeed/core"
  npm_weekly_downloads: 234588
---

# Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed

CodSpeed gives an agent a narrow performance-guard workflow. It can run executable programs or existing benchmark suites, compare the results against a baseline, and report regressions directly in pull-request review flows. That makes it useful when a repository already has benchmarks or can add a few targeted ones, and the team wants performance evidence before merge.

The scope boundary is clear. Invoke it when the agent’s job is benchmark execution and regression detection inside review or CI, not when the user wants a general observability platform, profiling backend, or production telemetry stack. The job-to-be-done is catching code slowdowns before they ship.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed/)
