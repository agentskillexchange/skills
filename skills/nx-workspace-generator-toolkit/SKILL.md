---
name: "Nx Workspace Generator Toolkit"
description: "Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness."
category: "Templates & Workflows"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Nx Workspace Generator Toolkit

Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness.

## Overview

The Nx Workspace Generator Toolkit enables creation of powerful custom workspace generators for Nx monorepos using the @nrwl/devkit API. It generates files using the TypeTree pattern for type-safe template composition with EJS templating support. Schema.json validation ensures generator inputs are properly typed and validated before execution. The toolkit understands the Nx dependency graph, automatically updating tsconfig paths, project.json configurations, and workspace.json entries when new libraries or applications are scaffolded. It supports generator composition where complex generators delegate to simpler ones, and includes utilities for modifying existing files using AST transformations via ts-morph. The tool provides generators for common patterns including React components with Storybook stories, NestJS modules with Swagger decorators, shared utility libraries with proper barrel exports, and end-to-end test projects with Cypress or Playwright configurations. Dry-run mode previews all file changes before applying them to the workspace.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-toolkit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-toolkit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-toolkit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-toolkit -a codex
```

### OpenClaw

```bash
clawhub install nx-workspace-generator-toolkit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/
