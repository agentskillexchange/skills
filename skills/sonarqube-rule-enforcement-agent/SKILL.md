---
title: SonarQube Rule Enforcement Agent
description: The SonarQube Rule Enforcement Agent connects directly to the SonarQube
  Web API to monitor code quality metrics across your entire codebase. It uses the
  sonar-scanner CLI to run incremental analysis on every pull request, evaluating
  complexity, duplication, maintainability, reliability, and security ratings against
  customizable quality gates. When issues are detected, the agent annotates the PR
  with inline comments pointing to exact file locations and suggests fixes based on
  SonarQube rule descriptions. It tracks quality trends over time using the measures/search
  endpoint, generating weekly reports on technical debt evolution. The agent supports
  multi-language projects with language-specific rule profiles and can automatically
  create Jira tickets for critical issues that need immediate attention. Configuration
  is managed through a YAML file that maps SonarQube quality profiles to repository
  branches and deployment environments.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/)
