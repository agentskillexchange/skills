---
title: "SonarQube Quality Gate Monitor"
description: "The SonarQube Quality Gate Monitor skill integrates with the SonarQube Web API to enforce code quality standards in CI/CD pipelines. It polls analysis task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status endpoints. The monitor checks all quality gate conditions including coverage percentage, duplicated lines density, reliability rating, security hotspots reviewed, and maintainability rating. When any condition fails, it generates detailed failure reports with specific metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation. Technical debt tracking uses the api/measures/search_history endpoint to build trend charts across releases, identifying modules with growing debt and files with the highest remediation cost. Integration with GitHub status checks and GitLab merge request approvals blocks deployment pipelines when quality gates fail. Webhook support enables real-time notifications to Slack and Teams channels with formatted analysis summaries including new issues by severity and hotspot counts."
source: "https://github.com/SonarSource/sonarqube"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
---

# SonarQube Quality Gate Monitor

The SonarQube Quality Gate Monitor skill integrates with the SonarQube Web API to enforce code quality standards in CI/CD pipelines. It polls analysis task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status endpoints. The monitor checks all quality gate conditions including coverage percentage, duplicated lines density, reliability rating, security hotspots reviewed, and maintainability rating. When any condition fails, it generates detailed failure reports with specific metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation. Technical debt tracking uses the api/measures/search_history endpoint to build trend charts across releases, identifying modules with growing debt and files with the highest remediation cost. Integration with GitHub status checks and GitLab merge request approvals blocks deployment pipelines when quality gates fail. Webhook support enables real-time notifications to Slack and Teams channels with formatted analysis summaries including new issues by severity and hotspot counts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/)
