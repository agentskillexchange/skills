---
title: Jenkins Pipeline Code Review Agent
description: The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile
  and shared library Groovy code to identify quality issues before they reach production.
  It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies
  custom rule sets for detecting common anti-patterns such as unbounded resource allocation,
  missing timeout blocks, improper credential handling, and non-deterministic parallel
  stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version
  compatibility, and flags insecure script approvals. It analyzes Declarative and
  Scripted pipeline syntax, checking for proper use of agent directives, post-condition
  blocks, and error handling patterns. The skill also reviews shared library implementations
  for proper @NonCPS annotations, checks for serialization issues in CPS-transformed
  code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked
  findings with fix suggestions, links to Jenkins documentation, and automated pull
  request comments via the GitHub Checks API integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/
category:
- Code Quality &amp; Review
framework:
- Cursor
---

# Jenkins Pipeline Code Review Agent

The Jenkins Pipeline Code Review Agent performs deep analysis of Jenkinsfile and shared library Groovy code to identify quality issues before they reach production. It integrates with the Jenkins Pipeline Linter API to validate syntax, then applies custom rule sets for detecting common anti-patterns such as unbounded resource allocation, missing timeout blocks, improper credential handling, and non-deterministic parallel stages. The agent checks for deprecated Jenkins plugin APIs, validates plugin version compatibility, and flags insecure script approvals. It analyzes Declarative and Scripted pipeline syntax, checking for proper use of agent directives, post-condition blocks, and error handling patterns. The skill also reviews shared library implementations for proper @NonCPS annotations, checks for serialization issues in CPS-transformed code, and validates proper use of the Jenkins Credentials API. Reports include severity-ranked findings with fix suggestions, links to Jenkins documentation, and automated pull request comments via the GitHub Checks API integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-code-review-agent/)
