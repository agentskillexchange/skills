---
name: "Jenkins Shared Library Auditor"
description: "Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
tool_ecosystem:
  tool: jenkins
  github_repo: jenkinsci/jenkins
  github_stars: 25143
  license: MIT
  maintained: true
---
# Jenkins Shared Library Auditor

Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries.

## Overview

The Jenkins Shared Library Auditor performs deep security analysis of Jenkins shared libraries by combining Groovy AST parsing with Jenkins API inspection. It connects to the Jenkins Script Console API to enumerate loaded libraries, then analyzes each library's source code for security anti-patterns.

Detection capabilities include identifying unsafe @Grab annotations, credential access outside approved patterns, sandbox escape techniques, arbitrary script execution, and insecure deserialization. The auditor also checks library version pinning, verifies SCM source integrity, and validates that library trust configurations match organizational security policies.

The agent generates detailed audit reports with severity ratings, remediation guidance, and automated fix suggestions. It can integrate with Jenkins Configuration as Code (JCasC) to enforce library allowlists and version constraints. Supports both declarative and scripted pipeline syntax analysis across multiple Jenkins controller instances.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-auditor-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-auditor-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-auditor-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-shared-library-auditor-agent -a codex
```

### OpenClaw

```bash
clawhub install jenkins-shared-library-auditor-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/)
