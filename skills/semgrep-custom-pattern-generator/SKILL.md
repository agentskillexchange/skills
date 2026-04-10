---
title: "Semgrep Custom Pattern Generator"
description: "Generates Semgrep SAST rules from vulnerability descriptions using the Semgrep CLI and semgrep-rules YAML schema. Supports metavariable patterns, taint tracking, and join rules for cross-function analysis."
slug: "semgrep-custom-pattern-generator"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-custom-pattern-generator/"
listed: true
---

# Semgrep Custom Pattern Generator

Generates Semgrep SAST rules from vulnerability descriptions using the Semgrep CLI and semgrep-rules YAML schema. Supports metavariable patterns, taint tracking, and join rules for cross-function analysis.

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
clawhub install semgrep-custom-pattern-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Custom Pattern Generator skill creates custom static analysis rules for security and code quality scanning. It translates vulnerability descriptions or insecure code patterns into Semgrep rule definitions using the official semgrep-rules YAML schema.
The skill supports the full range of Semgrep pattern operators including pattern, pattern-not, pattern-inside, pattern-either, and metavariable-pattern for complex matching logic. For security-focused rules, it generates taint-mode rules with proper source, sink, and sanitizer definitions that track data flow across function boundaries.
Advanced rule features are supported including join rules for cross-file analysis using the semgrep join mode, pattern-regex for matching string literals and comments, and metavariable-comparison for numeric constraint checking. Each rule includes proper metadata following the semgrep-rule-schema with cwe, owasp, confidence, and impact fields.
Validation is performed using the semgrep –validate flag against the generated YAML, and the skill runs semgrep –test against provided test fixtures to verify true positives and false negative handling. Rules are organized into rulesets compatible with the Semgrep Registry publishing format, ready for use with semgrep ci in your CI pipeline.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-generator/)
