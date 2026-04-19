---
title: "SonarQube Gate Enforcer"
description: "The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status endpoint after analysis completion to retrieve gate conditions and their pass/fail status. The skill supports custom quality gate profiles with configurable thresholds for code coverage percentage, duplication density, maintainability rating, reliability rating, and security hotspot review percentage. When a gate fails, it generates detailed failure reports showing exactly which conditions were violated, the delta from the threshold, and specific files contributing to the failure via the /api/issues/search endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality gate status as commit checks and PR comments. It supports branch analysis for feature branches and pull request decoration with inline code annotations from SonarQube findings."
source: "https://github.com/SonarSource/sonarqube"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Gate Enforcer

The SonarQube Gate Enforcer skill integrates SonarQube quality gate checks directly into CI/CD pipelines via the SonarQube Web API. It polls the /api/qualitygates/project_status endpoint after analysis completion to retrieve gate conditions and their pass/fail status. The skill supports custom quality gate profiles with configurable thresholds for code coverage percentage, duplication density, maintainability rating, reliability rating, and security hotspot review percentage. When a gate fails, it generates detailed failure reports showing exactly which conditions were violated, the delta from the threshold, and specific files contributing to the failure via the /api/issues/search endpoint. The tool integrates with GitHub, GitLab, and Bitbucket APIs to post quality gate status as commit checks and PR comments. It supports branch analysis for feature branches and pull request decoration with inline code annotations from SonarQube findings.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
