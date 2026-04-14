---
title: "SonarQube Rule Enforcement Agent"
description: "Integrates with SonarQube Web API and sonar-scanner CLI to enforce code quality gates across pull requests. Automatically blocks merges when critical code smells, security hotspots, or duplications exceed configurable thresholds."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Rule Enforcement Agent

The SonarQube Rule Enforcement Agent connects directly to the SonarQube Web API to monitor code quality metrics across your entire codebase. It uses the sonar-scanner CLI to run incremental analysis on every pull request, evaluating complexity, duplication, maintainability, reliability, and security ratings against customizable quality gates. When issues are detected, the agent annotates the PR with inline comments pointing to exact file locations and suggests fixes based on SonarQube rule descriptions. It tracks quality trends over time using the measures/search endpoint, generating weekly reports on technical debt evolution. The agent supports multi-language projects with language-specific rule profiles and can automatically create Jira tickets for critical issues that need immediate attention. Configuration is managed through a YAML file that maps SonarQube quality profiles to repository branches and deployment environments.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/)
