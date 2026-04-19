---
title: "Shard, retry, and summarize Rust test runs with CI-friendly artifacts and failure isolation using cargo-nextest"
description: "Tool: cargo-nextest. This skill is for agents that need to run Rust test suites with better scheduling, failure isolation, retries, and structured artifacts than the default test runner provides. When to use it: invoke this in CI repair loops, flaky-test triage, or large Rust repositories where the agent needs to shard runs, rerun failures, or emit machine-readable results for downstream analysis. Using this skill is different from using the product normally because the operator workflow is specific: execute the suite under nextest, collect the artifacts, and turn failures into actionable repair or retry decisions. Scope boundary: this is not a generic Rust testing listing and not a broad CI platform card. Its boundary is narrow: run and triage Rust tests with cargo-nextest when scheduling, retries, and failure summaries matter."
source: "https://github.com/nextest-rs/nextest"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nextest-rs/nextest"
  github_stars: 2910
  npm_package: "cargo-nextest"
  npm_weekly_downloads: 9751524
---

# Shard, retry, and summarize Rust test runs with CI-friendly artifacts and failure isolation using cargo-nextest

Tool: cargo-nextest. This skill is for agents that need to run Rust test suites with better scheduling, failure isolation, retries, and structured artifacts than the default test runner provides. When to use it: invoke this in CI repair loops, flaky-test triage, or large Rust repositories where the agent needs to shard runs, rerun failures, or emit machine-readable results for downstream analysis. Using this skill is different from using the product normally because the operator workflow is specific: execute the suite under nextest, collect the artifacts, and turn failures into actionable repair or retry decisions. Scope boundary: this is not a generic Rust testing listing and not a broad CI platform card. Its boundary is narrow: run and triage Rust tests with cargo-nextest when scheduling, retries, and failure summaries matter.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shard-retry-and-summarize-rust-test-runs-with-ci-friendly-artifacts-and-failure-isolation-using-cargo-nextest/)
