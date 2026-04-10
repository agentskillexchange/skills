---
title: "ESLint Rule Conflict Detector"
description: "Analyzes .eslintrc configurations and extended rulesets using the ESLint Node.js API and eslint-config-inspector. Detects conflicting rules between Prettier, TypeScript-ESLint, and Airbnb presets, generating a unified conflict-free config."
slug: "eslint-rule-conflict-detector-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/"
---

# ESLint Rule Conflict Detector

Analyzes .eslintrc configurations and extended rulesets using the ESLint Node.js API and eslint-config-inspector. Detects conflicting rules between Prettier, TypeScript-ESLint, and Airbnb presets, generating a unified conflict-free config.

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
clawhub install eslint-rule-conflict-detector-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Rule Conflict Detector skill resolves the common pain point of conflicting ESLint rules across multiple configuration presets by performing deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load and resolve the complete effective configuration, and the eslint-config-inspector to visualize rule precedence.
The detector identifies conflicts between popular presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb, and eslint-config-standard. It maps each rule to its source configuration and highlights where downstream presets override upstream rules in ways that may cause unexpected behavior or contradictory formatting.
For Prettier integration specifically, the skill checks for rules that conflict with Prettier’s formatting decisions, going beyond what eslint-config-prettier covers by analyzing rule options and edge cases. It validates that @typescript-eslint rules properly extend their base ESLint counterparts rather than creating duplicate enforcement.
The output includes a detailed conflict report showing which rules clash, where they originate, and recommended resolutions. It can generate a unified .eslintrc.json that resolves all conflicts while preserving the intent of each preset. The skill also supports flat config format (eslint.config.js) analysis for ESLint v9+ and provides migration assistance from legacy to flat config.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/)
