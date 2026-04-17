---
title: "Jenkins Pipeline Linter & Fixer"
description: "Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax issues and stages missing agent directives."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Pipeline Linter & Fixer

The Jenkins Pipeline Linter & Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing.

The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting.

Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues.

Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-pipeline-linter-fixer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-pipeline-linter-fixer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
