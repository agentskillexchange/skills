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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/)
