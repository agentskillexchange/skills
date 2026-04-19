---
title: "Nx Workspace Generator"
description: "The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices. The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects. Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution."
source: "https://agentskillexchange.com/skills/nx-workspace-generator/"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# Nx Workspace Generator

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices. The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects. Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator/)
