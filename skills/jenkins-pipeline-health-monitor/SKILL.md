---
title: "Jenkins Pipeline Health Monitor"
description: "Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance."
slug: "jenkins-pipeline-health-monitor"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/"
---

# Jenkins Pipeline Health Monitor

Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install jenkins-pipeline-health-monitor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts.
The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data.
Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/)
