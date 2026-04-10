---
title: "Biome Lint Migration Toolkit"
description: "Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting."
slug: "biome-lint-migration-toolkit"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/biomejs/biome"
tool_ecosystem:
  github_repo: "biomejs/biome"
  github_stars: 24293
---

# Biome Lint Migration Toolkit

Automates migration from ESLint and Prettier to Biome (formerly Rome) by parsing .eslintrc and .prettierrc configs, mapping rules to biome.json equivalents, and running biome check –apply for bulk reformatting.

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
clawhub install biome-lint-migration-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Biome Lint Migration Toolkit streamlines the transition from ESLint and Prettier to the Biome unified toolchain. It parses your existing .eslintrc.json, .eslintrc.yml, and .prettierrc configurations, then generates an equivalent biome.json with mapped lint rules, formatter settings, and organize-imports configuration. The agent handles ESLint plugin mappings (eslint-plugin-react, @typescript-eslint) to Biome’s built-in nursery and recommended rule sets. It runs biome check –apply across your codebase to auto-fix formatting differences, then produces a diff report showing which ESLint rules have no Biome equivalent and need manual review. Includes support for biome.jsonc with comments, workspace-level overrides for monorepos, and CI integration snippets for GitHub Actions using the official biome/setup-biome action. Reduces toolchain complexity by replacing three tools (ESLint + Prettier + eslint-plugin-import) with a single Rust-based binary.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/biome-lint-migration-toolkit/)
