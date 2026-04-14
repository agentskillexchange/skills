---
title: "Semgrep Rule Runner"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Rule Runner

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns.

The skill invokes the semgrep CLI with configurable options including –config for rule selection, –json for structured output parsing, –severity for filtering, and –exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass.

Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking.

For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
