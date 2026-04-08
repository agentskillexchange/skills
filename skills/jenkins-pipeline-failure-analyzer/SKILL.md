---
title: "Jenkins Pipeline Failure Analyzer"
slug: "jenkins-pipeline-failure-analyzer"
verification: "security_reviewed"
description: "Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification."
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/"
---

# Jenkins Pipeline Failure Analyzer

Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
