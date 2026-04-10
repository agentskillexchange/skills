---
title: "Jenkins Groovy Shared Library Auditor"
description: "Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code."
slug: "jenkins-groovy-shared-library-auditor"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/"
listed: true
---

# Jenkins Groovy Shared Library Auditor

Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code.

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
clawhub install jenkins-groovy-shared-library-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin’s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access.
The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization’s governance policy.
Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization’s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
