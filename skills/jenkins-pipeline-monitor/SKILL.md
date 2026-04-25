---
title: "Jenkins Pipeline Monitor"
description: "Monitors Jenkins CI pipelines via the Jenkins REST API (/api/json) and Blue Ocean REST endpoints. Tracks build queue times, stage durations, and test result trends using JUnit XML parsing."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Monitor

The Jenkins Pipeline Monitor agent connects to Jenkins instances via the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to provide real-time visibility into CI/CD pipeline health. It authenticates using API tokens and supports both freestyle and declarative pipeline jobs. The agent tracks key metrics including build queue wait times, individual stage durations, overall pipeline execution time, and flaky test detection. It parses JUnit XML test reports to identify consistently failing tests, newly broken tests, and tests with high variance in execution time. For pipeline optimization, the agent analyzes stage-level timing data to identify bottlenecks and suggests parallelization opportunities. It monitors agent/node resource utilization and flags capacity issues that cause queue buildup. Supports Multibranch Pipeline scanning for branch-specific health dashboards and integrates with the Jenkins Credentials API for secure secret rotation reminders.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-pipeline-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-pipeline-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-monitor/)
