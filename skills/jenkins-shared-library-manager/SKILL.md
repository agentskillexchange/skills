---
title: "Jenkins Shared Library Manager"
description: "Manages Jenkins Shared Libraries with proper vars/ and src/ structure using the Jenkins Pipeline Shared Groovy Libraries plugin. Validates Groovy syntax, tests steps with jenkins-pipeline-unit, and configures Global Pipeline Libraries via Jenkins CLI."
verification: "security_reviewed"
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
  license: "MIT"
---

# Jenkins Shared Library Manager

The Jenkins Shared Library Manager skill streamlines the development and maintenance of Jenkins Pipeline shared libraries. It scaffolds library repositories with proper vars/ (global variables/steps), src/ (Groovy classes), and resources/ directory structures following Jenkins conventions.

The skill creates custom pipeline steps in vars/ as Groovy scripts with call() methods, supporting both scripted and declarative pipeline syntax. Each step includes proper parameter handling, error management with try/catch blocks, and currentBuild status updates. Utility classes in src/ follow the standard Groovy package structure and implement Serializable for pipeline CPS compatibility.

Testing is automated using the jenkins-pipeline-unit framework (JenkinsPipelineUnit). The skill generates Spock or JUnit test specifications that mock Jenkins pipeline steps, validate library behavior, and ensure Groovy compilation. It configures Gradle build scripts with the groovy plugin for local development and testing.

Library configuration uses the Jenkins CLI or REST API to register libraries as Global Pipeline Libraries with proper SCM settings, version defaults, and load implicitly options. The skill handles library versioning with git tags and branch-based loading via @Library annotations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-manager/)
