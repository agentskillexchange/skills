---
title: SonarQube Quality Gate Monitor
description: The SonarQube Quality Gate Monitor skill integrates with the SonarQube
  Web API to enforce code quality standards in CI/CD pipelines. It polls analysis
  task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status
  endpoints. The monitor checks all quality gate conditions including coverage percentage,
  duplicated lines density, reliability rating, security hotspots reviewed, and maintainability
  rating. When any condition fails, it generates detailed failure reports with specific
  metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation.
  Technical debt tracking uses the api/measures/search_history endpoint to build trend
  charts across releases, identifying modules with growing debt and files with the
  highest remediation cost. Integration with GitHub status checks and GitLab merge
  request approvals blocks deployment pipelines when quality gates fail. Webhook support
  enables real-time notifications to Slack and Teams channels with formatted analysis
  summaries including new issues by severity and hotspot counts.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# SonarQube Quality Gate Monitor

The SonarQube Quality Gate Monitor skill integrates with the SonarQube Web API to enforce code quality standards in CI/CD pipelines. It polls analysis task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status endpoints. The monitor checks all quality gate conditions including coverage percentage, duplicated lines density, reliability rating, security hotspots reviewed, and maintainability rating. When any condition fails, it generates detailed failure reports with specific metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation. Technical debt tracking uses the api/measures/search_history endpoint to build trend charts across releases, identifying modules with growing debt and files with the highest remediation cost. Integration with GitHub status checks and GitLab merge request approvals blocks deployment pipelines when quality gates fail. Webhook support enables real-time notifications to Slack and Teams channels with formatted analysis summaries including new issues by severity and hotspot counts.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/)
