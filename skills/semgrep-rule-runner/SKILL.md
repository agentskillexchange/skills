---
title: "Semgrep Rule Runner"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows."
slug: "semgrep-rule-runner"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-rule-runner/"
---

# Semgrep Rule Runner

Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows.

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
clawhub install semgrep-rule-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns.
The skill invokes the semgrep CLI with configurable options including –config for rule selection, –json for structured output parsing, –severity for filtering, and –exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass.
Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking.
For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
