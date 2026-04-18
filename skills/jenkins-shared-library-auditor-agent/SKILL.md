---
title: "Jenkins Shared Library Auditor"
description: "Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Auditor

The Jenkins Shared Library Auditor performs deep security analysis of Jenkins shared libraries by combining Groovy AST parsing with Jenkins API inspection. It connects to the Jenkins Script Console API to enumerate loaded libraries, then analyzes each library’s source code for security anti-patterns.

Detection capabilities include identifying unsafe @Grab annotations, credential access outside approved patterns, sandbox escape techniques, arbitrary script execution, and insecure deserialization. The auditor also checks library version pinning, verifies SCM source integrity, and validates that library trust configurations match organizational security policies.

The agent generates detailed audit reports with severity ratings, remediation guidance, and automated fix suggestions. It can integrate with Jenkins Configuration as Code (JCasC) to enforce library allowlists and version constraints. Supports both declarative and scripted pipeline syntax analysis across multiple Jenkins controller instances.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-shared-library-auditor-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-shared-library-auditor-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/)
