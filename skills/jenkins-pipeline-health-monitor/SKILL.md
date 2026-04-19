---
title: "Jenkins Pipeline Health Monitor"
description: "The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts. The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data. Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators."
source: "https://github.com/jenkinsci/jenkins"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Health Monitor

The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts. The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data. Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/)
