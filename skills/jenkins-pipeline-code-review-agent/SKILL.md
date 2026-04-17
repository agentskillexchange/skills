---
title: "Jenkins Pipeline Code Review Agent"
description: "The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Code Review Agent

The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-code-review-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-code-review-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/)
