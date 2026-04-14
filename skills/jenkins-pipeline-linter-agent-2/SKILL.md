---
title: "Jenkins Pipeline Linter Agent"
description: "Validates Jenkinsfile syntax using the Jenkins Pipeline Linter REST API before commits. Integrates with jenkins-client npm SDK to authenticate and submit declarative or scripted pipelines for server-side validation."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Linter Agent

The Jenkins Pipeline Linter Agent leverages the Jenkins Pipeline Linter REST API endpoint (/pipeline-model-converter/validate) to validate Jenkinsfile syntax before code is committed. Built on the jenkins-client npm SDK, this skill authenticates against your Jenkins instance using API tokens or SSO credentials, then submits pipeline definitions for server-side syntax checking. It supports both declarative and scripted pipeline formats, parsing validation responses to surface specific line-number errors and warnings. The agent can be integrated into pre-commit hooks or CI gate steps to prevent broken pipelines from reaching the build queue. It caches authentication tokens for session reuse and supports Jenkins instances behind reverse proxies. Configuration accepts multiple Jenkins controller URLs for organizations running distributed Jenkins setups across environments.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-agent-2/)
