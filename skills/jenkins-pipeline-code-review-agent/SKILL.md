---
name: "Jenkins Pipeline Code Review Agent"
description: "Reviews Jenkinsfile and Groovy pipeline scripts for anti-patterns, security issues, and performance bottlenecks using Jenkins Pipeline Linter API and static analysis rules."
category: "Code Quality & Review"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/"
tool_ecosystem:
  tool: jenkins
  github_stars: 25122
  github_repo: jenkinsci/jenkins
  license: MIT
  maintained: true
---

# Jenkins Pipeline Code Review Agent

Reviews Jenkinsfile and Groovy pipeline scripts for anti-patterns, security issues, and performance bottlenecks using Jenkins Pipeline Linter API and static analysis rules.

## Overview

The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-code-review-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-code-review-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-code-review-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-code-review-agent -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-code-review-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/
