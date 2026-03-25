---
name: "Prettier Config Harmonizer"
description: "Resolves Prettier formatting conflicts across monorepo packages using the Prettier API and @prettier/plugin-xml. Generates unified .prettierrc configs with per-package overrides and EditorConfig synchronization."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prettier-config-harmonizer-2/"
---

# Prettier Config Harmonizer

Resolves Prettier formatting conflicts across monorepo packages using the Prettier API and @prettier/plugin-xml. Generates unified .prettierrc configs with per-package overrides and EditorConfig synchronization.

## Overview

The Prettier Config Harmonizer skill solves formatting inconsistencies in monorepo environments by analyzing and unifying Prettier configurations across packages. It uses the Prettier Node.js API (prettier.resolveConfig and prettier.getFileInfo) to scan each package for existing formatting preferences.

The skill reads all configuration sources — .prettierrc, .prettierrc.json, .prettierrc.yaml, prettier.config.js, and package.json prettier fields — across your monorepo packages. It identifies conflicting settings like differing tabWidth, printWidth, trailingComma, or singleQuote values and proposes a unified base configuration with targeted overrides.

Plugin compatibility is handled automatically. The skill detects usage of @prettier/plugin-xml, prettier-plugin-tailwindcss, prettier-plugin-organize-imports, and other community plugins, ensuring the generated config loads plugins in the correct order to avoid conflicts. It also generates .prettierignore files based on each package gitignore and build output directories.

The unified configuration includes workspace-level overrides using the Prettier overrides array with glob patterns for different file types and package directories. An accompanying .editorconfig file is generated to keep IDE formatting in sync, and the skill validates the final config by running prettier –check against a sample of files from each package.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prettier-config-harmonizer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prettier-config-harmonizer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prettier-config-harmonizer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prettier-config-harmonizer-2 -a codex
```

### OpenClaw

```bash
clawhub install prettier-config-harmonizer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prettier-config-harmonizer-2/
