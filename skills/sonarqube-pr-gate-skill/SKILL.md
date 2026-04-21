---
title: "SonarQube PR Gate"
slug: "sonarqube-pr-gate-skill"
description: "Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
framework:
  - "Codex"
---

# SonarQube PR Gate

Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/)
