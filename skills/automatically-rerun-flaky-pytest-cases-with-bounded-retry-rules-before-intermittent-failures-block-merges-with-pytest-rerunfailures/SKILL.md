---
title: "Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures"
description: "Use pytest-rerunfailures when an agent needs to stabilize an existing pytest pipeline by rerunning intermittent failures under explicit retry limits. Invoke it instead of manually rerunning the full suite or bolting retry logic onto CI scripts when the job is flaky-test containment inside pytest itself. The scope boundary is narrow: retry and report unstable pytest cases, not generic Python testing, broad CI orchestration, or a plain plugin listing."
source: "https://github.com/pytest-dev/pytest-rerunfailures"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pytest-dev/pytest-rerunfailures"
  github_stars: 458
  npm_package: "pytest-rerunfailures"
---

# Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures

Use pytest-rerunfailures when an agent needs to stabilize an existing pytest pipeline by rerunning intermittent failures under explicit retry limits. Invoke it instead of manually rerunning the full suite or bolting retry logic onto CI scripts when the job is flaky-test containment inside pytest itself. The scope boundary is narrow: retry and report unstable pytest cases, not generic Python testing, broad CI orchestration, or a plain plugin listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures/)
