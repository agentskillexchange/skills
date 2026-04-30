---
title: "Jenkins Pipeline Failure Analyzer"
description: "Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Failure Analyzer

Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/)
