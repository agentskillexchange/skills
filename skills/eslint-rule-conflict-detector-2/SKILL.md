---
title: "ESLint Rule Conflict Detector"
description: "Analyzes .eslintrc configurations and extended rulesets using the ESLint Node.js API and eslint-config-inspector. Detects conflicting rules between Prettier, TypeScript-ESLint, and Airbnb presets, generating a unified conflict-free config."
verification: security_reviewed
source: "https://github.com/eslint/eslint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "eslint/eslint"
  github_stars: 27188
  npm_package: "eslint"
  npm_weekly_downloads: 120215107
---

# ESLint Rule Conflict Detector

The ESLint Rule Conflict Detector skill resolves the common pain point of conflicting ESLint rules across multiple configuration presets by performing deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load and resolve the complete effective configuration, and the eslint-config-inspector to visualize rule precedence.

The detector identifies conflicts between popular presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb, and eslint-config-standard. It maps each rule to its source configuration and highlights where downstream presets override upstream rules in ways that may cause unexpected behavior or contradictory formatting.

For Prettier integration specifically, the skill checks for rules that conflict with Prettier’s formatting decisions, going beyond what eslint-config-prettier covers by analyzing rule options and edge cases. It validates that @typescript-eslint rules properly extend their base ESLint counterparts rather than creating duplicate enforcement.

The output includes a detailed conflict report showing which rules clash, where they originate, and recommended resolutions. It can generate a unified .eslintrc.json that resolves all conflicts while preserving the intent of each preset. The skill also supports flat config format (eslint.config.js) analysis for ESLint v9+ and provides migration assistance from legacy to flat config.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/)
