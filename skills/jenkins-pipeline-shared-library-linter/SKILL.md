---
title: "Jenkins Pipeline Shared Library Linter"
description: "Lints Jenkins Declarative and Scripted pipeline syntax using the Jenkins REST API and the Jenkins CLI jar. Checks Jenkinsfile syntax against a live or sandbox Jenkins controller using the /pipeline-model-converter/validate endpoint. Reports errors with line numbers and suggested fixes."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Shared Library Linter

This skill automates linting of Jenkins pipeline files by interacting with the Jenkins REST API and the Jenkins CLI jar. It posts Jenkinsfile content to the /pipeline-model-converter/validate endpoint on a configured Jenkins controller, parses the JSON response for syntax errors, and reports them with exact line numbers and suggested corrections. The skill supports both Declarative and Scripted pipeline syntax, handles authentication via Jenkins API tokens, and works with multibranch pipelines. It integrates with GitHub webhooks and GitLab CI triggers to run on every pull request. Configuration covers Jenkins controller URL, credentials, and branch-specific overrides. Output is formatted for terminal, GitHub Checks annotations, and Slack notifications via the Slack Notification Plugin. Useful for preventing broken pipeline code from merging into protected branches.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-shared-library-linter/)
