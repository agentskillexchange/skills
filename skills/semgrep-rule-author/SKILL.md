---
title: "Semgrep Rule Author"
description: "Semgrep Rule Author transforms natural language descriptions of code vulnerabilities or anti-patterns into production-ready Semgrep YAML rules.\nHow It Works\nDescribe a vulnerability pattern in plain English — such as “SQL injection via string concatenation in Python Flask routes” — and the skill generates a complete Semgrep rule with pattern, pattern-not, metavariable constraints, and metadata fields.\nKey Features\n\nSupports all Semgrep pattern operators including pattern-inside, pattern-either, and metavariable-regex\nAutomatically runs semgrep –validate to ensure rule syntax correctness\nGenerates test fixtures and runs semgrep –test to verify true/false positive behavior\nOutputs rules in Semgrep Registry format with proper severity, confidence, and CWE mappings\n\nUse Cases\nIdeal for security teams building custom rule packs, developers enforcing framework-specific patterns, and compliance teams mapping rules to OWASP Top 10 categories. Exports rules compatible with Semgrep Cloud Platform and semgrep-app."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Rule Author

Semgrep Rule Author transforms natural language descriptions of code vulnerabilities or anti-patterns into production-ready Semgrep YAML rules.
How It Works
Describe a vulnerability pattern in plain English — such as “SQL injection via string concatenation in Python Flask routes” — and the skill generates a complete Semgrep rule with pattern, pattern-not, metavariable constraints, and metadata fields.
Key Features

Supports all Semgrep pattern operators including pattern-inside, pattern-either, and metavariable-regex
Automatically runs semgrep –validate to ensure rule syntax correctness
Generates test fixtures and runs semgrep –test to verify true/false positive behavior
Outputs rules in Semgrep Registry format with proper severity, confidence, and CWE mappings

Use Cases
Ideal for security teams building custom rule packs, developers enforcing framework-specific patterns, and compliance teams mapping rules to OWASP Top 10 categories. Exports rules compatible with Semgrep Cloud Platform and semgrep-app.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-rule-author
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-rule-author` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-author/)
