---
title: "Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum"
description: "Use gotestsum when an agent needs to run `go test -json`, summarize failing packages and tests, emit CI-friendly artifacts, and optionally rerun flaky failures before handing a repair loop back to CI. Invoke this instead of plain `go test` when the real job is triage, reporting, and failure-focused supervision around a Go test run, not just executing tests once. The scope boundary is narrow and skill-shaped: gotestsum is the reporting, rerun, and CI-artifact layer for Go test workflows, not a generic Go framework, package manager, or broad test platform listing."
source: "https://github.com/gotestyourself/gotestsum"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gotestyourself/gotestsum"
  github_stars: 2600
---

# Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum

Use gotestsum when an agent needs to run `go test -json`, summarize failing packages and tests, emit CI-friendly artifacts, and optionally rerun flaky failures before handing a repair loop back to CI. Invoke this instead of plain `go test` when the real job is triage, reporting, and failure-focused supervision around a Go test run, not just executing tests once. The scope boundary is narrow and skill-shaped: gotestsum is the reporting, rerun, and CI-artifact layer for Go test workflows, not a generic Go framework, package manager, or broad test platform listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/)
