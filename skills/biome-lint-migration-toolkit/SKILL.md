---
name: "Biome Lint Migration Toolkit"
description: "Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/biome-lint-migration-toolkit/"
tool_ecosystem:
  tool: "eslint"
  github_stars: 27185
  npm_weekly_downloads: 109028697
  github_repo: "eslint/eslint"
  license: "MIT"
  maintained: true
---

# Biome Lint Migration Toolkit

Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting.

## Overview

The Biome Lint Migration Toolkit streamlines the transition from ESLint and Prettier to the Biome unified toolchain. It parses your existing .eslintrc.json, .eslintrc.yml, and .prettierrc configurations, then generates an equivalent biome.json with mapped lint rules, formatter settings, and organize-imports configuration. The agent handles ESLint plugin mappings (eslint-plugin-react, @typescript-eslint) to Biome’s built-in nursery and recommended rule sets. It runs biome check –apply across your codebase to auto-fix formatting differences, then produces a diff report showing which ESLint rules have no Biome equivalent and need manual review. Includes support for biome.jsonc with comments, workspace-level overrides for monorepos, and CI integration snippets for GitHub Actions using the official biome/setup-biome action. Reduces toolchain complexity by replacing three tools (ESLint + Prettier + eslint-plugin-import) with a single Rust-based binary.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill biome-lint-migration-toolkit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill biome-lint-migration-toolkit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill biome-lint-migration-toolkit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill biome-lint-migration-toolkit -a codex
```

### OpenClaw

```bash
clawhub install biome-lint-migration-toolkit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/biome-lint-migration-toolkit/
