---
name: "SAST Pipeline Scanner"
description: "Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sast-pipeline-scanner/"
tool_ecosystem:
  tool: semgrep
  github_stars: 14551
  github_repo: semgrep/semgrep
  license: LGPL-2.1
  maintained: true
---
# SAST Pipeline Scanner

Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management.

## Overview

The SAST Pipeline Scanner skill integrates static application security testing directly into your CI/CD pipeline through agent automation. It orchestrates Semgrep’s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities, and leverages CodeQL’s semantic code analysis for deeper taint-tracking across function boundaries.

When triggered on pull request events, the skill analyzes only the changed diff to minimize scan time, while maintaining a baseline of full-repository findings. Results are formatted in SARIF (Static Analysis Results Interchange Format) for compatibility with GitHub Advanced Security’s code scanning alerts dashboard.

Configuration supports custom Semgrep rule registries, CodeQL query suites for specific languages (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions, and inline PR comment annotations with remediation guidance. The skill also tracks false positive suppressions across scans to reduce developer alert fatigue over time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sast-pipeline-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sast-pipeline-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sast-pipeline-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sast-pipeline-scanner -a codex
```

### OpenClaw

```bash
clawhub install sast-pipeline-scanner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
