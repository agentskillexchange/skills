---
title: ESLint Rule Conflict Detector
description: The ESLint Rule Conflict Detector skill resolves the common pain point
  of conflicting ESLint rules across multiple configuration presets by performing
  deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load
  and resolve the complete effective configuration, and the eslint-config-inspector
  to visualize rule precedence. The detector identifies conflicts between popular
  presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb,
  and eslint-config-standard. It maps each rule to its source configuration and highlights
  where downstream presets override upstream rules in ways that may cause unexpected
  behavior or contradictory formatting. For Prettier integration specifically, the
  skill checks for rules that conflict with Prettier’s formatting decisions, going
  beyond what eslint-config-prettier covers by analyzing rule options and edge cases.
  It validates that @typescript-eslint rules properly extend their base ESLint counterparts
  rather than creating duplicate enforcement. The output includes a detailed conflict
  report showing which rules clash, where they originate, and recommended resolutions.
  It can generate a unified .eslintrc.json that resolves all conflicts while preserving
  the intent of each preset. The skill also supports flat config format (eslint.config.js)
  analysis for ESLint v9+ and provides migration assistance from legacy to flat config.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/
category:
- Code Quality &amp; Review
framework:
- Codex
---

# ESLint Rule Conflict Detector

The ESLint Rule Conflict Detector skill resolves the common pain point of conflicting ESLint rules across multiple configuration presets by performing deep analysis of rule inheritance chains. It uses the ESLint Node.js API to load and resolve the complete effective configuration, and the eslint-config-inspector to visualize rule precedence. The detector identifies conflicts between popular presets including eslint-config-prettier, @typescript-eslint/eslint-plugin, eslint-config-airbnb, and eslint-config-standard. It maps each rule to its source configuration and highlights where downstream presets override upstream rules in ways that may cause unexpected behavior or contradictory formatting. For Prettier integration specifically, the skill checks for rules that conflict with Prettier’s formatting decisions, going beyond what eslint-config-prettier covers by analyzing rule options and edge cases. It validates that @typescript-eslint rules properly extend their base ESLint counterparts rather than creating duplicate enforcement. The output includes a detailed conflict report showing which rules clash, where they originate, and recommended resolutions. It can generate a unified .eslintrc.json that resolves all conflicts while preserving the intent of each preset. The skill also supports flat config format (eslint.config.js) analysis for ESLint v9+ and provides migration assistance from legacy to flat config.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-conflict-detector-2/)
