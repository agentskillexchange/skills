---
title: Jenkins Pipeline Failure Analyzer
description: 'The Jenkins Pipeline Failure Analyzer automates the diagnosis of Jenkins
  CI/CD pipeline failures by interfacing with the Jenkins REST API. It authenticates
  via API tokens and queries /job/{name}/lastFailedBuild/api/json to retrieve build
  metadata, then fetches /job/{name}/{build}/consoleText for full console output parsing.
  The agent uses pattern matching to classify failures into categories: compilation
  errors, test failures, dependency resolution issues, timeout errors, and infrastructure
  problems. For Pipeline (Jenkinsfile) jobs, it queries the Blue Ocean REST API at
  /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes to extract stage-level
  execution data, identifying exactly which stage and step failed. It analyzes Jenkinsfile
  syntax for common issues like missing credentials references, incorrect agent specifications,
  and stale lock files. The analyzer correlates failures with recent SCM changes via
  /job/{name}/{build}/api/json changeSet to identify likely culprit commits. It generates
  fix suggestions and can automatically retry transient infrastructure failures.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# Jenkins Pipeline Failure Analyzer

The Jenkins Pipeline Failure Analyzer automates the diagnosis of Jenkins CI/CD pipeline failures by interfacing with the Jenkins REST API. It authenticates via API tokens and queries /job/{name}/lastFailedBuild/api/json to retrieve build metadata, then fetches /job/{name}/{build}/consoleText for full console output parsing. The agent uses pattern matching to classify failures into categories: compilation errors, test failures, dependency resolution issues, timeout errors, and infrastructure problems. For Pipeline (Jenkinsfile) jobs, it queries the Blue Ocean REST API at /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes to extract stage-level execution data, identifying exactly which stage and step failed. It analyzes Jenkinsfile syntax for common issues like missing credentials references, incorrect agent specifications, and stale lock files. The analyzer correlates failures with recent SCM changes via /job/{name}/{build}/api/json changeSet to identify likely culprit commits. It generates fix suggestions and can automatically retry transient infrastructure failures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
