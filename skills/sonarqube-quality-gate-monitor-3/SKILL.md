---
title: "SonarQube Quality Gate Monitor"
description: "Monitors SonarQube project quality gates via the Web API and blocks CI deployments when thresholds fail. Tracks technical debt trends across releases."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "LGPL-3.0"
---

# SonarQube Quality Gate Monitor

The SonarQube Quality Gate Monitor skill integrates with the SonarQube Web API to enforce code quality standards in CI/CD pipelines. It polls analysis task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status endpoints.

The monitor checks all quality gate conditions including coverage percentage, duplicated lines density, reliability rating, security hotspots reviewed, and maintainability rating. When any condition fails, it generates detailed failure reports with specific metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation.

Technical debt tracking uses the api/measures/search_history endpoint to build trend charts across releases, identifying modules with growing debt and files with the highest remediation cost. Integration with GitHub status checks and GitLab merge request approvals blocks deployment pipelines when quality gates fail. Webhook support enables real-time notifications to Slack and Teams channels with formatted analysis summaries including new issues by severity and hotspot counts.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/)
