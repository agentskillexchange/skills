---
title: "Jenkins Groovy Shared Library Auditor"
description: "Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Groovy Shared Library Auditor

The Jenkins Groovy Shared Library Auditor skill performs deep security analysis of Jenkins shared library code by cross-referencing method calls against the Script Security Plugin’s approved signatures list. It parses Groovy AST to detect patterns that could lead to sandbox escapes, credential exposure, or unauthorized system access.

The skill checks vars/ and src/ directories for dangerous patterns including @Grab annotations that pull external dependencies, direct use of Jenkins.instance or hudson.model classes, credential binding misuse via withCredentials blocks, and shell injection through unescaped string interpolation in sh steps. It also validates that library versions pinned in @Library annotations match approved versions in your organization’s governance policy.

Integration with the Jenkins REST API allows real-time checking of scriptApproval pending queues and comparison against your organization’s allowlist. Outputs SARIF-compatible reports for integration with GitHub Advanced Security or SonarQube dashboards. Supports both Declarative and Scripted pipeline syntax analysis.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
