---
title: "Nx Workspace Generator Toolkit"
description: "Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness."
verification: "security_reviewed"
source: "https://github.com/nrwl/nx"
category:
  - "Templates & Workflows"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "nrwl/nx"
  github_stars: 28566
  npm_package: "@nx/devkit"
  npm_weekly_downloads: 29518517
---

# Nx Workspace Generator Toolkit

The Nx Workspace Generator Toolkit enables creation of powerful custom workspace generators for Nx monorepos using the @nrwl/devkit API. It generates files using the TypeTree pattern for type-safe template composition with EJS templating support. Schema.json validation ensures generator inputs are properly typed and validated before execution. The toolkit understands the Nx dependency graph, automatically updating tsconfig paths, project.json configurations, and workspace.json entries when new libraries or applications are scaffolded. It supports generator composition where complex generators delegate to simpler ones, and includes utilities for modifying existing files using AST transformations via ts-morph. The tool provides generators for common patterns including React components with Storybook stories, NestJS modules with Swagger decorators, shared utility libraries with proper barrel exports, and end-to-end test projects with Cypress or Playwright configurations. Dry-run mode previews all file changes before applying them to the workspace.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nx-workspace-generator-toolkit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/nx-workspace-generator-toolkit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/)
