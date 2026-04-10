---
name: Jenkins Pipeline Orchestrator
description: Automates Jenkins CI/CD pipeline configuration using the Jenkins REST
  API and Jenkinsfile DSL. Manages multi-branch pipelines, triggers builds via webhooks,
  and parses build artifacts for deployment readiness.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-orchestrator-3/
category:
- CI/CD Integrations
framework:
- OpenClaw
---
# Jenkins Pipeline Orchestrator

The Jenkins Pipeline Orchestrator skill provides comprehensive automation for Jenkins CI/CD environments. It leverages the Jenkins REST API to programmatically create, configure, and manage pipeline jobs without manual intervention through the Jenkins UI.
Key capabilities include generating Jenkinsfile definitions using the Declarative Pipeline DSL, configuring multi-branch pipeline jobs that automatically discover branches and pull requests, and setting up webhook triggers for GitHub, GitLab, and Bitbucket repositories. The skill handles credential management through the Jenkins Credentials API, ensuring secrets are securely stored and referenced in pipeline stages.
Build artifact analysis is built in — the skill parses JUnit XML test reports, collects code coverage metrics from JaCoCo or Cobertura plugins, and evaluates deployment gates based on configurable quality thresholds. It also integrates with the Jenkins Blue Ocean API for modern pipeline visualization and status reporting to external notification channels via Slack or Microsoft Teams webhooks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-orchestrator-3/)
