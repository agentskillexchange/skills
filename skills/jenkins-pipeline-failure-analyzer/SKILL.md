---
title: "Jenkins Pipeline Failure Analyzer"
description: "The Jenkins Pipeline Failure Analyzer automates the diagnosis of Jenkins CI/CD pipeline failures by interfacing with the Jenkins REST API. It authenticates via API tokens and queries /job/{name}/lastFailedBuild/api/json to retrieve build metadata, then fetches /job/{name}/{build}/consoleText for full console output parsing. The agent uses pattern matching to classify failures into categories: compilation errors, test failures, dependency resolution issues, timeout errors, and infrastructure problems. For Pipeline (Jenkinsfile) jobs, it queries the Blue Ocean REST API at /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes to extract stage-level execution data, identifying exactly which stage and step failed. It analyzes Jenkinsfile syntax for common issues like missing credentials references, incorrect agent specifications, and stale lock files. The analyzer correlates failures with recent SCM changes via /job/{name}/{build}/api/json changeSet to identify likely culprit commits. It generates fix suggestions and can automatically retry transient infrastructure failures."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Failure Analyzer

The Jenkins Pipeline Failure Analyzer automates the diagnosis of Jenkins CI/CD pipeline failures by interfacing with the Jenkins REST API. It authenticates via API tokens and queries /job/{name}/lastFailedBuild/api/json to retrieve build metadata, then fetches /job/{name}/{build}/consoleText for full console output parsing. The agent uses pattern matching to classify failures into categories: compilation errors, test failures, dependency resolution issues, timeout errors, and infrastructure problems. For Pipeline (Jenkinsfile) jobs, it queries the Blue Ocean REST API at /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes to extract stage-level execution data, identifying exactly which stage and step failed. It analyzes Jenkinsfile syntax for common issues like missing credentials references, incorrect agent specifications, and stale lock files. The analyzer correlates failures with recent SCM changes via /job/{name}/{build}/api/json changeSet to identify likely culprit commits. It generates fix suggestions and can automatically retry transient infrastructure failures.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
