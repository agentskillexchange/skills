---
title: "SAST Pipeline Scanner"
description: "Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sast-pipeline-scanner/"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
---

# SAST Pipeline Scanner

The SAST Pipeline Scanner skill integrates static application security testing directly into your CI/CD pipeline through agent automation. It orchestrates Semgrep’s pattern-matching engine with custom rule sets targeting OWASP Top 10 vulnerabilities, and leverages CodeQL’s semantic code analysis for deeper taint-tracking across function boundaries.

When triggered on pull request events, the skill analyzes only the changed diff to minimize scan time, while maintaining a baseline of full-repository findings. Results are formatted in SARIF (Static Analysis Results Interchange Format) for compatibility with GitHub Advanced Security’s code scanning alerts dashboard.

Configuration supports custom Semgrep rule registries, CodeQL query suites for specific languages (Python, JavaScript, Go, Java, C#), severity threshold gating for CI pass/fail decisions, and inline PR comment annotations with remediation guidance. The skill also tracks false positive suppressions across scans to reduce developer alert fatigue over time.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sast-pipeline-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sast-pipeline-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sast-pipeline-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
