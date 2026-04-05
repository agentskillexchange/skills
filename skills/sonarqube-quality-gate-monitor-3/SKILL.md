---
name: "SonarQube Quality Gate Monitor"
description: "Monitors SonarQube project quality gates via the Web API and blocks CI deployments when thresholds fail. Tracks technical debt trends across releases."
category: "Code Quality &amp; Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/"
---
# SonarQube Quality Gate Monitor

Monitors SonarQube project quality gates via the Web API and blocks CI deployments when thresholds fail. Tracks technical debt trends across releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-monitor-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-monitor-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-monitor-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-monitor-3 -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-quality-gate-monitor-3
```

## Details

The SonarQube Quality Gate Monitor skill integrates with the SonarQube Web API to enforce code quality standards in CI/CD pipelines. It polls analysis task status via api/ce/task and evaluates quality gate conditions through api/qualitygates/project_status endpoints.

The monitor checks all quality gate conditions including coverage percentage, duplicated lines density, reliability rating, security hotspots reviewed, and maintainability rating. When any condition fails, it generates detailed failure reports with specific metrics, threshold values, and links to the SonarQube dashboard for drill-down investigation.

Technical debt tracking uses the api/measures/search_history endpoint to build trend charts across releases, identifying modules with growing debt and files with the highest remediation cost. Integration with GitHub status checks and GitLab merge request approvals blocks deployment pipelines when quality gates fail. Webhook support enables real-time notifications to Slack and Teams channels with formatted analysis summaries including new issues by severity and hotspot counts.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-monitor-3/)
