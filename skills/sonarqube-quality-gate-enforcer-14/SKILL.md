---
title: "SonarQube Quality Gate Enforcer"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
slug: "sonarqube-quality-gate-enforcer-14"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/"
---

# SonarQube Quality Gate Enforcer

Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed.

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
clawhub install sonarqube-quality-gate-enforcer-14
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Quality Gate Enforcer skill integrates SonarQube quality gate enforcement into pull request workflows. It queries the SonarQube Web API measures/component endpoint to fetch real-time quality metrics including code coverage, duplicated lines percentage, cognitive complexity, and security hotspot counts. The skill monitors the ce/task endpoint for analysis completion and evaluates results against configurable quality gate profiles. When violations are detected, it posts detailed PR comments breaking down each failed condition with specific file-level metrics and remediation guidance. Supports multi-language projects with per-language threshold overrides. Can enforce differential quality gates that apply stricter standards to new code versus legacy code. Integrates with GitHub Check Runs API to create blocking status checks. Generates trend reports showing quality metric trajectories across releases. Works with SonarQube Community, Developer, and Enterprise editions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/)
