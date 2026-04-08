---
title: Semgrep Pattern Scanner
description: The Semgrep Pattern Scanner leverages the Semgrep open-source static
  analysis engine to scan codebases for security vulnerabilities, anti-patterns, and
  code smells. It loads rules from the Semgrep Registry via the –config=auto flag
  and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside
  operators. The agent executes semgrep scan with –sarif output for direct integration
  with GitHub Advanced Security and the Code Scanning API. It supports taint mode
  analysis by defining source-sink-sanitizer rules to track dangerous data flows across
  function boundaries. For monorepo support, it uses –include/–exclude glob patterns
  and respects .semgrepignore files. The scanner handles multiple languages simultaneously
  including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern
  syntax. Results are deduplicated across runs using fingerprinting and can be filtered
  by severity (ERROR, WARNING, INFO) for actionable reporting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-pattern-scanner/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# Semgrep Pattern Scanner

The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the –config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with –sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses –include/–exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-scanner/)
