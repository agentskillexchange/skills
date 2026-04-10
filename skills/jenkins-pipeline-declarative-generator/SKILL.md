---
title: "Jenkins Pipeline Declarative Generator"
description: "Creates Jenkins Declarative Pipeline Jenkinsfiles using jenkins-pipeline-syntax and jenkins-shared-libraries. Configures stages, parallel execution, and post-build actions with Blue Ocean compatibility."
slug: "jenkins-pipeline-declarative-generator"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/"
listed: true
---

# Jenkins Pipeline Declarative Generator

Creates Jenkins Declarative Pipeline Jenkinsfiles using jenkins-pipeline-syntax and jenkins-shared-libraries. Configures stages, parallel execution, and post-build actions with Blue Ocean compatibility.

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
clawhub install jenkins-pipeline-declarative-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Pipeline Declarative Generator skill creates Jenkinsfile configurations using the Declarative Pipeline syntax (pipeline { agent, stages, post }) compatible with Jenkins 2.x and Blue Ocean. It leverages Jenkins shared libraries (@Library annotations) and pipeline-model-definition-plugin for structured pipeline authoring.
The skill generates stage definitions with steps including sh, bat, powershell, checkout scm, withCredentials, and archiveArtifacts. It configures agent blocks with Docker containers (agent { docker { image } }), Kubernetes pods (agent { kubernetes { yaml } }), and label-based node selection. Parallel stage execution uses the parallel keyword within stage blocks for concurrent testing.
Advanced features include shared library development with vars/*.groovy global functions and src/**/*.groovy class definitions, stash/unstash for cross-stage artifact passing, input step configuration for manual approval gates, lock resource management for deployment serialization, and when clause conditions (branch, environment, expression, changeset) for conditional stage execution. The generator also supports Multibranch Pipeline configuration, GitHub Organization scanning, and pipeline replay/restart capabilities through the Jenkins CLI and REST API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-declarative-generator/)
