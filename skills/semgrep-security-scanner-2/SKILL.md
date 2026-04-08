---
title: Semgrep Security Scanner
description: 'The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep
  Registry to perform fast, pattern-based static analysis across 30+ programming languages.
  It uses the semgrep scan command with configurable rulesets from the Semgrep Registry
  (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions
  in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and
  metavariable-comparison operators. The skill handles monorepo scanning with path
  filtering via –include and –exclude flags, generates SARIF reports for GitHub Code
  Scanning integration, and produces JSON output for programmatic processing. It supports
  Semgrep App integration for diff-aware scanning in CI pipelines via –baseline-commit,
  manages findings with triage states (open, ignored, fixed), and can autofix certain
  patterns using the fix: key in custom rules. The scanner also supports secrets detection
  via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-security-scanner-2/
category:
- Code Quality &amp; Review
framework:
- Claude Agents
---

# Semgrep Security Scanner

The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via –include and –exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via –baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-scanner-2/)
