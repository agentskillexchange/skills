---
title: "Nx Workspace Generator"
description: "Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph."
verification: "security_reviewed"
source: "https://github.com/nrwl/nx"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "nrwl/nx"
  github_stars: 28562
---

# Nx Workspace Generator

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices.

The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects.

Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/nx-workspace-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nx-workspace-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/nx-workspace-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator/)
