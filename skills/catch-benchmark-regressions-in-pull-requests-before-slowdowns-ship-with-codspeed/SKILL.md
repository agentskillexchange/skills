---
title: "Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed"
description: "Use CodSpeed when an agent needs benchmark runs compared in CI and surfaced on pull requests before performance regressions merge."
verification: "security_reviewed"
source: "https://github.com/CodSpeedHQ/codspeed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "CodSpeedHQ/codspeed"
  github_stars: 143
  ase_npm_package: "@codspeed/core"
  npm_weekly_downloads: 234588
---

# Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed

CodSpeed gives an agent a narrow performance-guard workflow. It can run executable programs or existing benchmark suites, compare the results against a baseline, and report regressions directly in pull-request review flows. That makes it useful when a repository already has benchmarks or can add a few targeted ones, and the team wants performance evidence before merge.

The scope boundary is clear. Invoke it when the agent’s job is benchmark execution and regression detection inside review or CI, not when the user wants a general observability platform, profiling backend, or production telemetry stack. The job-to-be-done is catching code slowdowns before they ship.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed/)
