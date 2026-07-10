---
name: "Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed"
slug: "catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed"
description: "Use CodSpeed when an agent needs benchmark runs compared in CI and surfaced on pull requests before performance regressions merge."
github_stars: 143
verification: "security_reviewed"
source: "https://github.com/CodSpeedHQ/codspeed"
author: "CodSpeed"
publisher_type: "company"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "CodSpeedHQ/codspeed"
  github_stars: 143
  npm_package: "@codspeed/core"
  npm_weekly_downloads: 234588
---

# Catch benchmark regressions in pull requests before slowdowns ship with CodSpeed

Use CodSpeed when an agent needs benchmark runs compared in CI and surfaced on pull requests before performance regressions merge.

## Prerequisites

A repository with executable benchmarks or benchmark commands, a CI system such as GitHub Actions, and a CodSpeed account or auth flow for storing and comparing results.

## Installation

Use the upstream install or setup path that matches your environment:
- codspeed run cargo codspeed run
- codspeed run pnpm vitest bench

Requirements and caveats from upstream:
- 🐍 **Multi-language support** for Python, Rust, Node.js, Go, C/C++ and more.
- codspeed exec -- python my_script.py
- codspeed exec --mode walltime -- node app.js

Basic usage or getting-started notes:
- 🏠 **Run locally or in CI** - works on your machine and integrates with GitHub Actions, GitLab CI, and more.
- bash
- [!NOTE]

- Source: https://github.com/CodSpeedHQ/codspeed
- Extracted from upstream docs: https://raw.githubusercontent.com/CodSpeedHQ/codspeed/HEAD/README.md

## Documentation

- https://codspeed.io/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-benchmark-regressions-in-pull-requests-before-slowdowns-ship-with-codspeed/)
