---
name: Jenkins Shared Library Linter
description: Validates Jenkins Shared Library Groovy code using the Jenkins Pipeline
  Model Definition API and Groovy AST parser. Catches syntax errors and anti-patterns
  before pipeline execution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-shared-library-linter/
category:
- CI/CD Integrations
framework:
- Codex
---
# Jenkins Shared Library Linter

The Jenkins Shared Library Linter skill provides static analysis for Jenkins Shared Libraries written in Groovy. It uses the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and the Groovy Abstract Syntax Tree parser for deeper code inspection.
The skill checks for common anti-patterns including unapproved script security calls, CPS transformation issues with @NonCPS annotations, and improper use of Jenkins pipeline steps in library code. It validates against the Jenkins Script Security Plugin approved signatures list.
Using the Jenkins REST API, the skill can connect to a running Jenkins instance to verify that referenced plugins and pipeline steps actually exist. It also checks Shared Library version pinning in Jenkinsfile configurations and warns about floating branch references.
Output formats include JUnit-compatible XML for CI integration, SARIF for GitHub/GitLab security dashboards, and human-readable console output. The skill supports custom rule definitions via a YAML configuration file for organization-specific conventions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-linter/)
