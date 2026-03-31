---
name: "Jenkins Pipeline Orchestrator"
description: "Automates Jenkins CI/CD pipeline configuration using the Jenkins REST API and Jenkinsfile DSL. Manages multi-branch pipelines, triggers builds via webhooks, and parses build artifacts for deployment readiness."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_repo: jenkinsci/jenkins
  github_stars: 25143
  license: MIT
  maintained: true
---
# Jenkins Pipeline Orchestrator

Automates Jenkins CI/CD pipeline configuration using the Jenkins REST API and Jenkinsfile DSL. Manages multi-branch pipelines, triggers builds via webhooks, and parses build artifacts for deployment readiness.

## Overview

The Jenkins Pipeline Orchestrator skill provides comprehensive automation for Jenkins CI/CD environments. It leverages the Jenkins REST API to programmatically create, configure, and manage pipeline jobs without manual intervention through the Jenkins UI.

Key capabilities include generating Jenkinsfile definitions using the Declarative Pipeline DSL, configuring multi-branch pipeline jobs that automatically discover branches and pull requests, and setting up webhook triggers for GitHub, GitLab, and Bitbucket repositories. The skill handles credential management through the Jenkins Credentials API, ensuring secrets are securely stored and referenced in pipeline stages.

Build artifact analysis is built in — the skill parses JUnit XML test reports, collects code coverage metrics from JaCoCo or Cobertura plugins, and evaluates deployment gates based on configurable quality thresholds. It also integrates with the Jenkins Blue Ocean API for modern pipeline visualization and status reporting to external notification channels via Slack or Microsoft Teams webhooks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-orchestrator-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-orchestrator-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-orchestrator-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-orchestrator-3 -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-orchestrator-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-orchestrator-3/)
