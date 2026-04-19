---
title: "Semgrep Rule Runner"
description: "The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns. The skill invokes the semgrep CLI with configurable options including &#8211;config for rule selection, &#8211;json for structured output parsing, &#8211;severity for filtering, and &#8211;exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass. Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking. For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking."
source: "https://github.com/semgrep/semgrep"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Rule Runner

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns. The skill invokes the semgrep CLI with configurable options including &#8211;config for rule selection, &#8211;json for structured output parsing, &#8211;severity for filtering, and &#8211;exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass. Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking. For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
