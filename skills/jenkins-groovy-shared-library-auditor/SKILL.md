---
title: "Jenkins Groovy Shared Library Auditor"
description: "The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin&#8217;s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access. The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization&#8217;s governance policy. Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization&#8217;s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Groovy Shared Library Auditor

The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin&#8217;s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access. The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization&#8217;s governance policy. Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization&#8217;s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
