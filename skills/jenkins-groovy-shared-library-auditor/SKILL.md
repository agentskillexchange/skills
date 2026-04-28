---
title: Jenkins Groovy Shared Library Auditor
description: Audits Jenkins shared library Groovy scripts for security anti-patterns
  using the Script Security Plugin API. Detects unapproved method signatures, sandbox
  escapes, and credential leakage in pipeline code.
verification: security_reviewed
source: https://github.com/jenkinsci/jenkins
category:
- CI/CD Integrations
framework:
- OpenClaw
tool_ecosystem:
  github_repo: jenkinsci/jenkins
  github_stars: 25189
---

# Jenkins Groovy Shared Library Auditor

Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-groovy-shared-library-auditor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jenkins-groovy-shared-library-auditor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
