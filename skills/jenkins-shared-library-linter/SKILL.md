---
title: "Jenkins Shared Library Linter"
description: "The Jenkins Shared Library Linter skill provides static analysis for Jenkins Shared Libraries written in Groovy. It uses the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and the Groovy Abstract Syntax Tree parser for deeper code inspection. The skill checks for common anti-patterns including unapproved script security calls, CPS transformation issues with @NonCPS annotations, and improper use of Jenkins pipeline steps in library code. It validates against the Jenkins Script Security Plugin approved signatures list. Using the Jenkins REST API, the skill can connect to a running Jenkins instance to verify that referenced plugins and pipeline steps actually exist. It also checks Shared Library version pinning in Jenkinsfile configurations and warns about floating branch references. Output formats include JUnit-compatible XML for CI integration, SARIF for GitHub/GitLab security dashboards, and human-readable console output. The skill supports custom rule definitions via a YAML configuration file for organization-specific conventions."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Linter

The Jenkins Shared Library Linter skill provides static analysis for Jenkins Shared Libraries written in Groovy. It uses the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and the Groovy Abstract Syntax Tree parser for deeper code inspection. The skill checks for common anti-patterns including unapproved script security calls, CPS transformation issues with @NonCPS annotations, and improper use of Jenkins pipeline steps in library code. It validates against the Jenkins Script Security Plugin approved signatures list. Using the Jenkins REST API, the skill can connect to a running Jenkins instance to verify that referenced plugins and pipeline steps actually exist. It also checks Shared Library version pinning in Jenkinsfile configurations and warns about floating branch references. Output formats include JUnit-compatible XML for CI integration, SARIF for GitHub/GitLab security dashboards, and human-readable console output. The skill supports custom rule definitions via a YAML configuration file for organization-specific conventions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-linter/)
