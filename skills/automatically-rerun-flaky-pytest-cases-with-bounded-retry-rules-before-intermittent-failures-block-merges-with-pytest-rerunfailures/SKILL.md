---
title: "Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures"
description: "Add controlled retries to pytest runs so agents can contain flaky tests and report final failures without rerunning whole suites by hand."
verification: listed
source: "https://github.com/pytest-dev/pytest-rerunfailures"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pytest-dev/pytest-rerunfailures"
  github_stars: 458
  ase_npm_package: "pytest-rerunfailures"
---

# Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures

Use pytest-rerunfailures when an agent needs to stabilize an existing pytest pipeline by rerunning intermittent failures under explicit retry limits. Invoke it instead of manually rerunning the full suite or bolting retry logic onto CI scripts when the job is flaky-test containment inside pytest itself. The scope boundary is narrow: retry and report unstable pytest cases, not generic Python testing, broad CI orchestration, or a plain plugin listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures/)
