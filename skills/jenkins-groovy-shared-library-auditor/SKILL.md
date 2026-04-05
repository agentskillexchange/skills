---
name: "Jenkins Groovy Shared Library Auditor"
description: "Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/"
---
# Jenkins Groovy Shared Library Auditor

Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code.

The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin’s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access.



The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization’s governance policy.



Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization’s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-groovy-shared-library-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-groovy-shared-library-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-groovy-shared-library-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-groovy-shared-library-auditor -a codex
```

### OpenClaw

```bash
clawhub install jenkins-groovy-shared-library-auditor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
