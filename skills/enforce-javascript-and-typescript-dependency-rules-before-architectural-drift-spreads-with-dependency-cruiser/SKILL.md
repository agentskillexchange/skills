---
title: "Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser"
description: "Scan a JS or TS codebase for forbidden imports, circular dependencies, orphaned modules, and other dependency-rule violations before they turn into structural drift."
verification: "listed"
source: "https://github.com/sverweij/dependency-cruiser"
author: "sverweij"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "sverweij/dependency-cruiser"
  github_stars: 6557
  npm_package: "dependency-cruiser"
  npm_weekly_downloads: 5181412
---

# Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser

Scan a JS or TS codebase for forbidden imports, circular dependencies, orphaned modules, and other dependency-rule violations before they turn into structural drift.

## Prerequisites

Node.js, npm or pnpm

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install --save-dev dependency-cruiser` (or the yarn/pnpm equivalent), run `npx depcruise --init` to create a config, then run `npx depcruise` in CI or review workflows.
```

## Documentation

- https://github.com/sverweij/dependency-cruiser

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-javascript-and-typescript-dependency-rules-before-architectural-drift-spreads-with-dependency-cruiser/)
