---
title: "Jenkins Pipeline Linter &#038; Fixer"
description: "The Jenkins Pipeline Linter &#038; Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing. The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting. Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues. Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Linter &#038; Fixer

The Jenkins Pipeline Linter &#038; Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing. The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting. Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues. Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
