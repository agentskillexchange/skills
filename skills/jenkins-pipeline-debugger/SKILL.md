---
title: "Jenkins Pipeline Debugger"
description: "Connects to Jenkins via the Jenkins REST API and Blue Ocean API to debug Declarative and Scripted pipelines. Retrieves stage logs, replays failed builds, and traces Groovy CPS execution state."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Debugger

The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/ to map stage execution graphs. Failed stage logs are retrieved via the consoleText API and parsed for common error patterns including dependency resolution failures, Docker image pull errors, and credential binding issues. The skill can replay failed builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts. It inspects the CPS (Continuation Passing Style) execution state through the Pipeline Steps API to identify where Groovy closures stalled. Shared library resolution is traced using the Global Library configuration API. Build queue analysis via /queue/api/json identifies executor starvation and label mismatch bottlenecks.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-debugger/)
