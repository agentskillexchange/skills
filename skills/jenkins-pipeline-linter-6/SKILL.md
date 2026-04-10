---
title: "Jenkins Pipeline Linter"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter HTTP API (/pipeline-model-converter/validate) and npm-groovy-lint for Groovy static analysis with CodeNarc rulesets."
slug: "jenkins-pipeline-linter-6"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/"
---

# Jenkins Pipeline Linter

Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter HTTP API (/pipeline-model-converter/validate) and npm-groovy-lint for Groovy static analysis with CodeNarc rulesets.

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
clawhub install jenkins-pipeline-linter-6
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions before they reach the CI server, catching syntax errors, anti-patterns, and security issues early in the development process. It uses two complementary validation approaches for comprehensive coverage.
For declarative pipelines, the skill submits Jenkinsfile content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate, which performs server-side validation against the declarative pipeline schema. This catches structural issues like invalid stage definitions, missing required sections, and unsupported step configurations.
For deeper analysis, the skill runs npm-groovy-lint with CodeNarc rulesets to perform static analysis on both declarative and scripted pipeline Groovy code. It detects common issues including hardcoded credentials, missing timeout blocks, unbounded retry loops, and insecure script approvals. The linter checks for pipeline best practices such as proper use of parallel stages, stash/unstash patterns, shared library imports, and agent allocation strategies. It generates reports with specific line references and suggested fixes, supporting both local validation and integration as a PR check via the Jenkins GitHub plugin webhook.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/)
