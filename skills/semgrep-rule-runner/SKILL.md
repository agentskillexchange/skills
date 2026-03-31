---
name: "Semgrep Rule Runner"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows."
category: "Code Quality & Review"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-rule-runner/"
---
# Semgrep Rule Runner

Executes Semgrep static analysis using the semgrep CLI with custom YAML rule packs. Supports –config auto for community rules, parses JSON output via –json flag, and integrates with Semgrep App API for centralized findings management and triage workflows.

## Overview

The Semgrep Rule Runner provides advanced static analysis capabilities using the Semgrep open-source engine. It supports both local rule definitions in YAML format and the Semgrep Registry for community-maintained rule packs covering OWASP Top 10, CWE categories, and framework-specific patterns.

The skill invokes the semgrep CLI with configurable options including –config for rule selection, –json for structured output parsing, –severity for filtering, and –exclude for path ignoring. It supports multi-language scanning across Python, JavaScript, TypeScript, Go, Java, Ruby, and Kotlin in a single pass.

Results are parsed from the JSON output format, extracting match locations, severity levels, fix suggestions, and metadata references. The agent can automatically apply Semgrep autofix suggestions where available and generate suppression comments (# nosemgrep) with justification tracking.

For team workflows, the skill integrates with the Semgrep App API to upload findings, manage triage states (open/ignored/fixed), track false positive rates, and enforce policy-as-code rules that block PRs containing critical findings. It also supports custom rule authoring with pattern-either, metavariable-comparison, and taint-mode tracking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-runner -a codex
```

### OpenClaw

```bash
clawhub install semgrep-rule-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-runner/)
