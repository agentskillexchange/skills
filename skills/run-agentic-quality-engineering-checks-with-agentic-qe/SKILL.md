---
name: "Run agentic quality engineering checks with Agentic QE"
slug: "run-agentic-quality-engineering-checks-with-agentic-qe"
description: "Configure Agentic QE in a repository so a coding agent can generate tests, inspect coverage gaps, investigate flaky behavior, and report reviewable quality evidence."
github_stars: 495
verification: "security_reviewed"
source: "https://github.com/proffesor-for-testing/agentic-qe"
author: "Dragan Spiridonov / proffesor-for-testing"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "proffesor-for-testing/agentic-qe"
  github_stars: 495
  npm_package: "agentic-qe"
  npm_weekly_downloads: 44764
---

# Run agentic quality engineering checks with Agentic QE

Configure Agentic QE in a repository so a coding agent can generate tests, inspect coverage gaps, investigate flaky behavior, and report reviewable quality evidence.

## Prerequisites

Node.js 22.13.0 or newer, npm 10 or newer, the agentic-qe CLI, and a supported coding-agent client such as Claude Code, Codex CLI, GitHub Copilot, Cursor, Cline, OpenCode, Kiro, Roo Code, Windsurf, or Continue.dev

## Installation

Install or set up from the source-backed instructions:

Run npm install -g agentic-qe, then cd into the target repository and run aqe init --auto. Add client-specific setup flags such as --with-codex, --with-cursor, or --with-all-platforms when needed, then verify with aqe health.

- Source: https://github.com/proffesor-for-testing/agentic-qe

## Documentation

- https://agentic-qe.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agentic-quality-engineering-checks-with-agentic-qe/)
