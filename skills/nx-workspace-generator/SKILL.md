---
title: Nx Workspace Generator
description: The Nx Workspace Generator skill manages monorepo scaffolding and code
  generation through the Nx build system. It uses @nx/devkit to create custom workspace
  generators that produce libraries, applications, and shared utilities following
  monorepo best practices. The skill leverages the Nx plugin API for creating custom
  executors and generators that integrate with the Nx dependency graph. It supports
  automatic project.json configuration, tsconfig path mapping, and build target setup
  for generated projects. Key features include intelligent code generation with AST
  manipulation via ts-morph, automatic barrel file updates, and integration with Nx
  affected commands for incremental builds. The skill handles cross-project dependency
  management, generates move and remove generators for safe refactoring, and supports
  Nx Cloud integration for distributed task caching and execution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nx-workspace-generator/
category:
- Templates &amp; Workflows
framework:
- Claude Code
---

# Nx Workspace Generator

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices. The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects. Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator/)
