---
title: "Semgrep Custom Rule Builder"
description: "Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Custom Rule Builder

The Semgrep Custom Rule Builder skill helps security teams create precise static analysis rules using the Semgrep open-source SAST tool. It generates rules in Semgrep YAML format with proper pattern syntax, metavariable bindings, and fix suggestions.

The skill supports all Semgrep pattern operators including pattern-either for matching multiple code variants, pattern-not for exclusions, metavariable-regex for constraining captured variables, and metavariable-comparison for numeric checks. It leverages taint-mode analysis to track data flow from sources to sinks across function boundaries, essential for detecting injection vulnerabilities.

Rule generation covers common vulnerability patterns for Python (Django, Flask), Go (net/http, gin), and JavaScript (Express, React) frameworks. The skill creates rules with proper severity levels, CWE references, OWASP mappings, and actionable fix suggestions using the fix or fix-regex fields. It includes test case generation with semgrep –test compatible annotations marking expected true positives and negatives. Rules are validated against the Semgrep rule schema and tested against sample code snippets before deployment to Semgrep App or CI integration.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/)
