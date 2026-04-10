---
title: "SonarQube Rule Enforcement Agent"
description: "Integrates with SonarQube Web API and sonar-scanner CLI to enforce code quality gates across pull requests. Automatically blocks merges when critical code smells, security hotspots, or duplications exceed configurable thresholds."
slug: "sonarqube-rule-enforcement-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/"
---

# SonarQube Rule Enforcement Agent

Integrates with SonarQube Web API and sonar-scanner CLI to enforce code quality gates across pull requests. Automatically blocks merges when critical code smells, security hotspots, or duplications exceed configurable thresholds.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sonarqube-rule-enforcement-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Rule Enforcement Agent connects directly to the SonarQube Web API to monitor code quality metrics across your entire codebase. It uses the sonar-scanner CLI to run incremental analysis on every pull request, evaluating complexity, duplication, maintainability, reliability, and security ratings against customizable quality gates. When issues are detected, the agent annotates the PR with inline comments pointing to exact file locations and suggests fixes based on SonarQube rule descriptions. It tracks quality trends over time using the measures/search endpoint, generating weekly reports on technical debt evolution. The agent supports multi-language projects with language-specific rule profiles and can automatically create Jira tickets for critical issues that need immediate attention. Configuration is managed through a YAML file that maps SonarQube quality profiles to repository branches and deployment environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/)
