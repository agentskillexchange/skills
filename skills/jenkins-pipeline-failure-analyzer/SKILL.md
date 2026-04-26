---
title: "Jenkins Pipeline Failure Analyzer"
description: "Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Failure Analyzer

Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-failure-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-pipeline-failure-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
