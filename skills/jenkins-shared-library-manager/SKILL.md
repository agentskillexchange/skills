---
title: "Jenkins Shared Library Manager"
description: "The Jenkins Shared Library Manager skill streamlines the development and maintenance of Jenkins Pipeline shared libraries. It scaffolds library repositories with proper vars/ (global variables/steps), src/ (Groovy classes), and resources/ directory structures following Jenkins conventions.\nThe skill creates custom pipeline steps in vars/ as Groovy scripts with call() methods, supporting both scripted and declarative pipeline syntax. Each step includes proper parameter handling, error management with try/catch blocks, and currentBuild status updates. Utility classes in src/ follow the standard Groovy package structure and implement Serializable for pipeline CPS compatibility.\nTesting is automated using the jenkins-pipeline-unit framework (JenkinsPipelineUnit). The skill generates Spock or JUnit test specifications that mock Jenkins pipeline steps, validate library behavior, and ensure Groovy compilation. It configures Gradle build scripts with the groovy plugin for local development and testing.\nLibrary configuration uses the Jenkins CLI or REST API to register libraries as Global Pipeline Libraries with proper SCM settings, version defaults, and load implicitly options. The skill handles library versioning with git tags and branch-based loading via @Library annotations."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Manager

The Jenkins Shared Library Manager skill streamlines the development and maintenance of Jenkins Pipeline shared libraries. It scaffolds library repositories with proper vars/ (global variables/steps), src/ (Groovy classes), and resources/ directory structures following Jenkins conventions.
The skill creates custom pipeline steps in vars/ as Groovy scripts with call() methods, supporting both scripted and declarative pipeline syntax. Each step includes proper parameter handling, error management with try/catch blocks, and currentBuild status updates. Utility classes in src/ follow the standard Groovy package structure and implement Serializable for pipeline CPS compatibility.
Testing is automated using the jenkins-pipeline-unit framework (JenkinsPipelineUnit). The skill generates Spock or JUnit test specifications that mock Jenkins pipeline steps, validate library behavior, and ensure Groovy compilation. It configures Gradle build scripts with the groovy plugin for local development and testing.
Library configuration uses the Jenkins CLI or REST API to register libraries as Global Pipeline Libraries with proper SCM settings, version defaults, and load implicitly options. The skill handles library versioning with git tags and branch-based loading via @Library annotations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-shared-library-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-shared-library-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-manager/)
