---
name: "Jenkins Pipeline Health Monitor"
description: "Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_stars: 25122
  github_repo: jenkinsci/jenkins
  license: MIT
  maintained: true
---
# Jenkins Pipeline Health Monitor

Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance.

## Overview

The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts.

The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data.

Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-health-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-health-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-health-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-health-monitor -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-health-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/)
