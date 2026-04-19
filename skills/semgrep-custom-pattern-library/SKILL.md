---
title: "Semgrep Custom Pattern Library"
description: "The Semgrep Custom Pattern Library creates targeted static analysis rules using Semgrep&#8217;s pattern matching DSL. It generates YAML rule files with sophisticated pattern combinations including pattern-either for variant matching, pattern-not for false positive suppression, and metavariable-pattern for deep structural checks. The skill supports taint-mode analysis for tracking data flow from sources to sinks across function boundaries, enabling detection of injection vulnerabilities, SSRF, and path traversal issues. Rules are organized into packs aligned with OWASP Top 10 categories and CWE identifiers for compliance reporting. Advanced features include autofix generation using Semgrep&#8217;s fix key for automated remediation, join rules for cross-file analysis patterns, and extract mode configurations for analyzing embedded languages like SQL in Python strings. The library integrates with Semgrep App for rule sharing and includes semgrep ci configuration for pre-commit hooks and CI pipeline integration with SARIF output for GitHub Security tab ingestion."
source: "https://github.com/semgrep/semgrep"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Custom Pattern Library

The Semgrep Custom Pattern Library creates targeted static analysis rules using Semgrep&#8217;s pattern matching DSL. It generates YAML rule files with sophisticated pattern combinations including pattern-either for variant matching, pattern-not for false positive suppression, and metavariable-pattern for deep structural checks. The skill supports taint-mode analysis for tracking data flow from sources to sinks across function boundaries, enabling detection of injection vulnerabilities, SSRF, and path traversal issues. Rules are organized into packs aligned with OWASP Top 10 categories and CWE identifiers for compliance reporting. Advanced features include autofix generation using Semgrep&#8217;s fix key for automated remediation, join rules for cross-file analysis patterns, and extract mode configurations for analyzing embedded languages like SQL in Python strings. The library integrates with Semgrep App for rule sharing and includes semgrep ci configuration for pre-commit hooks and CI pipeline integration with SARIF output for GitHub Security tab ingestion.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-library/)
