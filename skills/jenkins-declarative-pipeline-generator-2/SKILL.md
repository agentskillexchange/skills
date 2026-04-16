---
title: "Jenkins Declarative Pipeline Generator"
description: "Generates Jenkins Declarative Pipelines using the Pipeline Model Definition Plugin API and Jenkins shared library conventions. Integrates with the Jenkins REST API for job provisioning and credentials management."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/pipeline-model-definition-plugin"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "jenkinsci/pipeline-model-definition-plugin"
  github_stars: 564
---

# Jenkins Declarative Pipeline Generator

The Jenkins Declarative Pipeline Generator creates production-ready Jenkinsfiles by analyzing project structure and generating appropriate stage definitions with proper agent selection. It leverages the Pipeline Model Definition Plugin for structured pipeline syntax and integrates with Jenkins shared libraries following the vars/ and src/ directory conventions. The skill uses the Jenkins REST API (jenkins-cli and jenkins-api npm packages) for remote job creation, parameter configuration, and credential store management via the Credentials Plugin API. It supports multi-branch pipeline configurations with automatic SCM trigger setup through the GitHub Branch Source Plugin and Bitbucket Branch Source Plugin. The generator handles complex deployment stages with environment-specific configurations, implementing proper input gates for production deployments and integrating with the Pipeline Stage View Plugin for visual pipeline monitoring. It also configures post-build actions including Slack notifications via the Slack Notification Plugin API and artifact archiving strategies.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-declarative-pipeline-generator-2/)
