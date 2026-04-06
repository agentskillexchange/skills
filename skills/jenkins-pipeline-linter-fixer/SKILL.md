---
name: "Jenkins Pipeline Linter & Fixer"
description: Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline
  Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax
  issues and stages missing agent directives.
category: CI/CD Integrations
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/"
---
# Jenkins Pipeline Linter & Fixer

Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax issues and stages missing agent directives.

The Jenkins Pipeline Linter & Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing.

The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting.

Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues.

Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-fixer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-fixer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-fixer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-linter-fixer -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-linter-fixer
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
