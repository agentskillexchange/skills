---
title: "Semgrep Security Scanner"
description: "Scan codebases for security vulnerabilities and anti-patterns using Semgrep OSS rules and the Semgrep CLI. Supports custom YAML rule authoring and SARIF output for CI integration."
slug: "semgrep-security-scanner-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-security-scanner-2/"
listed: true
---

# Semgrep Security Scanner

Scan codebases for security vulnerabilities and anti-patterns using Semgrep OSS rules and the Semgrep CLI. Supports custom YAML rule authoring and SARIF output for CI integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install semgrep-security-scanner-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via –include and –exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via –baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-scanner-2/)
