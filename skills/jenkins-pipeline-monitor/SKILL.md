---
name: "Jenkins Pipeline Monitor"
description: "Monitors Jenkins CI pipelines via the Jenkins REST API (/api/json) and Blue Ocean REST endpoints. Tracks build queue times, stage durations, and test result trends using JUnit XML parsing."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-monitor/
