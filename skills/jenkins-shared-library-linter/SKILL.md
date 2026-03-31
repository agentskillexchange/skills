---
name: "Jenkins Shared Library Linter"
description: "Validates Jenkins Shared Library Groovy code using the Jenkins Pipeline Model Definition API and Groovy AST parser. Catches syntax errors and anti-patterns before pipeline execution."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_repo: jenkinsci/jenkins
  github_stars: 25143
  license: MIT
  maintained: true
---
# Jenkins Shared Library Linter

Validates Jenkins Shared Library Groovy code using the Jenkins Pipeline Model Definition API and Groovy AST parser. Catches syntax errors and anti-patterns before pipeline execution.

## Overview

The Jenkins Shared Library Linter skill provides static analysis for Jenkins Shared Libraries written in Groovy. It uses the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and the Groovy Abstract Syntax Tree parser for deeper code inspection.

The skill checks for common anti-patterns including unapproved script security calls, CPS transformation issues with @NonCPS annotations, and improper use of Jenkins pipeline steps in library code. It validates against the Jenkins Script Security Plugin approved signatures list.

Using the Jenkins REST API, the skill can connect to a running Jenkins instance to verify that referenced plugins and pipeline steps actually exist. It also checks Shared Library version pinning in Jenkinsfile configurations and warns about floating branch references.

Output formats include JUnit-compatible XML for CI integration, SARIF for GitHub/GitLab security dashboards, and human-readable console output. The skill supports custom rule definitions via a YAML configuration file for organization-specific conventions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-linter -a codex
```

### OpenClaw

```bash
clawhub install jenkins-shared-library-linter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-linter/)
