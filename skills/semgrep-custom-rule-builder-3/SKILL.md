---
title: "Semgrep Custom Rule Builder"
description: "Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript."
slug: "semgrep-custom-rule-builder-3"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/"
---

# Semgrep Custom Rule Builder

Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript.

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
clawhub install semgrep-custom-rule-builder-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Custom Rule Builder skill helps security teams create precise static analysis rules using the Semgrep open-source SAST tool. It generates rules in Semgrep YAML format with proper pattern syntax, metavariable bindings, and fix suggestions.
The skill supports all Semgrep pattern operators including pattern-either for matching multiple code variants, pattern-not for exclusions, metavariable-regex for constraining captured variables, and metavariable-comparison for numeric checks. It leverages taint-mode analysis to track data flow from sources to sinks across function boundaries, essential for detecting injection vulnerabilities.
Rule generation covers common vulnerability patterns for Python (Django, Flask), Go (net/http, gin), and JavaScript (Express, React) frameworks. The skill creates rules with proper severity levels, CWE references, OWASP mappings, and actionable fix suggestions using the fix or fix-regex fields. It includes test case generation with semgrep –test compatible annotations marking expected true positives and negatives. Rules are validated against the Semgrep rule schema and tested against sample code snippets before deployment to Semgrep App or CI integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/)
