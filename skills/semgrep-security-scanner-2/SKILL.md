---
title: "Semgrep Security Scanner"
description: "The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via &#8211;include and &#8211;exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via &#8211;baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities."
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

# Semgrep Security Scanner

The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via &#8211;include and &#8211;exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via &#8211;baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-scanner-2/)
