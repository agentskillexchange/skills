---
name: "Jenkins Pipeline Linter Agent"
description: "Validates Jenkinsfile syntax using the Jenkins Pipeline Linter REST API before commits. Integrates with jenkins-client npm SDK to authenticate and submit declarative or scripted pipelines for server-side validation."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-pipeline-linter-agent-2/"
tool_ecosystem:
  tool: "jenkins"
  github_stars: 25122
  github_repo: "jenkinsci/jenkins"
  license: "MIT"
  maintained: true
---

# Jenkins Pipeline Linter Agent

Validates Jenkinsfile syntax using the Jenkins Pipeline Linter REST API before commits. Integrates with jenkins-client npm SDK to authenticate and submit declarative or scripted pipelines for server-side validation.

## Overview

The Jenkins Pipeline Linter Agent leverages the Jenkins Pipeline Linter REST API endpoint (/pipeline-model-converter/validate) to validate Jenkinsfile syntax before code is committed. Built on the jenkins-client npm SDK, this skill authenticates against your Jenkins instance using API tokens or SSO credentials, then submits pipeline definitions for server-side syntax checking. It supports both declarative and scripted pipeline formats, parsing validation responses to surface specific line-number errors and warnings. The agent can be integrated into pre-commit hooks or CI gate steps to prevent broken pipelines from reaching the build queue. It caches authentication tokens for session reuse and supports Jenkins instances behind reverse proxies. Configuration accepts multiple Jenkins controller URLs for organizations running distributed Jenkins setups across environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-linter-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-linter-agent-2/
