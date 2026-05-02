---
title: "Jenkins Pipeline Linter"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter HTTP API (/pipeline-model-converter/validate) and npm-groovy-lint for Groovy static analysis with CodeNarc rulesets."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Linter

The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions before they reach the CI server, catching syntax errors, anti-patterns, and security issues early in the development process. It uses two complementary validation approaches for comprehensive coverage.

For declarative pipelines, the skill submits Jenkinsfile content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate, which performs server-side validation against the declarative pipeline schema. This catches structural issues like invalid stage definitions, missing required sections, and unsupported step configurations.

For deeper analysis, the skill runs npm-groovy-lint with CodeNarc rulesets to perform static analysis on both declarative and scripted pipeline Groovy code. It detects common issues including hardcoded credentials, missing timeout blocks, unbounded retry loops, and insecure script approvals. The linter checks for pipeline best practices such as proper use of parallel stages, stash/unstash patterns, shared library imports, and agent allocation strategies. It generates reports with specific line references and suggested fixes, supporting both local validation and integration as a PR check via the Jenkins GitHub plugin webhook.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-linter-6
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-pipeline-linter-6`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/)
