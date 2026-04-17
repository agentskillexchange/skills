---
title: "Jenkins Shared Library Builder"
description: "The Jenkins Shared Library Builder skill automates the creation, testing, and deployment of Jenkins Shared Libraries — reusable Groovy code packages that standardize CI/CD pipeline definitions across an organization. It scaffolds the standard directory structure (vars/, src/, resources/) and generates both declarative and scripted pipeline step implementations.\nUnit testing is powered by the jenkins-pipeline-unit framework (JenkinsPipelineUnit), which provides a mock Jenkins environment for testing pipeline steps without a running Jenkins instance. The skill generates comprehensive test suites that validate step behavior with various parameter combinations, mock external tool responses, and verify stage execution ordering.\nFor integration testing, the skill uses jenkins-test-harness with JenkinsRule to spin up ephemeral Jenkins instances that execute actual pipeline code. This catches issues that unit tests miss, such as plugin compatibility problems and ClassLoader conflicts.\nCode quality is enforced through CodeNarc static analysis configured with Jenkins-specific rules: detecting deprecated Jenkins API usage, identifying pipeline steps that block executor threads, and flagging Groovy anti-patterns. The skill also validates that all @NonCPS annotations are correctly applied to prevent serialization issues.\nDeployment automation includes Git tag-based versioning, automatic CHANGELOG.md generation from commit messages, and Jenkins configuration-as-code (JCasC) snippets for library registration. The skill supports both GitHub and Bitbucket SCM configurations for library source.\nCompatible with Jenkins 2.346+ and Pipeline plugin 2.6+."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Shared Library Builder

The Jenkins Shared Library Builder skill automates the creation, testing, and deployment of Jenkins Shared Libraries — reusable Groovy code packages that standardize CI/CD pipeline definitions across an organization. It scaffolds the standard directory structure (vars/, src/, resources/) and generates both declarative and scripted pipeline step implementations.
Unit testing is powered by the jenkins-pipeline-unit framework (JenkinsPipelineUnit), which provides a mock Jenkins environment for testing pipeline steps without a running Jenkins instance. The skill generates comprehensive test suites that validate step behavior with various parameter combinations, mock external tool responses, and verify stage execution ordering.
For integration testing, the skill uses jenkins-test-harness with JenkinsRule to spin up ephemeral Jenkins instances that execute actual pipeline code. This catches issues that unit tests miss, such as plugin compatibility problems and ClassLoader conflicts.
Code quality is enforced through CodeNarc static analysis configured with Jenkins-specific rules: detecting deprecated Jenkins API usage, identifying pipeline steps that block executor threads, and flagging Groovy anti-patterns. The skill also validates that all @NonCPS annotations are correctly applied to prevent serialization issues.
Deployment automation includes Git tag-based versioning, automatic CHANGELOG.md generation from commit messages, and Jenkins configuration-as-code (JCasC) snippets for library registration. The skill supports both GitHub and Bitbucket SCM configurations for library source.
Compatible with Jenkins 2.346+ and Pipeline plugin 2.6+.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-shared-library-builder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-shared-library-builder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-builder/)
