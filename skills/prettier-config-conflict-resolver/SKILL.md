---
title: "Prettier Config Conflict Resolver"
description: "Detects and resolves conflicts between Prettier, ESLint, and EditorConfig formatting rules using the Prettier resolveConfig API and eslint-config-prettier compatibility checker."
slug: "prettier-config-conflict-resolver"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prettier-config-conflict-resolver/"
---

# Prettier Config Conflict Resolver

Detects and resolves conflicts between Prettier, ESLint, and EditorConfig formatting rules using the Prettier resolveConfig API and eslint-config-prettier compatibility checker.

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
clawhub install prettier-config-conflict-resolver
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prettier Config Conflict Resolver skill identifies formatting rule conflicts across the Prettier, ESLint, and EditorConfig toolchain that cause inconsistent code style and CI failures. It uses the Prettier resolveConfig Node.js API to load effective Prettier configuration for each file path and compares settings against ESLint rules loaded via the ESLint CLIEngine. The skill runs eslint-config-prettier compatibility checks to detect ESLint rules that conflict with Prettier formatting, such as conflicting indent, quotes, and semi rules. It parses .editorconfig files to verify alignment with Prettier settings for tab width, end-of-line characters, and max line length. The tool generates a unified configuration recommendation that eliminates conflicts while preserving team preferences. It supports monorepo setups with per-package overrides and can output merged configurations in JSON, YAML, and TOML formats for .prettierrc, .eslintrc, and .editorconfig files.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-config-conflict-resolver/)
