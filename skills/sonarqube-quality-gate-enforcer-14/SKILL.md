---
name: "SonarQube Quality Gate Enforcer"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
category: "Code Quality & Review"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sonarqube"  # from ase_tool_match
  github_stars: 10357  # from ase_github_stars (integer, not string)
  github_repo: "SonarSource/sonarqube"  # from ase_github_repo
  license: "LGPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SonarQube Quality Gate Enforcer

Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed.

## Overview

The SonarQube Quality Gate Enforcer skill integrates SonarQube quality gate enforcement into pull request workflows. It queries the SonarQube Web API measures/component endpoint to fetch real-time quality metrics including code coverage, duplicated lines percentage, cognitive complexity, and security hotspot counts. The skill monitors the ce/task endpoint for analysis completion and evaluates results against configurable quality gate profiles. When violations are detected, it posts detailed PR comments breaking down each failed condition with specific file-level metrics and remediation guidance. Supports multi-language projects with per-language threshold overrides. Can enforce differential quality gates that apply stricter standards to new code versus legacy code. Integrates with GitHub Check Runs API to create blocking status checks. Generates trend reports showing quality metric trajectories across releases. Works with SonarQube Community, Developer, and Enterprise editions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-enforcer-14
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-enforcer-14 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-enforcer-14 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-enforcer-14 -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-quality-gate-enforcer-14
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/
