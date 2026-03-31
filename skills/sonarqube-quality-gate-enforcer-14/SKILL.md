---
name: "SonarQube Quality Gate Enforcer"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
category: "Code Quality &amp; Review"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/sonarsource/sonarqube"
tool_ecosystem:
  tool: sonarqube
  github_repo: sonarsource/sonarqube
  github_stars: 10379
  license: LGPL-3.0
  maintained: true
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/)
