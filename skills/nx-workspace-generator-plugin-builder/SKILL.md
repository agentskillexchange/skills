---
name: "Nx Workspace Generator Plugin"
description: "Creates custom Nx workspace generators and executors for monorepo scaffolding using @nx/devkit. Builds project.json configurations, generator schemas with x-prompt UI hints, and TypeScript AST transformations via ts-morph for code generation."
category: "Templates & Workflows"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nx-workspace-generator-plugin-builder/"
---

# Nx Workspace Generator Plugin

Creates custom Nx workspace generators and executors for monorepo scaffolding using @nx/devkit. Builds project.json configurations, generator schemas with x-prompt UI hints, and TypeScript AST transformations via ts-morph for code generation.

## Overview

Overview

The Nx Workspace Generator Plugin skill enables agents to create custom Nx plugins that extend monorepo workflows with project generators, executors, and migrations. Using the `@nx/devkit` and `@nx/plugin` packages, the skill scaffolds a complete plugin structure with generator functions that create new libraries, applications, or configuration files based on user-provided schema inputs with interactive prompts.

How It Works

The agent generates a plugin using `npx nx generate @nx/plugin:plugin my-plugin` as the starting point, then creates custom generators inside `src/generators/`. Each generator has a `schema.json` defining input properties with JSON Schema types, `x-prompt` fields for interactive CLI input, default values, and enum choices. The generator function uses `@nx/devkit` utilities: `generateFiles()` for EJS template rendering, `addProjectConfiguration()` for project.json creation, `updateJson()` for tsconfig.base.json path aliases, and `installPackagesTask()` for dependency installation. For advanced code generation, the skill uses `ts-morph` to manipulate TypeScript ASTs — adding imports, modifying class decorators, inserting barrel exports, and updating module arrays.

Output and Testing

Produces a publishable Nx plugin with generators, executors, and EJS template files in `src/generators/<name>/files/`. Executors wrap CLI tools like `esbuild`, `jest`, or `docker build` with typed option schemas and process spawning via `child_process.execSync`. Includes e2e tests using `@nx/plugin/testing`‘s `createTreeWithEmptyWorkspace()` and `runGenerator()` to verify file creation and project graph updates. Supports Nx Cloud caching, affected commands, and task pipeline configuration in `nx.json`. Publishes to npm with `nx release` for versioning and changelog generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-plugin-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-plugin-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-plugin-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator-plugin-builder -a codex
```

### OpenClaw

```bash
clawhub install nx-workspace-generator-plugin-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nx-workspace-generator-plugin-builder/
