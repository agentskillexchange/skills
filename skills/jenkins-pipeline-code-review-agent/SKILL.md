---
title: "Jenkins Pipeline Code Review Agent"
description: "Reviews Jenkinsfile and Groovy pipeline scripts for anti-patterns, security issues, and performance bottlenecks using Jenkins Pipeline Linter API and static analysis rules."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "Code Quality & Review"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Code Review Agent

The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/)
