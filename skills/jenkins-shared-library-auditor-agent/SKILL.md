---
name: Jenkins Shared Library Auditor
description: Audits Jenkins shared libraries for security vulnerabilities using the
  Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls,
  credential leaks, and sandbox escapes in pipeline libraries.
category: CI/CD Integrations
framework: Cursor
verification: security_reviewed
source: https://github.com/jenkinsci/jenkins
tool_ecosystem:
  github_repo: jenkinsci/jenkins
  github_stars: 25189
  tool: jenkins
  license: MIT
  maintained: true
---
# Jenkins Shared Library Auditor
Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries.

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
