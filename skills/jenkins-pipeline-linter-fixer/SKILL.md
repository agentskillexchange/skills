---
title: "Jenkins Pipeline Linter & Fixer"
description: "Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax issues and stages missing agent directives."
slug: "jenkins-pipeline-linter-fixer"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/"
listed: true
---

# Jenkins Pipeline Linter & Fixer

Validates Jenkinsfile declarative pipelines using the Jenkins Pipeline Linter API endpoint (/pipeline-model-converter/validate). Auto-fixes common syntax issues and stages missing agent directives.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install jenkins-pipeline-linter-fixer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Pipeline Linter & Fixer skill provides automated validation and correction of Jenkinsfile declarative pipeline syntax. It submits pipeline code to the Jenkins Pipeline Linter API at /pipeline-model-converter/validate to catch structural errors before committing.
The fixer component addresses common mistakes including missing agent directives on stages, incorrect when/expression closures, and malformed environment blocks. It uses AST-level manipulation of the Groovy-based pipeline DSL to apply corrections while preserving comments and formatting.
Integration with the Jenkins REST API (/api/json) allows fetching build history to correlate lint warnings with actual build failures. The skill can pull console output from failed builds to identify runtime pipeline errors distinct from syntax issues.
Shared library validation covers @Library annotations and checks function signatures against the configured Global Pipeline Libraries repository. The skill supports both Scripted and Declarative pipeline styles with different validation rule sets. It generates diff output showing proposed fixes in unified diff format for code review integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-fixer/)
