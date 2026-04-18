---
title: "Shard, retry, and summarize Rust test runs with CI-friendly artifacts and failure isolation using cargo-nextest"
description: "Use cargo-nextest when an agent needs more reliable Rust test execution than cargo test, especially for sharding, retries, machine-readable output, and CI triage."
verification: security_reviewed
source: "https://github.com/nextest-rs/nextest"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nextest-rs/nextest"
  github_stars: 2910
  ase_npm_package: "cargo-nextest"
  npm_weekly_downloads: 9751524
---

# Shard, retry, and summarize Rust test runs with CI-friendly artifacts and failure isolation using cargo-nextest

Tool: cargo-nextest. This skill is for agents that need to run Rust test suites with better scheduling, failure isolation, retries, and structured artifacts than the default test runner provides.

When to use it: invoke this in CI repair loops, flaky-test triage, or large Rust repositories where the agent needs to shard runs, rerun failures, or emit machine-readable results for downstream analysis. Using this skill is different from using the product normally because the operator workflow is specific: execute the suite under nextest, collect the artifacts, and turn failures into actionable repair or retry decisions.

Scope boundary: this is not a generic Rust testing listing and not a broad CI platform card. Its boundary is narrow: run and triage Rust tests with cargo-nextest when scheduling, retries, and failure summaries matter.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/shard-retry-and-summarize-rust-test-runs-with-ci-friendly-artifacts-and-failure-isolation-using-cargo-nextest
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/shard-retry-and-summarize-rust-test-runs-with-ci-friendly-artifacts-and-failure-isolation-using-cargo-nextest` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shard-retry-and-summarize-rust-test-runs-with-ci-friendly-artifacts-and-failure-isolation-using-cargo-nextest/)
