---
title: "Biome Lint Migration Toolkit"
description: "Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting."
verification: "security_reviewed"
source: "https://github.com/biomejs/biome"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "biomejs/biome"
  github_stars: 24293
---

# Biome Lint Migration Toolkit

The Biome Lint Migration Toolkit streamlines the transition from ESLint and Prettier to the Biome unified toolchain. It parses your existing .eslintrc.json, .eslintrc.yml, and .prettierrc configurations, then generates an equivalent biome.json with mapped lint rules, formatter settings, and organize-imports configuration. The agent handles ESLint plugin mappings (eslint-plugin-react, @typescript-eslint) to Biome’s built-in nursery and recommended rule sets. It runs biome check –apply across your codebase to auto-fix formatting differences, then produces a diff report showing which ESLint rules have no Biome equivalent and need manual review. Includes support for biome.jsonc with comments, workspace-level overrides for monorepos, and CI integration snippets for GitHub Actions using the official biome/setup-biome action. Reduces toolchain complexity by replacing three tools (ESLint + Prettier + eslint-plugin-import) with a single Rust-based binary.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/biome-lint-migration-toolkit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/biome-lint-migration-toolkit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/biome-lint-migration-toolkit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-lint-migration-toolkit/)
