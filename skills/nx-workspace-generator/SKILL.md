---
title: "Nx Workspace Generator"
description: "Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph."
slug: "nx-workspace-generator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/nx-workspace-generator/"
---

# Nx Workspace Generator

Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph.

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
clawhub install nx-workspace-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices.
The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects.
Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator/)
