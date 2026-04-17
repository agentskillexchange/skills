---
name: Jenkins Pipeline Failure Analyzer
description: Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and
  /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations
  for stage-level timing and error classification.
category: CI/CD Integrations
framework: Claude Agents
verification: security_reviewed
source: https://github.com/jenkinsci/jenkins
tool_ecosystem:
  github_repo: jenkinsci/jenkins
  github_stars: 25189
  tool: jenkins
  license: MIT
  maintained: true
---
# Jenkins Pipeline Failure Analyzer
Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-failure-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-failure-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
