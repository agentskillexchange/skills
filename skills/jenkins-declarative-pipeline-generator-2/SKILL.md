---
title: "Jenkins Declarative Pipeline Generator"
description: "Generates Jenkins Declarative Pipelines using the Pipeline Model Definition Plugin API and Jenkins shared library conventions. Integrates with the Jenkins REST API for job provisioning and credentials management."
slug: "jenkins-declarative-pipeline-generator-2"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/jenkinsci/pipeline-model-definition-plugin"
tool_ecosystem:
  github_repo: "jenkinsci/pipeline-model-definition-plugin"
  github_stars: 564
listed: true
---

# Jenkins Declarative Pipeline Generator

Generates Jenkins Declarative Pipelines using the Pipeline Model Definition Plugin API and Jenkins shared library conventions. Integrates with the Jenkins REST API for job provisioning and credentials management.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install jenkins-declarative-pipeline-generator-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Declarative Pipeline Generator creates production-ready Jenkinsfiles by analyzing project structure and generating appropriate stage definitions with proper agent selection. It leverages the Pipeline Model Definition Plugin for structured pipeline syntax and integrates with Jenkins shared libraries following the vars/ and src/ directory conventions. The skill uses the Jenkins REST API (jenkins-cli and jenkins-api npm packages) for remote job creation, parameter configuration, and credential store management via the Credentials Plugin API. It supports multi-branch pipeline configurations with automatic SCM trigger setup through the GitHub Branch Source Plugin and Bitbucket Branch Source Plugin. The generator handles complex deployment stages with environment-specific configurations, implementing proper input gates for production deployments and integrating with the Pipeline Stage View Plugin for visual pipeline monitoring. It also configures post-build actions including Slack notifications via the Slack Notification Plugin API and artifact archiving strategies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-declarative-pipeline-generator-2/)
