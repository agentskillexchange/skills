---
title: "Nx Workspace Generator"
description: "Creates and manages Nx monorepo workspace generators using @nx/devkit and the Nx plugin API. Generates libraries, applications, and custom executors with automatic dependency graph updates via nx graph."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nx-workspace-generator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# Nx Workspace Generator

The Nx Workspace Generator skill manages monorepo scaffolding and code generation through the Nx build system. It uses @nx/devkit to create custom workspace generators that produce libraries, applications, and shared utilities following monorepo best practices.

The skill leverages the Nx plugin API for creating custom executors and generators that integrate with the Nx dependency graph. It supports automatic project.json configuration, tsconfig path mapping, and build target setup for generated projects.

Key features include intelligent code generation with AST manipulation via ts-morph, automatic barrel file updates, and integration with Nx affected commands for incremental builds. The skill handles cross-project dependency management, generates move and remove generators for safe refactoring, and supports Nx Cloud integration for distributed task caching and execution.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-workspace-generator/)
