---
title: "Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt"
description: "Use treefmt when an agent needs one repo-level formatting plan across multiple languages instead of stitching formatter commands together ad hoc."
verification: "security_reviewed"
source: "https://github.com/numtide/treefmt"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "numtide/treefmt"
  github_stars: 977
  ase_npm_package: "treefmt"
  npm_weekly_downloads: 18627
---

# Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt

Tool: treefmt. This skill gives an agent a bounded repository-maintenance job: define one formatter plan for a mixed-language codebase and apply it consistently so generated edits stay predictable.


When to use it: invoke this before review, before sweeping refactors, or when a repository has several language-specific formatters and the agent needs one stable entry point for formatting. Using this skill is different from using the product normally because the workflow is orchestration-focused: declare the formatter set once, run it at repo scope, and hand back a clean predictable formatting pass.


Scope boundary: this is not a generic formatter listing and not a language-specific style tool card. Its boundary is narrower: coordinate multiple existing formatters from one repo-level plan with treefmt.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-one-formatter-plan-across-a-mixed-language-repo-and-keep-generated-edits-predictable-with-treefmt/)
