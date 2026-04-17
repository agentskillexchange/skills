---
title: "Jenkins Pipeline Linter"
description: "The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions before they reach the CI server, catching syntax errors, anti-patterns, and security issues early in the development process. It uses two complementary validation approaches for comprehensive coverage.\nFor declarative pipelines, the skill submits Jenkinsfile content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate, which performs server-side validation against the declarative pipeline schema. This catches structural issues like invalid stage definitions, missing required sections, and unsupported step configurations.\nFor deeper analysis, the skill runs npm-groovy-lint with CodeNarc rulesets to perform static analysis on both declarative and scripted pipeline Groovy code. It detects common issues including hardcoded credentials, missing timeout blocks, unbounded retry loops, and insecure script approvals. The linter checks for pipeline best practices such as proper use of parallel stages, stash/unstash patterns, shared library imports, and agent allocation strategies. It generates reports with specific line references and suggested fixes, supporting both local validation and integration as a PR check via the Jenkins GitHub plugin webhook."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-linter-6
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-linter-6` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/)
