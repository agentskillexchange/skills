---
title: "Jenkins Shared Library Auditor"
description: "Audits Jenkins shared libraries for security vulnerabilities using the Jenkins Script Console API and Groovy AST analysis. Detects unsafe method calls, credential leaks, and sandbox escapes in pipeline libraries."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Shared Library Auditor

The Jenkins Shared Library Auditor performs deep security analysis of Jenkins shared libraries by combining Groovy AST parsing with Jenkins API inspection. It connects to the Jenkins Script Console API to enumerate loaded libraries, then analyzes each library’s source code for security anti-patterns.

Detection capabilities include identifying unsafe @Grab annotations, credential access outside approved patterns, sandbox escape techniques, arbitrary script execution, and insecure deserialization. The auditor also checks library version pinning, verifies SCM source integrity, and validates that library trust configurations match organizational security policies.

The agent generates detailed audit reports with severity ratings, remediation guidance, and automated fix suggestions. It can integrate with Jenkins Configuration as Code (JCasC) to enforce library allowlists and version constraints. Supports both declarative and scripted pipeline syntax analysis across multiple Jenkins controller instances.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-auditor-agent/)
