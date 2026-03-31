---
name: "Jenkins Pipeline Monitor"
description: "Monitors Jenkins CI pipelines via the Jenkins REST API (/api/json) and Blue Ocean REST endpoints. Tracks build queue times, stage durations, and test result trends using JUnit XML parsing."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-pipeline-monitor/"
---
# Jenkins Pipeline Monitor

Monitors Jenkins CI pipelines via the Jenkins REST API (/api/json) and Blue Ocean REST endpoints. Tracks build queue times, stage durations, and test result trends using JUnit XML parsing.

## Overview

The Jenkins Pipeline Monitor agent connects to Jenkins instances via the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to provide real-time visibility into CI/CD pipeline health. It authenticates using API tokens and supports both freestyle and declarative pipeline jobs.

The agent tracks key metrics including build queue wait times, individual stage durations, overall pipeline execution time, and flaky test detection. It parses JUnit XML test reports to identify consistently failing tests, newly broken tests, and tests with high variance in execution time.

For pipeline optimization, the agent analyzes stage-level timing data to identify bottlenecks and suggests parallelization opportunities. It monitors agent/node resource utilization and flags capacity issues that cause queue buildup. Supports Multibranch Pipeline scanning for branch-specific health dashboards and integrates with the Jenkins Credentials API for secure secret rotation reminders.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-monitor -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-monitor/)
