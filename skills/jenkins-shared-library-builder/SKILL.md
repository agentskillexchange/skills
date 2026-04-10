---
name: Jenkins Shared Library Builder
description: Scaffolds and tests Jenkins Shared Libraries using the jenkins-pipeline-unit
  framework (JenkinsPipelineUnit). Validates Groovy DSL syntax via CodeNarc static
  analysis and tests pipeline steps with JenkinsRule from jenkins-test-harness.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-shared-library-builder/
category:
- CI/CD Integrations
framework:
- Gemini
---
# Jenkins Shared Library Builder

The Jenkins Shared Library Builder skill automates the creation, testing, and deployment of Jenkins Shared Libraries — reusable Groovy code packages that standardize CI/CD pipeline definitions across an organization. It scaffolds the standard directory structure (vars/, src/, resources/) and generates both declarative and scripted pipeline step implementations.
Unit testing is powered by the jenkins-pipeline-unit framework (JenkinsPipelineUnit), which provides a mock Jenkins environment for testing pipeline steps without a running Jenkins instance. The skill generates comprehensive test suites that validate step behavior with various parameter combinations, mock external tool responses, and verify stage execution ordering.
For integration testing, the skill uses jenkins-test-harness with JenkinsRule to spin up ephemeral Jenkins instances that execute actual pipeline code. This catches issues that unit tests miss, such as plugin compatibility problems and ClassLoader conflicts.
Code quality is enforced through CodeNarc static analysis configured with Jenkins-specific rules: detecting deprecated Jenkins API usage, identifying pipeline steps that block executor threads, and flagging Groovy anti-patterns. The skill also validates that all @NonCPS annotations are correctly applied to prevent serialization issues.
Deployment automation includes Git tag-based versioning, automatic CHANGELOG.md generation from commit messages, and Jenkins configuration-as-code (JCasC) snippets for library registration. The skill supports both GitHub and Bitbucket SCM configurations for library source.
Compatible with Jenkins 2.346+ and Pipeline plugin 2.6+.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-shared-library-builder/)
