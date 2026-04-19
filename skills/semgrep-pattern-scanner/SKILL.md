---
title: "Semgrep Pattern Scanner"
description: "The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the &#8211;config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with &#8211;sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses &#8211;include/&#8211;exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting."
source: "https://github.com/semgrep/semgrep"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Pattern Scanner

The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the &#8211;config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with &#8211;sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses &#8211;include/&#8211;exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-scanner/)
