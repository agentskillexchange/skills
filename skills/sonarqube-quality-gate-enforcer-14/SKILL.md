---
title: "SonarQube Quality Gate Enforcer"
slug: "sonarqube-quality-gate-enforcer-14"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
author: "SonarSource"
category: "Code Quality & Review"
framework: "MCP"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Quality Gate Enforcer

Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://docs.sonarsource.com/sonarqube-server/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/)
