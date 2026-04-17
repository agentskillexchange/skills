---
title: "Semgrep Rule Runner"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
---

# Semgrep Rule Runner

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns.

The skill invokes the semgrep CLI with configurable options including –config for rule selection, –json for structured output parsing, –severity for filtering, and –exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass.

Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking.

For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-rule-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-rule-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
