---
name: "Semgrep Rule Author"
description: "Generates custom Semgrep rules from natural language descriptions of vulnerability patterns. Uses semgrep -validate to verify rule syntax and semgrep -test to run against sample code fixtures automatically."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-rule-author/"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
---

# Semgrep Rule Author

Semgrep Rule Author transforms natural language descriptions of code vulnerabilities or anti-patterns into production-ready Semgrep YAML rules.
How It Works
Describe a vulnerability pattern in plain English — such as &#8220;SQL injection via string concatenation in Python Flask routes&#8221; — and the skill generates a complete Semgrep rule with pattern, pattern-not, metavariable constraints, and metadata fields.
Key Features

Supports all Semgrep pattern operators including pattern-inside, pattern-either, and metavariable-regex
Automatically runs semgrep -validate to ensure rule syntax correctness
Generates test fixtures and runs semgrep -test to verify true/false positive behavior
Outputs rules in Semgrep Registry format with proper severity, confidence, and CWE mappings

Use Cases
Ideal for security teams building custom rule packs, developers enforcing framework-specific patterns, and compliance teams mapping rules to OWASP Top 10 categories. Exports rules compatible with Semgrep Cloud Platform and semgrep-app.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-author/)
