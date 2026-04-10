---
name: "Jenkins Pipeline Linter & Fixer"
description: "Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax issues and stages missing agent directives."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Jenkins Pipeline Linter & Fixer

The Jenkins Pipeline Linter & Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing.
The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting.
Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues.
Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
