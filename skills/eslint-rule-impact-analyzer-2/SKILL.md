---
name: "ESLint Rule Impact Analyzer"
description: "Measures the impact of enabling new ESLint rules across a codebase using the ESLint Node.js API and @typescript-eslint/parser. Generates violation heatmaps, estimates auto-fix coverage, and prioritizes rules by fix effort."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
---

# ESLint Rule Impact Analyzer

The ESLint Rule Impact Analyzer skill helps teams adopt stricter linting rules incrementally by measuring the real impact before enabling them. Using the ESLint Node.js API programmatically, it runs candidate rules against the entire codebase without modifying configuration files. For each rule, it counts violations per file, calculates auto-fix coverage using the fix metadata, and estimates manual remediation effort based on violation complexity scoring. The skill generates interactive heatmaps showing violation density across directories, helping teams identify hotspots. Supports @typescript-eslint/parser rules, eslint-plugin-react, eslint-plugin-import, and custom rule packages. Can simulate enabling multiple rules simultaneously to detect interaction effects. Outputs prioritized adoption plans as markdown or Jira tickets with per-rule effort estimates. Integrates with SonarQube for combined static analysis reporting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-impact-analyzer-2/)
