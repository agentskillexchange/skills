---
name: "Nx Workspace Generator"
description: "Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nx-workspace-generator/"
---

# Nx Workspace Generator

Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph.

## Overview

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices.

The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects.

Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nx-workspace-generator -a codex
```

### OpenClaw

```bash
clawhub install nx-workspace-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nx-workspace-generator/
