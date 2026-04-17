---
title: "ESLint Rule Conflict Detector"
description: "The ESLint Rule Conflict Detector skill resolves the common pain point of conflicting ESLint rules across multiple configuration presets by performing deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load and resolve the complete effective configuration, and the eslint-config-inspector to visualize rule precedence.\nThe detector identifies conflicts between popular presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb, and eslint-config-standard. It maps each rule to its source configuration and highlights where downstream presets override upstream rules in ways that may cause unexpected behavior or contradictory formatting.\nFor Prettier integration specifically, the skill checks for rules that conflict with Prettier’s formatting decisions, going beyond what eslint-config-prettier covers by analyzing rule options and edge cases. It validates that @typescript-eslint rules properly extend their base ESLint counterparts rather than creating duplicate enforcement.\nThe output includes a detailed conflict report showing which rules clash, where they originate, and recommended resolutions. It can generate a unified .eslintrc.json that resolves all conflicts while preserving the intent of each preset. The skill also supports flat config format (eslint.config.js) analysis for ESLint v9+ and provides migration assistance from legacy to flat config."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  ase_npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Conflict Detector

The ESLint Rule Conflict Detector skill resolves the common pain point of conflicting ESLint rules across multiple configuration presets by performing deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load and resolve the complete effective configuration, and the eslint-config-inspector to visualize rule precedence.
The detector identifies conflicts between popular presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb, and eslint-config-standard. It maps each rule to its source configuration and highlights where downstream presets override upstream rules in ways that may cause unexpected behavior or contradictory formatting.
For Prettier integration specifically, the skill checks for rules that conflict with Prettier’s formatting decisions, going beyond what eslint-config-prettier covers by analyzing rule options and edge cases. It validates that @typescript-eslint rules properly extend their base ESLint counterparts rather than creating duplicate enforcement.
The output includes a detailed conflict report showing which rules clash, where they originate, and recommended resolutions. It can generate a unified .eslintrc.json that resolves all conflicts while preserving the intent of each preset. The skill also supports flat config format (eslint.config.js) analysis for ESLint v9+ and provides migration assistance from legacy to flat config.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/eslint-rule-conflict-detector-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/eslint-rule-conflict-detector-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/)
