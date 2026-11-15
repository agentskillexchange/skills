---
name: "Gate agent code changes with OpenQodex review"
slug: "gate-agent-code-changes-with-openqodex-review"
description: "Run diff-aware scanner and AI review gates before pushing Claude Code or Codex changes, with pinned scanners, isolated reviewer contexts, and optional pre-push enforcement."
github_stars: 247
verification: "security_reviewed"
source: "https://github.com/openqodex/openqodex"
author: "openqodex"
publisher_type: "open_source"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "openqodex/openqodex"
  github_stars: 247
  npm_package: "openqodex"
  npm_weekly_downloads: 1296
---

# Gate agent code changes with OpenQodex review

Run diff-aware scanner and AI review gates before pushing Claude Code or Codex changes, with pinned scanners, isolated reviewer contexts, and optional pre-push enforcement.

## Prerequisites

Node/npm, Git, OpenQodex CLI, Claude Code or Codex for full reviewer mode, scanner runtimes as needed by project language

## Installation

Install or set up from the source-backed instructions:

Run `npx openqodex init` for terminal setup, or install the agent skill with `npx skills add openqodex/openqodex`; then run or ask the agent to run `openqodex review` against the current change before pushing.

- Source: https://github.com/openqodex/openqodex

## Documentation

- https://qodex.ai/openqodex

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-agent-code-changes-with-openqodex-review/)
