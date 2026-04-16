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
  license: "MIT"
---

# Jenkins Pipeline Failure Analyzer

The Jenkins Pipeline Failure Analyzer automates the diagnosis of Jenkins CI/CD pipeline failures by interfacing with the Jenkins REST API. It authenticates via API tokens and queries /job/{name}/lastFailedBuild/api/json to retrieve build metadata, then fetches /job/{name}/{build}/consoleText for full console output parsing. The agent uses pattern matching to classify failures into categories: compilation errors, test failures, dependency resolution issues, timeout errors, and infrastructure problems. For Pipeline (Jenkinsfile) jobs, it queries the Blue Ocean REST API at /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes to extract stage-level execution data, identifying exactly which stage and step failed. It analyzes Jenkinsfile syntax for common issues like missing credentials references, incorrect agent specifications, and stale lock files. The analyzer correlates failures with recent SCM changes via /job/{name}/{build}/api/json changeSet to identify likely culprit commits. It generates fix suggestions and can automatically retry transient infrastructure failures.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
