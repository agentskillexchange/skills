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

Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-shared-library-auditor-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-shared-library-auditor-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/)
