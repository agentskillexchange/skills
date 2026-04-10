---
name: Jenkins Pipeline Linter Pro
description: Validates Jenkinsfile syntax and best practices using the Jenkins Pipeline
  Model Definition API and jenkins-cli.jar linter endpoint. Detects anti-patterns
  like unbounded parallel stages, missing timeout blocks, and credential leaks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-linter-pro/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---
# Jenkins Pipeline Linter Pro

Jenkins Pipeline Linter Pro provides deep static analysis of Jenkinsfile configurations, going far beyond basic syntax validation to enforce CI/CD best practices and security policies. It interfaces with the Jenkins Pipeline Model Definition API to validate declarative pipeline syntax and uses the jenkins-cli.jar linter endpoint for scripted pipeline verification.
The linter detects common anti-patterns including unbounded parallel stages that can exhaust executor capacity, missing timeout blocks that allow hung builds to consume resources indefinitely, and credential usage patterns that risk secret exposure in console logs. It analyzes withCredentials blocks to ensure sensitive values are properly masked.
Shared library references are resolved and validated against the configured library versions, flagging incompatible method signatures or deprecated library functions. The skill checks agent labels against available node configurations to prevent pipeline failures from missing executors.
Advanced features include Groovy sandbox escape detection for scripted pipelines, resource lock analysis to identify potential deadlocks in parallel stages, artifact archival best practices, and stash/unstash optimization recommendations. The linter generates both human-readable reports and machine-parseable JSON output for integration with PR status checks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-linter-pro/)
