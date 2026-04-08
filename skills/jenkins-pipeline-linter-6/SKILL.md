---
title: Jenkins Pipeline Linter
description: The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions
  before they reach the CI server, catching syntax errors, anti-patterns, and security
  issues early in the development process. It uses two complementary validation approaches
  for comprehensive coverage. For declarative pipelines, the skill submits Jenkinsfile
  content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate,
  which performs server-side validation against the declarative pipeline schema. This
  catches structural issues like invalid stage definitions, missing required sections,
  and unsupported step configurations. For deeper analysis, the skill runs npm-groovy-lint
  with CodeNarc rulesets to perform static analysis on both declarative and scripted
  pipeline Groovy code. It detects common issues including hardcoded credentials,
  missing timeout blocks, unbounded retry loops, and insecure script approvals. The
  linter checks for pipeline best practices such as proper use of parallel stages,
  stash/unstash patterns, shared library imports, and agent allocation strategies.
  It generates reports with specific line references and suggested fixes, supporting
  both local validation and integration as a PR check via the Jenkins GitHub plugin
  webhook.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/
category:
- CI/CD Integrations
framework:
- Custom Agents
---

# Jenkins Pipeline Linter

The Jenkins Pipeline Linter skill validates Jenkins pipeline definitions before they reach the CI server, catching syntax errors, anti-patterns, and security issues early in the development process. It uses two complementary validation approaches for comprehensive coverage. For declarative pipelines, the skill submits Jenkinsfile content to the Jenkins Pipeline Linter HTTP API at /pipeline-model-converter/validate, which performs server-side validation against the declarative pipeline schema. This catches structural issues like invalid stage definitions, missing required sections, and unsupported step configurations. For deeper analysis, the skill runs npm-groovy-lint with CodeNarc rulesets to perform static analysis on both declarative and scripted pipeline Groovy code. It detects common issues including hardcoded credentials, missing timeout blocks, unbounded retry loops, and insecure script approvals. The linter checks for pipeline best practices such as proper use of parallel stages, stash/unstash patterns, shared library imports, and agent allocation strategies. It generates reports with specific line references and suggested fixes, supporting both local validation and integration as a PR check via the Jenkins GitHub plugin webhook.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-6/)
