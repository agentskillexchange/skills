---
title: Biome Lint Migration Toolkit
description: The Biome Lint Migration Toolkit streamlines the transition from ESLint
  and Prettier to the Biome unified toolchain. It parses your existing .eslintrc.json,
  .eslintrc.yml, and .prettierrc configurations, then generates an equivalent biome.json
  with mapped lint rules, formatter settings, and organize-imports configuration.
  The agent handles ESLint plugin mappings (eslint-plugin-react, @typescript-eslint)
  to Biome’s built-in nursery and recommended rule sets. It runs biome check –apply
  across your codebase to auto-fix formatting differences, then produces a diff report
  showing which ESLint rules have no Biome equivalent and need manual review. Includes
  support for biome.jsonc with comments, workspace-level overrides for monorepos,
  and CI integration snippets for GitHub Actions using the official biome/setup-biome
  action. Reduces toolchain complexity by replacing three tools (ESLint + Prettier
  + eslint-plugin-import) with a single Rust-based binary.
verification: security_reviewed
source: https://github.com/biomejs/biome
category:
- Developer Tools
framework:
- Claude Code
tool_ecosystem:
  github_repo: biomejs/biome
  github_stars: 24199
---

# Biome Lint Migration Toolkit

The Biome Lint Migration Toolkit streamlines the transition from ESLint and Prettier to the Biome unified toolchain. It parses your existing .eslintrc.json, .eslintrc.yml, and .prettierrc configurations, then generates an equivalent biome.json with mapped lint rules, formatter settings, and organize-imports configuration. The agent handles ESLint plugin mappings (eslint-plugin-react, @typescript-eslint) to Biome’s built-in nursery and recommended rule sets. It runs biome check –apply across your codebase to auto-fix formatting differences, then produces a diff report showing which ESLint rules have no Biome equivalent and need manual review. Includes support for biome.jsonc with comments, workspace-level overrides for monorepos, and CI integration snippets for GitHub Actions using the official biome/setup-biome action. Reduces toolchain complexity by replacing three tools (ESLint + Prettier + eslint-plugin-import) with a single Rust-based binary.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-lint-migration-toolkit/)
