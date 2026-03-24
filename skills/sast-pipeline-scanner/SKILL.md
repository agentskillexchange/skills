---
name: "SAST Pipeline Scanner"
description: "Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management."
category: "Security & Verification"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sast-pipeline-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/sast-pipeline-scanner/
