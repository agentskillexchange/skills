---
name: Jenkins Pipeline Lint Agent
description: Validates Jenkinsfile declarative and scripted pipelines using the Jenkins
  Pipeline Linter API endpoint. Checks for deprecated step usage, security anti-patterns,
  and Groovy sandbox violations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/
category:
- CI/CD Integrations
framework:
- Claude Code
---
# Jenkins Pipeline Lint Agent

The Jenkins Pipeline Lint Agent skill submits Jenkinsfile contents to the Jenkins /pipeline-model-converter/validate REST endpoint for server-side syntax validation. Beyond basic linting, it performs static analysis on both declarative and scripted pipeline syntax to detect deprecated step names, insecure credential handling patterns, and Groovy sandbox escape attempts. The skill maintains a knowledge base of Jenkins plugin compatibility matrices, flagging steps that require specific plugin versions. It checks for common anti-patterns like unbounded node blocks, missing timeout wrappers, and improper shared library imports. The agent can process multi-branch pipeline configurations, validating Jenkinsfile variants across branches via the Jenkins Blue Ocean REST API. Results include line-level annotations with fix suggestions, severity ratings, and links to Jenkins documentation for each finding.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-lint-agent/)
