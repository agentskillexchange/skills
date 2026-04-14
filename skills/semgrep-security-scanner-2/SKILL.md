---
title: "Semgrep Security Scanner"
description: "Scan codebases for security vulnerabilities and anti-patterns using Semgrep OSS rules and the Semgrep CLI. Supports custom YAML rule authoring and SARIF output for CI integration."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Security Scanner

The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via –include and –exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via –baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-scanner-2/)
