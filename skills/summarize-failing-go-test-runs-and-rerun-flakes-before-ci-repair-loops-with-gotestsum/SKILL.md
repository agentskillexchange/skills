---
name: "Summarize failing Go test runs and rerun flakes before CI repair loops with gotestsum"
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

Requirements and caveats from upstream:
- The nerdfonts icons requires a font from [Nerd Fonts](https://www.nerdfonts.com/).
- Note that using --rerun-fails may require the use of other flags, depending on
- [moby](https://github.com/moby/moby/blob/master/hack/test/unit) (aka Docker)

Basic usage or getting-started notes:
- gotestsum runs tests using go test -json, prints formatted test output, and a summary of the test run.
- Download a binary from [releases](https://github.com/gotestyourself/gotestsum/releases), or build from
- source with go install gotest.tools/gotestsum@latest. To run without installing use

- Source: https://github.com/gotestyourself/gotestsum
- Extracted from upstream docs: https://raw.githubusercontent.com/gotestyourself/gotestsum/HEAD/README.md

## Documentation

- https://github.com/gotestyourself/gotestsum

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/summarize-failing-go-test-runs-and-rerun-flakes-before-ci-repair-loops-with-gotestsum/)
