---
title: Jenkins Declarative Pipeline Generator
description: The Jenkins Declarative Pipeline Generator creates production-ready Jenkinsfiles
  by analyzing project structure and generating appropriate stage definitions with
  proper agent selection. It leverages the Pipeline Model Definition Plugin for structured
  pipeline syntax and integrates with Jenkins shared libraries following the vars/
  and src/ directory conventions. The skill uses the Jenkins REST API (jenkins-cli
  and jenkins-api npm packages) for remote job creation, parameter configuration,
  and credential store management via the Credentials Plugin API. It supports multi-branch
  pipeline configurations with automatic SCM trigger setup through the GitHub Branch
  Source Plugin and Bitbucket Branch Source Plugin. The generator handles complex
  deployment stages with environment-specific configurations, implementing proper
  input gates for production deployments and integrating with the Pipeline Stage View
  Plugin for visual pipeline monitoring. It also configures post-build actions including
  Slack notifications via the Slack Notification Plugin API and artifact archiving
  strategies.
verification: security_reviewed
source: https://github.com/jenkinsci/pipeline-model-definition-plugin
category:
- CI/CD Integrations
framework:
- OpenClaw
tool_ecosystem:
  github_repo: jenkinsci/pipeline-model-definition-plugin
  github_stars: 564
---

# Jenkins Declarative Pipeline Generator

The Jenkins Declarative Pipeline Generator creates production-ready Jenkinsfiles by analyzing project structure and generating appropriate stage definitions with proper agent selection. It leverages the Pipeline Model Definition Plugin for structured pipeline syntax and integrates with Jenkins shared libraries following the vars/ and src/ directory conventions. The skill uses the Jenkins REST API (jenkins-cli and jenkins-api npm packages) for remote job creation, parameter configuration, and credential store management via the Credentials Plugin API. It supports multi-branch pipeline configurations with automatic SCM trigger setup through the GitHub Branch Source Plugin and Bitbucket Branch Source Plugin. The generator handles complex deployment stages with environment-specific configurations, implementing proper input gates for production deployments and integrating with the Pipeline Stage View Plugin for visual pipeline monitoring. It also configures post-build actions including Slack notifications via the Slack Notification Plugin API and artifact archiving strategies.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-declarative-pipeline-generator-2/)
