---
title: "Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum"
slug: "summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum"
description: "Use gotestsum to turn noisy `go test` output into compact failure summaries, JUnit or JSON artifacts, and optional reruns of flaky tests before an agent starts fixing Go code."
github_stars: 2600
verification: "security_reviewed"
source: "https://github.com/gotestyourself/gotestsum"
author: "gotestyourself maintainers"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "gotestyourself/gotestsum"
  github_stars: 2600
---

# Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum

Use gotestsum to turn noisy `go test` output into compact failure summaries, JUnit or JSON artifacts, and optional reruns of flaky tests before an agent starts fixing Go code.

## Prerequisites

gotestsum, Go toolchain

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a release binary, or install from source with `go install gotest.tools/gotestsum@latest`.
```

## Documentation

- https://github.com/gotestyourself/gotestsum

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/)
