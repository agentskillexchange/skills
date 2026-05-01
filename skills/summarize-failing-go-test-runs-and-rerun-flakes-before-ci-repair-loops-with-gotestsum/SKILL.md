---
title: "Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum"
description: "Use gotestsum to turn noisy `go test` output into compact failure summaries, JUnit or JSON artifacts, and optional reruns of flaky tests before an agent starts fixing Go code."
verification: "listed"
source: "https://github.com/gotestyourself/gotestsum"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gotestyourself/gotestsum"
  github_stars: 2600
---

# Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum

Use gotestsum when an agent needs to run `go test -json`, summarize failing packages and tests, emit CI-friendly artifacts, and optionally rerun flaky failures before handing a repair loop back to CI. Invoke this instead of plain `go test` when the real job is triage, reporting, and failure-focused supervision around a Go test run, not just executing tests once. The scope boundary is narrow and skill-shaped: gotestsum is the reporting, rerun, and CI-artifact layer for Go test workflows, not a generic Go framework, package manager, or broad test platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/)
