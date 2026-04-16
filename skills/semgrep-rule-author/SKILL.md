---
title: "Semgrep Rule Author"
description: "Generates custom Semgrep rules from natural language descriptions of vulnerability patterns. Uses semgrep –validate to verify rule syntax and semgrep –test to run against sample code fixtures automatically."
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-author/)
