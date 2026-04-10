---
title: "Jenkins Pipeline Shared Library Linter"
description: "Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes."
slug: "jenkins-pipeline-shared-library-linter"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/"
listed: true
---

# Jenkins Pipeline Shared Library Linter

Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes.

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
clawhub install jenkins-pipeline-shared-library-linter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates linting of Jenkins pipeline files by interacting with the Jenkins REST API and the Jenkins CLI jar. It posts Jenkinsfile content to the /pipeline-model-converter/validate endpoint on a configured Jenkins controller, parses the JSON response for syntax errors, and reports them with exact line numbers and suggested corrections. The skill supports both Declarative and Scripted pipeline syntax, handles authentication via Jenkins API tokens, and works with multibranch pipelines. It integrates with GitHub webhooks and GitLab CI triggers to run on every pull request. Configuration covers Jenkins controller URL, credentials, and branch-specific overrides. Output is formatted for terminal, GitHub Checks annotations, and Slack notifications via the Slack Notification Plugin. Useful for preventing broken pipeline code from merging into protected branches.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/)
