---
title: "Jenkins Pipeline Health Monitor"
description: "Monitors Jenkins pipelines using the Jenkins REST API and Blue Ocean API, detecting flaky tests, build queue bottlenecks, and credential expiration warnings for proactive CI maintenance."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Pipeline Health Monitor

The Jenkins Pipeline Health Monitor agent provides continuous health monitoring for Jenkins CI/CD environments. It connects to Jenkins using the REST API and Blue Ocean REST API to track pipeline performance, detect degradation patterns, and provide proactive maintenance alerts.

The agent monitors build queue depth and wait times via the Jenkins Queue API, alerting when executor starvation or label mismatches cause jobs to queue excessively. It analyzes build history using the Jenkins Build API to identify flaky tests by tracking pass/fail patterns across recent runs, and calculates test reliability scores per test case using JUnit result data.

Credential management is monitored through the Jenkins Credentials API, providing advance warnings before certificates and API tokens expire. The agent tracks pipeline stage durations over time to detect performance regressions, and monitors Jenkins system health including disk space, memory usage, and plugin compatibility via the Jenkins System API. It generates weekly health reports with trending charts and prioritized action items for Jenkins administrators.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-health-monitor/)
