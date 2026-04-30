---
title: "Jenkins Groovy Shared Library Auditor"
description: "Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Groovy Shared Library Auditor

Audits Jenkins shared library Groovy scripts for security anti-patterns using the Script Security Plugin API. Detects unapproved method signatures, sandbox escapes, and credential leakage in pipeline code.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-groovy-shared-library-auditor/)
