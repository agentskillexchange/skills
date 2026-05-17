---
name: "SonarQube Gate Checker"
slug: "sonarqube-gate-checker-2"
description: "Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles."
github_stars: 10433
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Gate Checker

Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-checker-2/)
