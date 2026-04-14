---
title: "Jenkins Shared Library Linter"
description: "Validates Jenkins Shared Library Groovy code using the Jenkins Pipeline Model Definition API and Groovy AST parser. Catches syntax errors and anti-patterns before pipeline execution."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Linter

The Jenkins Shared Library Linter skill provides static analysis for Jenkins Shared Libraries written in Groovy. It uses the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and the Groovy Abstract Syntax Tree parser for deeper code inspection.

The skill checks for common anti-patterns including unapproved script security calls, CPS transformation issues with @NonCPS annotations, and improper use of Jenkins pipeline steps in library code. It validates against the Jenkins Script Security Plugin approved signatures list.

Using the Jenkins REST API, the skill can connect to a running Jenkins instance to verify that referenced plugins and pipeline steps actually exist. It also checks Shared Library version pinning in Jenkinsfile configurations and warns about floating branch references.

Output formats include JUnit-compatible XML for CI integration, SARIF for GitHub/GitLab security dashboards, and human-readable console output. The skill supports custom rule definitions via a YAML configuration file for organization-specific conventions.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-linter/)
