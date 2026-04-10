---
title: "Jenkins Pipeline Code Review Agent"
description: "Reviews Jenkinsfile and Groovy pipeline scripts for anti-patterns, security issues, and performance bottlenecks using Jenkins Pipeline Linter API and static analysis rules."
slug: "jenkins-pipeline-code-review-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/"
listed: true
---

# Jenkins Pipeline Code Review Agent

Reviews Jenkinsfile and Groovy pipeline scripts for anti-patterns, security issues, and performance bottlenecks using Jenkins Pipeline Linter API and static analysis rules.

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
clawhub install jenkins-pipeline-code-review-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/)
