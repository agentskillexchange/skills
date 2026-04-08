---
title: Jenkins Pipeline Linter & Fixer
description: The Jenkins Pipeline Linter & Fixer skill provides automated validation
  and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code
  to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch
  structural errors before committing. The fixer component addresses common mistakes
  including missing agent directives on stages, incorrect when/expression closures,
  and malformed environment blocks. It uses AST-level manipulation of the Groovy-based
  pipeline DSL to apply corrections while preserving comments and formatting. Integration
  with the Jenkins REST API (/api/json) allows fetching build history to correlate
  lint warnings with actual build failures. The skill can pull console output from
  failed builds to identify runtime pipeline errors distinct from syntax issues. Shared
  library validation covers @Library annotations and checks function signatures against
  the configured Global Pipeline Libraries repository. The skill supports both Scripted
  and Declarative pipeline styles with different validation rule sets. It generates
  diff output showing proposed fixes in unified diff format for code review integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/
category:
- CI/CD Integrations
framework:
- Cursor
---

# Jenkins Pipeline Linter & Fixer

The Jenkins Pipeline Linter & Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing. The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting. Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues. Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
