---
name: "Jenkins Shared Library Linter"
description: "Validates Jenkins Shared Library Groovy code using the Jenkins Pipeline Model Definition API and Groovy AST parser. Catches syntax errors and anti-patterns before pipeline execution."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-shared-library-linter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/jenkins-shared-library-linter/
