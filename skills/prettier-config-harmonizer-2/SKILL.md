---
title: "Prettier Config Harmonizer"
description: "Resolves Prettier formatting conflicts across monorepo packages using the Prettier API and @prettier/plugin-xml. Generates unified .prettierrc configs with per-package overrides and EditorConfig synchronization."
slug: "prettier-config-harmonizer-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prettier-config-harmonizer-2/"
---

# Prettier Config Harmonizer

Resolves Prettier formatting conflicts across monorepo packages using the Prettier API and @prettier/plugin-xml. Generates unified .prettierrc configs with per-package overrides and EditorConfig synchronization.

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
clawhub install prettier-config-harmonizer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prettier Config Harmonizer skill solves formatting inconsistencies in monorepo environments by analyzing and unifying Prettier configurations across packages. It uses the Prettier Node.js API (prettier.resolveConfig and prettier.getFileInfo) to scan each package for existing formatting preferences.
The skill reads all configuration sources — .prettierrc, .prettierrc.json, .prettierrc.yaml, prettier.config.js, and package.json prettier fields — across your monorepo packages. It identifies conflicting settings like differing tabWidth, printWidth, trailingComma, or singleQuote values and proposes a unified base configuration with targeted overrides.
Plugin compatibility is handled automatically. The skill detects usage of @prettier/plugin-xml, prettier-plugin-tailwindcss, prettier-plugin-organize-imports, and other community plugins, ensuring the generated config loads plugins in the correct order to avoid conflicts. It also generates .prettierignore files based on each package gitignore and build output directories.
The unified configuration includes workspace-level overrides using the Prettier overrides array with glob patterns for different file types and package directories. An accompanying .editorconfig file is generated to keep IDE formatting in sync, and the skill validates the final config by running prettier –check against a sample of files from each package.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prettier-config-harmonizer-2/)
