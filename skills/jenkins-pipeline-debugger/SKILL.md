---
title: Jenkins Pipeline Debugger
description: The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins
  CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches
  pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/
  to map stage execution graphs. Failed stage logs are retrieved via the consoleText
  API and parsed for common error patterns including dependency resolution failures,
  Docker image pull errors, and credential binding issues. The skill can replay failed
  builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts.
  It inspects the CPS (Continuation Passing Style) execution state through the Pipeline
  Steps API to identify where Groovy closures stalled. Shared library resolution is
  traced using the Global Library configuration API. Build queue analysis via /queue/api/json
  identifies executor starvation and label mismatch bottlenecks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-debugger/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# Jenkins Pipeline Debugger

The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/ to map stage execution graphs. Failed stage logs are retrieved via the consoleText API and parsed for common error patterns including dependency resolution failures, Docker image pull errors, and credential binding issues. The skill can replay failed builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts. It inspects the CPS (Continuation Passing Style) execution state through the Pipeline Steps API to identify where Groovy closures stalled. Shared library resolution is traced using the Global Library configuration API. Build queue analysis via /queue/api/json identifies executor starvation and label mismatch bottlenecks.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-debugger/)
