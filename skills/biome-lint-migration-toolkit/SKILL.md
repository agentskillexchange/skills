---
name: "Biome Lint Migration Toolkit"
description: "Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/biome-lint-migration-toolkit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
