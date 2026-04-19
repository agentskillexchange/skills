---
title: "Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt"
description: "Tool: treefmt. This skill gives an agent a bounded repository-maintenance job: define one formatter plan for a mixed-language codebase and apply it consistently so generated edits stay predictable. When to use it: invoke this before review, before sweeping refactors, or when a repository has several language-specific formatters and the agent needs one stable entry point for formatting. Using this skill is different from using the product normally because the workflow is orchestration-focused: declare the formatter set once, run it at repo scope, and hand back a clean predictable formatting pass. Scope boundary: this is not a generic formatter listing and not a language-specific style tool card. Its boundary is narrower: coordinate multiple existing formatters from one repo-level plan with treefmt."
source: "https://github.com/numtide/treefmt"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "numtide/treefmt"
  github_stars: 977
  npm_package: "treefmt"
  npm_weekly_downloads: 18627
---

# Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt

Tool: treefmt. This skill gives an agent a bounded repository-maintenance job: define one formatter plan for a mixed-language codebase and apply it consistently so generated edits stay predictable. When to use it: invoke this before review, before sweeping refactors, or when a repository has several language-specific formatters and the agent needs one stable entry point for formatting. Using this skill is different from using the product normally because the workflow is orchestration-focused: declare the formatter set once, run it at repo scope, and hand back a clean predictable formatting pass. Scope boundary: this is not a generic formatter listing and not a language-specific style tool card. Its boundary is narrower: coordinate multiple existing formatters from one repo-level plan with treefmt.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-one-formatter-plan-across-a-mixed-language-repo-and-keep-generated-edits-predictable-with-treefmt/)
