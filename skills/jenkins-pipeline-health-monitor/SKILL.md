---
title: "Jenkins Pipeline Health Monitor"
description: "Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Health Monitor

The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts.

The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data.

Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-health-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-health-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/)
