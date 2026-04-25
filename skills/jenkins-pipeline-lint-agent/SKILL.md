---
title: "Jenkins Pipeline Lint Agent"
description: "Validates Jenkinsfile declarative and scripted pipelines using the Jenkins Pipeline Linter API endpoint. Checks for deprecated step usage, security anti-patterns, and Groovy sandbox violations."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Lint Agent

The Jenkins Pipeline Lint Agent skill submits Jenkinsfile contents to the Jenkins /pipeline-model-converter/validate REST endpoint for server-side syntax validation. Beyond basic linting, it performs static analysis on both declarative and scripted pipeline syntax to detect deprecated step names, insecure credential handling patterns, and Groovy sandbox escape attempts. The skill maintains a knowledge base of Jenkins plugin compatibility matrices, flagging steps that require specific plugin versions. It checks for common anti-patterns like unbounded node blocks, missing timeout wrappers, and improper shared library imports. The agent can process multi-branch pipeline configurations, validating Jenkinsfile variants across branches via the Jenkins Blue Ocean REST API. Results include line-level annotations with fix suggestions, severity ratings, and links to Jenkins documentation for each finding.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-lint-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-pipeline-lint-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/)
