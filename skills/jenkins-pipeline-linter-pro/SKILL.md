---
name: "Jenkins Pipeline Linter Pro"
description: "Validates Jenkinsfile syntax and best practices using the Jenkins Pipeline Model Definition API and jenkins-cli.jar linter endpoint. Detects anti-patterns like unbounded parallel stages, missing timeout blocks, and credential leaks."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_stars: 25122
  github_repo: jenkinsci/jenkins
  license: MIT
  maintained: true
---

# Jenkins Pipeline Linter Pro

Validates Jenkinsfile syntax and best practices using the Jenkins Pipeline Model Definition API and jenkins-cli.jar linter endpoint. Detects anti-patterns like unbounded parallel stages, missing timeout blocks, and credential leaks.

## Overview

Jenkins Pipeline Linter Pro provides deep static analysis of Jenkinsfile configurations, going far beyond basic syntax validation to enforce CI/CD best practices and security policies. It interfaces with the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and uses the jenkins-cli.jar linter endpoint for scripted pipeline verification.

The linter detects common anti-patterns including unbounded parallel stages that can exhaust executor capacity, missing timeout blocks that allow hung builds to consume resources indefinitely, and credential usage patterns that risk secret exposure in console logs. It analyzes withCredentials blocks to ensure sensitive values are properly masked.

Shared library references are resolved and validated against the configured library versions, flagging incompatible method signatures or deprecated library functions. The skill checks agent labels against available node configurations to prevent pipeline failures from missing executors.

Advanced features include Groovy sandbox escape detection for scripted pipelines, resource lock analysis to identify potential deadlocks in parallel stages, artifact archival best practices, and stash/unstash optimization recommendations. The linter generates both human-readable reports and machine-parseable JSON output for integration with PR status checks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-pro
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-pro -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-pro -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-pro -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-linter-pro
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-linter-pro/
