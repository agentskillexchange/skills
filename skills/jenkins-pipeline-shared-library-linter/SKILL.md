---
title: Jenkins Pipeline Shared Library Linter
description: This skill automates linting of Jenkins pipeline files by interacting
  with the Jenkins REST API and the Jenkins CLI jar. It posts Jenkinsfile content
  to the /pipeline-model-converter/validate endpoint on a configured Jenkins controller,
  parses the JSON response for syntax errors, and reports them with exact line numbers
  and suggested corrections. The skill supports both Declarative and Scripted pipeline
  syntax, handles authentication via Jenkins API tokens, and works with multibranch
  pipelines. It integrates with GitHub webhooks and GitLab CI triggers to run on every
  pull request. Configuration covers Jenkins controller URL, credentials, and branch-specific
  overrides. Output is formatted for terminal, GitHub Checks annotations, and Slack
  notifications via the Slack Notification Plugin. Useful for preventing broken pipeline
  code from merging into protected branches.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/
category:
- CI/CD Integrations
framework:
- Codex
---

# Jenkins Pipeline Shared Library Linter

This skill automates linting of Jenkins pipeline files by interacting with the Jenkins REST API and the Jenkins CLI jar. It posts Jenkinsfile content to the /pipeline-model-converter/validate endpoint on a configured Jenkins controller, parses the JSON response for syntax errors, and reports them with exact line numbers and suggested corrections. The skill supports both Declarative and Scripted pipeline syntax, handles authentication via Jenkins API tokens, and works with multibranch pipelines. It integrates with GitHub webhooks and GitLab CI triggers to run on every pull request. Configuration covers Jenkins controller URL, credentials, and branch-specific overrides. Output is formatted for terminal, GitHub Checks annotations, and Slack notifications via the Slack Notification Plugin. Useful for preventing broken pipeline code from merging into protected branches.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/)
