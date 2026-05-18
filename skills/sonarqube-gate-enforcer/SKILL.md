---
name: "SonarQube Gate Enforcer"
slug: "sonarqube-gate-enforcer"
description: "Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced."
github_stars: 10433
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category: "Code Quality & Review"
framework: "Cursor"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
