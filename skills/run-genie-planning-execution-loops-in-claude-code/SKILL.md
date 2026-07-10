---
name: "Run Genie planning and execution loops in Claude Code"
slug: "run-genie-planning-execution-loops-in-claude-code"
description: "Use Genie to turn a vague coding request into Claude Code brainstorm, wish, work, and review loops backed by markdown plans and local SQLite state."
github_stars: 323
verification: "security_reviewed"
source: "https://github.com/automagik-dev/genie"
author: "Automagik"
publisher_type: "company"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "automagik-dev/genie"
  github_stars: 323
---

# Run Genie planning and execution loops in Claude Code

Use Genie to turn a vague coding request into Claude Code brainstorm, wish, work, and review loops backed by markdown plans and local SQLite state.

## Prerequisites

Claude Code, Genie CLI, git, Bun-powered Genie runtime, and a repository where Genie can create .genie markdown documents and a local SQLite state file.

## Installation

Basic usage or getting-started notes:
- Every release is cosign-signed (keyless OIDC) with SLSA provenance; the installer verifies the binary — via gh attestation verify, falling back to cosign verify-blob — before it runs.
- Then, from inside your repo, run genie setup to configure Genie and wire up its Claude Code hooks. genie doctor checks the install at any time.
- The lifecycle runs as Claude Code skills. Open your repository in Claude Code and go:

- Source: https://github.com/automagik-dev/genie
- Extracted from upstream docs: https://raw.githubusercontent.com/automagik-dev/genie/HEAD/README.md

## Documentation

- https://docs.automagik.dev/genie

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-genie-planning-execution-loops-in-claude-code/)
