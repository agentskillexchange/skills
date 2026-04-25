---
title: "Prettier Config Conflict Resolver"
description: "Detects and resolves conflicts between Prettier, ESLint, and EditorConfig formatting rules using the Prettier resolveConfig API and eslint-config-prettier compatibility checker."
verification: "security_reviewed"
source: "https://github.com/prettier/prettier"
category:
  - "Code Quality & Review"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prettier/prettier"
  github_stars: 51820
  npm_package: "prettier"
  npm_weekly_downloads: 90506007
---

# Prettier Config Conflict Resolver

The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prettier-config-conflict-resolver/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prettier-config-conflict-resolver
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prettier-config-conflict-resolver`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-config-conflict-resolver/)
