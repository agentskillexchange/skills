---
title: "Jenkins Pipeline Debugger"
description: "The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/ to map stage execution graphs. Failed stage logs are retrieved via the consoleText API and parsed for common error patterns including dependency resolution failures, Docker image pull errors, and credential binding issues. The skill can replay failed builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts. It inspects the CPS (Continuation Passing Style) execution state through the Pipeline Steps API to identify where Groovy closures stalled. Shared library resolution is traced using the Global Library configuration API. Build queue analysis via /queue/api/json identifies executor starvation and label mismatch bottlenecks."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Debugger

The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/ to map stage execution graphs. Failed stage logs are retrieved via the consoleText API and parsed for common error patterns including dependency resolution failures, Docker image pull errors, and credential binding issues. The skill can replay failed builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts. It inspects the CPS (Continuation Passing Style) execution state through the Pipeline Steps API to identify where Groovy closures stalled. Shared library resolution is traced using the Global Library configuration API. Build queue analysis via /queue/api/json identifies executor starvation and label mismatch bottlenecks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-debugger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-debugger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-debugger/)
