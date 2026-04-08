---
title: Jenkins Groovy Shared Library Auditor
description: The Jenkins Groovy Shared Library Auditor skill performs deep security
  analysis of Jenkins shared library code by cross-referencing method calls against
  the Script Security Plugin’s approved signatures list. It parses Groovy AST to detect
  patterns that could lead to sandbox escapes, credential exposure, or unauthorized
  system access. The skill checks vars/ and src/ directories for dangerous patterns
  including @Grab annotations that pull external dependencies, direct use of Jenkins.instance
  or hudson.model classes, credential binding misuse via withCredentials blocks, and
  shell injection through unescaped string interpolation in sh steps. It also validates
  that library versions pinned in @Library annotations match approved versions in
  your organization’s governance policy. Integration with the Jenkins REST API allows
  real-time checking of scriptApproval pending queues and comparison against your
  organization’s allowlist. Outputs SARIF-compatible reports for integration with
  GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and
  Scripted pipeline syntax analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# Jenkins Groovy Shared Library Auditor

The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin’s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access. The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization’s governance policy. Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization’s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
