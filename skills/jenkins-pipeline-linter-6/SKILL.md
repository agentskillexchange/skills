---
name: "Jenkins Pipeline Linter"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter HTTP API (/pipeline-model-converter/validate) and npm-groovy-lint for Groovy static analysis with CodeNarc rulesets."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_stars: 25122
  github_repo: jenkinsci/jenkins
  license: MIT
  maintained: true
---
# Jenkins Pipeline Linter

Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter HTTP API (/pipeline-model-converter/validate) and npm-groovy-lint for Groovy static analysis with CodeNarc rulesets.

## Overview

The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions before they reach the CI server, catching syntax errors, anti-patterns, and security issues early in the development process. It uses two complementary validation approaches for comprehensive coverage.

For declarative pipelines, the skill submits Jenkinsfile content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate, which performs server-side validation against the declarative pipeline schema. This catches structural issues like invalid stage definitions, missing required sections, and unsupported step configurations.

For deeper analysis, the skill runs npm-groovy-lint with CodeNarc rulesets to perform static analysis on both declarative and scripted pipeline Groovy code. It detects common issues including hardcoded credentials, missing timeout blocks, unbounded retry loops, and insecure script approvals. The linter checks for pipeline best practices such as proper use of parallel stages, stash/unstash patterns, shared library imports, and agent allocation strategies. It generates reports with specific line references and suggested fixes, supporting both local validation and integration as a PR check via the Jenkins GitHub plugin webhook.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-6
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-6 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-6 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-6 -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-linter-6
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/)
