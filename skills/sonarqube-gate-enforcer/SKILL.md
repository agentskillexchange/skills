---
title: SonarQube Gate Enforcer
description: The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks
  directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status
  endpoint after analysis completion to retrieve gate conditions and their pass/fail
  status. The skill supports custom quality gate profiles with configurable thresholds
  for code coverage percentage, duplication density, maintainability rating, reliability
  rating, and security hotspot review percentage. When a gate fails, it generates
  detailed failure reports showing exactly which conditions were violated, the delta
  from the threshold, and specific files contributing to the failure via the /api/issues/search
  endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality
  gate status as commit checks and PR comments. It supports branch analysis for feature
  branches and pull request decoration with inline code annotations from SonarQube
  findings.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-gate-enforcer/
category:
- Code Quality &amp; Review
framework:
- Cursor
---

# SonarQube Gate Enforcer

The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status endpoint after analysis completion to retrieve gate conditions and their pass/fail status. The skill supports custom quality gate profiles with configurable thresholds for code coverage percentage, duplication density, maintainability rating, reliability rating, and security hotspot review percentage. When a gate fails, it generates detailed failure reports showing exactly which conditions were violated, the delta from the threshold, and specific files contributing to the failure via the /api/issues/search endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality gate status as commit checks and PR comments. It supports branch analysis for feature branches and pull request decoration with inline code annotations from SonarQube findings.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
