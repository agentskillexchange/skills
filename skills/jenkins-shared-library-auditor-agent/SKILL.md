---
title: "Jenkins Shared Library Auditor"
description: "The Jenkins Shared Library Auditor performs deep security analysis of Jenkins shared libraries by combining Groovy AST parsing with Jenkins API inspection. It connects to the Jenkins Script Console API to enumerate loaded libraries, then analyzes each library&#8217;s source code for security anti-patterns. Detection capabilities include identifying unsafe @Grab annotations, credential access outside approved patterns, sandbox escape techniques, arbitrary script execution, and insecure deserialization. The auditor also checks library version pinning, verifies SCM source integrity, and validates that library trust configurations match organizational security policies. The agent generates detailed audit reports with severity ratings, remediation guidance, and automated fix suggestions. It can integrate with Jenkins Configuration as Code (JCasC) to enforce library allowlists and version constraints. Supports both declarative and scripted pipeline syntax analysis across multiple Jenkins controller instances."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Auditor

The Jenkins Shared Library Auditor performs deep security analysis of Jenkins shared libraries by combining Groovy AST parsing with Jenkins API inspection. It connects to the Jenkins Script Console API to enumerate loaded libraries, then analyzes each library&#8217;s source code for security anti-patterns. Detection capabilities include identifying unsafe @Grab annotations, credential access outside approved patterns, sandbox escape techniques, arbitrary script execution, and insecure deserialization. The auditor also checks library version pinning, verifies SCM source integrity, and validates that library trust configurations match organizational security policies. The agent generates detailed audit reports with severity ratings, remediation guidance, and automated fix suggestions. It can integrate with Jenkins Configuration as Code (JCasC) to enforce library allowlists and version constraints. Supports both declarative and scripted pipeline syntax analysis across multiple Jenkins controller instances.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/)
