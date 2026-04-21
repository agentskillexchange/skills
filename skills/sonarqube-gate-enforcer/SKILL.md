---
title: "SonarQube Gate Enforcer"
slug: "sonarqube-gate-enforcer"
description: "Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
