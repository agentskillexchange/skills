---
title: Semgrep Custom Pattern Library
description: The Semgrep Custom Pattern Library creates targeted static analysis rules
  using Semgrep’s pattern matching DSL. It generates YAML rule files with sophisticated
  pattern combinations including pattern-either for variant matching, pattern-not
  for false positive suppression, and metavariable-pattern for deep structural checks.
  The skill supports taint-mode analysis for tracking data flow from sources to sinks
  across function boundaries, enabling detection of injection vulnerabilities, SSRF,
  and path traversal issues. Rules are organized into packs aligned with OWASP Top
  10 categories and CWE identifiers for compliance reporting. Advanced features include
  autofix generation using Semgrep’s fix key for automated remediation, join rules
  for cross-file analysis patterns, and extract mode configurations for analyzing
  embedded languages like SQL in Python strings. The library integrates with Semgrep
  App for rule sharing and includes semgrep ci configuration for pre-commit hooks
  and CI pipeline integration with SARIF output for GitHub Security tab ingestion.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-custom-pattern-library/
category:
- Code Quality &amp; Review
framework:
- Claude Agents
---

# Semgrep Custom Pattern Library

The Semgrep Custom Pattern Library creates targeted static analysis rules using Semgrep’s pattern matching DSL. It generates YAML rule files with sophisticated pattern combinations including pattern-either for variant matching, pattern-not for false positive suppression, and metavariable-pattern for deep structural checks. The skill supports taint-mode analysis for tracking data flow from sources to sinks across function boundaries, enabling detection of injection vulnerabilities, SSRF, and path traversal issues. Rules are organized into packs aligned with OWASP Top 10 categories and CWE identifiers for compliance reporting. Advanced features include autofix generation using Semgrep’s fix key for automated remediation, join rules for cross-file analysis patterns, and extract mode configurations for analyzing embedded languages like SQL in Python strings. The library integrates with Semgrep App for rule sharing and includes semgrep ci configuration for pre-commit hooks and CI pipeline integration with SARIF output for GitHub Security tab ingestion.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-library/)
