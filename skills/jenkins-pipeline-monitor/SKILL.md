---
title: "Jenkins Pipeline Monitor"
description: "The Jenkins Pipeline Monitor agent connects to Jenkins instances via the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to provide real-time visibility into CI/CD pipeline health. It authenticates using API tokens and supports both freestyle and declarative pipeline jobs. The agent tracks key metrics including build queue wait times, individual stage durations, overall pipeline execution time, and flaky test detection. It parses JUnit XML test reports to identify consistently failing tests, newly broken tests, and tests with high variance in execution time. For pipeline optimization, the agent analyzes stage-level timing data to identify bottlenecks and suggests parallelization opportunities. It monitors agent/node resource utilization and flags capacity issues that cause queue buildup. Supports Multibranch Pipeline scanning for branch-specific health dashboards and integrates with the Jenkins Credentials API for secure secret rotation reminders."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Monitor

The Jenkins Pipeline Monitor agent connects to Jenkins instances via the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to provide real-time visibility into CI/CD pipeline health. It authenticates using API tokens and supports both freestyle and declarative pipeline jobs. The agent tracks key metrics including build queue wait times, individual stage durations, overall pipeline execution time, and flaky test detection. It parses JUnit XML test reports to identify consistently failing tests, newly broken tests, and tests with high variance in execution time. For pipeline optimization, the agent analyzes stage-level timing data to identify bottlenecks and suggests parallelization opportunities. It monitors agent/node resource utilization and flags capacity issues that cause queue buildup. Supports Multibranch Pipeline scanning for branch-specific health dashboards and integrates with the Jenkins Credentials API for secure secret rotation reminders.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-monitor/)
