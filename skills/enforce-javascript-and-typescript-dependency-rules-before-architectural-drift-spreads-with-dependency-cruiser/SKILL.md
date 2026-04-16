---
title: "Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser"
description: "Scan a JS or TS codebase for forbidden imports, circular dependencies, orphaned modules, and other dependency-rule violations before they turn into structural drift."
verification: "listed"
source: "https://github.com/sverweij/dependency-cruiser"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sverweij/dependency-cruiser"
  github_stars: 6557
  ase_npm_package: "dependency-cruiser"
  npm_weekly_downloads: 5181412
---

# Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser

Use dependency-cruiser when an agent needs to check whether a JavaScript or TypeScript codebase still respects architecture boundaries, import rules, and package dependency expectations. It is the right invocation when you want a dependency-policy gate, violation report, or dependency graph for CI and review, rather than using a generic package tool normally. The scope boundary is narrow and skill-shaped: it validates and reports dependency structure against explicit rules, not general linting, package management, or broad code analysis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-javascript-and-typescript-dependency-rules-before-architectural-drift-spreads-with-dependency-cruiser/)
