---
name: Semgrep Custom Rule Builder
description: Creates custom Semgrep SAST rules using the semgrep CLI and rule schema
  YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking
  for detecting framework-specific vulnerabilities in Python, Go, and JavaScript.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/
category:
- Code Quality &amp; Review
framework:
- MCP
---
# Semgrep Custom Rule Builder

The Semgrep Custom Rule Builder skill helps security teams create precise static analysis rules using the Semgrep open-source SAST tool. It generates rules in Semgrep YAML format with proper pattern syntax, metavariable bindings, and fix suggestions.
The skill supports all Semgrep pattern operators including pattern-either for matching multiple code variants, pattern-not for exclusions, metavariable-regex for constraining captured variables, and metavariable-comparison for numeric checks. It leverages taint-mode analysis to track data flow from sources to sinks across function boundaries, essential for detecting injection vulnerabilities.
Rule generation covers common vulnerability patterns for Python (Django, Flask), Go (net/http, gin), and JavaScript (Express, React) frameworks. The skill creates rules with proper severity levels, CWE references, OWASP mappings, and actionable fix suggestions using the fix or fix-regex fields. It includes test case generation with semgrep -test compatible annotations marking expected true positives and negatives. Rules are validated against the Semgrep rule schema and tested against sample code snippets before deployment to Semgrep App or CI integration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/)
