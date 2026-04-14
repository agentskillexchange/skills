---
title: "Nx Workspace Generator Toolkit"
description: "Creates and manages custom Nx workspace generators using @nrwl/devkit with TypeTree file generation and schema.json validation. Automates monorepo library and app scaffolding with dependency graph awareness."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
---

# Nx Workspace Generator Toolkit

The Nx Workspace Generator Toolkit enables creation of powerful custom workspace generators for Nx monorepos using the @nrwl/devkit API. It generates files using the TypeTree pattern for type-safe template composition with EJS templating support. Schema.json validation ensures generator inputs are properly typed and validated before execution. The toolkit understands the Nx dependency graph, automatically updating tsconfig paths, project.json configurations, and workspace.json entries when new libraries or applications are scaffolded. It supports generator composition where complex generators delegate to simpler ones, and includes utilities for modifying existing files using AST transformations via ts-morph. The tool provides generators for common patterns including React components with Storybook stories, NestJS modules with Swagger decorators, shared utility libraries with proper barrel exports, and end-to-end test projects with Cypress or Playwright configurations. Dry-run mode previews all file changes before applying them to the workspace.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator-toolkit/)
