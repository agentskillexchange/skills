---
name: "Prettier Config Conflict Resolver"
description: "Detects and resolves conflicts between Prettier, ESLint, and EditorConfig formatting rules using the Prettier resolveConfig API and eslint-config-prettier compatibility checker."
category: "Code Quality & Review"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prettier-config-conflict-resolver/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "eslint"  # from ase_tool_match
  github_stars: 27186  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 109028697  # from ase_npm_downloads
  github_repo: "eslint/eslint"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prettier Config Conflict Resolver

Detects and resolves conflicts between Prettier, ESLint, and EditorConfig formatting rules using the Prettier resolveConfig API and eslint-config-prettier compatibility checker.

## Overview

The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prettier-config-conflict-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prettier-config-conflict-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prettier-config-conflict-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prettier-config-conflict-resolver -a codex
```

### OpenClaw

```bash
clawhub install prettier-config-conflict-resolver
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prettier-config-conflict-resolver/
