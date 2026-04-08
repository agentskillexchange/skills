---
title: Semgrep Rule Runner
description: The Semgrep Rule Runner provides advanced static analysis capabilities
  using the Semgrep open-source engine. It supports both local rule definitions in
  YAML format and the Semgrep Registry for community-maintained rule packs covering
  OWASP Top 10, CWE categories, and framework-specific patterns. The skill invokes
  the semgrep CLI with configurable options including –config for rule selection,
  –json for structured output parsing, –severity for filtering, and –exclude for path
  ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript,
  Go, Java, Ruby, and Kotlin in a single pass. Results are parsed from the JSON output
  format, extracting match locations, severity levels, fix suggestions, and metadata
  references. The agent can automatically apply Semgrep autofix suggestions where
  available and generate suppression comments (# nosemgrep) with justification tracking.
  For team workflows, the skill integrates with the Semgrep App API to upload findings,
  manage triage states (open/ignored/fixed), track false positive rates, and enforce
  policy-as-code rules that block PRs containing critical findings. It also supports
  custom rule authoring with pattern-either, metavariable-comparison, and taint-mode
  tracking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-rule-runner/
category:
- Code Quality &amp; Review
framework:
- Gemini
---

# Semgrep Rule Runner

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns. The skill invokes the semgrep CLI with configurable options including –config for rule selection, –json for structured output parsing, –severity for filtering, and –exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass. Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking. For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
