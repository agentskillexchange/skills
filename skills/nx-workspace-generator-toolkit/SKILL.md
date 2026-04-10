---
title: "Nx Workspace Generator Toolkit"
description: "Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness."
slug: "nx-workspace-generator-toolkit"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/"
---

# Nx Workspace Generator Toolkit

Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install nx-workspace-generator-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Nx Workspace Generator Toolkit enables creation of powerful custom workspace generators for Nx monorepos using the @nrwl/devkit API. It generates files using the TypeTree pattern for type-safe template composition with EJS templating support. Schema.json validation ensures generator inputs are properly typed and validated before execution. The toolkit understands the Nx dependency graph, automatically updating tsconfig paths, project.json configurations, and workspace.json entries when new libraries or applications are scaffolded. It supports generator composition where complex generators delegate to simpler ones, and includes utilities for modifying existing files using AST transformations via ts-morph. The tool provides generators for common patterns including React components with Storybook stories, NestJS modules with Swagger decorators, shared utility libraries with proper barrel exports, and end-to-end test projects with Cypress or Playwright configurations. Dry-run mode previews all file changes before applying them to the workspace.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/)
