---
title: "SonarQube Gate Enforcer"
description: "Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced."
slug: "sonarqube-gate-enforcer"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-gate-enforcer/"
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

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
clawhub install sonarqube-gate-enforcer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status endpoint after analysis completion to retrieve gate conditions and their pass/fail status. The skill supports custom quality gate profiles with configurable thresholds for code coverage percentage, duplication density, maintainability rating, reliability rating, and security hotspot review percentage. When a gate fails, it generates detailed failure reports showing exactly which conditions were violated, the delta from the threshold, and specific files contributing to the failure via the /api/issues/search endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality gate status as commit checks and PR comments. It supports branch analysis for feature branches and pull request decoration with inline code annotations from SonarQube findings.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
