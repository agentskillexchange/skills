---
name: SonarQube Rule Enforcement Agent
description: Integrates with SonarQube Web API and sonar-scanner CLI to enforce code
  quality gates across pull requests. Automatically blocks merges when critical code
  smells, security hotspots, or duplications exceed configurable thresholds.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---
# SonarQube Rule Enforcement Agent

The SonarQube Rule Enforcement Agent connects directly to the SonarQube Web API to monitor code quality metrics across your entire codebase. It uses the sonar-scanner CLI to run incremental analysis on every pull request, evaluating complexity, duplication, maintainability, reliability, and security ratings against customizable quality gates. When issues are detected, the agent annotates the PR with inline comments pointing to exact file locations and suggests fixes based on SonarQube rule descriptions. It tracks quality trends over time using the measures/search endpoint, generating weekly reports on technical debt evolution. The agent supports multi-language projects with language-specific rule profiles and can automatically create Jira tickets for critical issues that need immediate attention. Configuration is managed through a YAML file that maps SonarQube quality profiles to repository branches and deployment environments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/)
