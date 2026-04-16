---
title: "Shard, retry, and summarize Rust test runs with CI-friendly artifacts and failure isolation using cargo-nextest"
description: "Use cargo-nextest when an agent needs more reliable Rust test execution than cargo test, especially for sharding, retries, machine-readable output, and CI triage."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shard-retry-and-summarize-rust-test-runs-with-ci-friendly-artifacts-and-failure-isolation-using-cargo-nextest/)
