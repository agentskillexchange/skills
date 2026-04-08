---
title: Jenkins Shared Library Manager
description: The Jenkins Shared Library Manager skill streamlines the development
  and maintenance of Jenkins Pipeline shared libraries. It scaffolds library repositories
  with proper vars/ (global variables/steps), src/ (Groovy classes), and resources/
  directory structures following Jenkins conventions. The skill creates custom pipeline
  steps in vars/ as Groovy scripts with call() methods, supporting both scripted and
  declarative pipeline syntax. Each step includes proper parameter handling, error
  management with try/catch blocks, and currentBuild status updates. Utility classes
  in src/ follow the standard Groovy package structure and implement Serializable
  for pipeline CPS compatibility. Testing is automated using the jenkins-pipeline-unit
  framework (JenkinsPipelineUnit). The skill generates Spock or JUnit test specifications
  that mock Jenkins pipeline steps, validate library behavior, and ensure Groovy compilation.
  It configures Gradle build scripts with the groovy plugin for local development
  and testing. Library configuration uses the Jenkins CLI or REST API to register
  libraries as Global Pipeline Libraries with proper SCM settings, version defaults,
  and load implicitly options. The skill handles library versioning with git tags
  and branch-based loading via @Library annotations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-shared-library-manager/
category:
- CI/CD Integrations
framework:
- MCP
---

# Jenkins Shared Library Manager

The Jenkins Shared Library Manager skill streamlines the development and maintenance of Jenkins Pipeline shared libraries. It scaffolds library repositories with proper vars/ (global variables/steps), src/ (Groovy classes), and resources/ directory structures following Jenkins conventions. The skill creates custom pipeline steps in vars/ as Groovy scripts with call() methods, supporting both scripted and declarative pipeline syntax. Each step includes proper parameter handling, error management with try/catch blocks, and currentBuild status updates. Utility classes in src/ follow the standard Groovy package structure and implement Serializable for pipeline CPS compatibility. Testing is automated using the jenkins-pipeline-unit framework (JenkinsPipelineUnit). The skill generates Spock or JUnit test specifications that mock Jenkins pipeline steps, validate library behavior, and ensure Groovy compilation. It configures Gradle build scripts with the groovy plugin for local development and testing. Library configuration uses the Jenkins CLI or REST API to register libraries as Global Pipeline Libraries with proper SCM settings, version defaults, and load implicitly options. The skill handles library versioning with git tags and branch-based loading via @Library annotations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-manager/)
