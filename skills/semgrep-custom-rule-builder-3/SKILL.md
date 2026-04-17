---
title: "Semgrep Custom Rule Builder"
description: "Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
---

# Semgrep Custom Rule Builder

The Semgrep Custom Rule Builder skill helps security teams create precise static analysis rules using the Semgrep open-source SAST tool. It generates rules in Semgrep YAML format with proper pattern syntax, metavariable bindings, and fix suggestions.

The skill supports all Semgrep pattern operators including pattern-either for matching multiple code variants, pattern-not for exclusions, metavariable-regex for constraining captured variables, and metavariable-comparison for numeric checks. It leverages taint-mode analysis to track data flow from sources to sinks across function boundaries, essential for detecting injection vulnerabilities.

Rule generation covers common vulnerability patterns for Python (Django, Flask), Go (net/http, gin), and JavaScript (Express, React) frameworks. The skill creates rules with proper severity levels, CWE references, OWASP mappings, and actionable fix suggestions using the fix or fix-regex fields. It includes test case generation with semgrep –test compatible annotations marking expected true positives and negatives. Rules are validated against the Semgrep rule schema and tested against sample code snippets before deployment to Semgrep App or CI integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-custom-rule-builder-3
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-custom-rule-builder-3` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/)
