---
title: Jenkins Pipeline Monitor
description: The Jenkins Pipeline Monitor agent connects to Jenkins instances via
  the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to
  provide real-time visibility into CI/CD pipeline health. It authenticates using
  API tokens and supports both freestyle and declarative pipeline jobs. The agent
  tracks key metrics including build queue wait times, individual stage durations,
  overall pipeline execution time, and flaky test detection. It parses JUnit XML test
  reports to identify consistently failing tests, newly broken tests, and tests with
  high variance in execution time. For pipeline optimization, the agent analyzes stage-level
  timing data to identify bottlenecks and suggests parallelization opportunities.
  It monitors agent/node resource utilization and flags capacity issues that cause
  queue buildup. Supports Multibranch Pipeline scanning for branch-specific health
  dashboards and integrates with the Jenkins Credentials API for secure secret rotation
  reminders.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-monitor/
category:
- CI/CD Integrations
framework:
- Gemini
---

# Jenkins Pipeline Monitor

The Jenkins Pipeline Monitor agent connects to Jenkins instances via the REST API (/api/json) and Blue Ocean endpoints (/blue/rest/organizations) to provide real-time visibility into CI/CD pipeline health. It authenticates using API tokens and supports both freestyle and declarative pipeline jobs. The agent tracks key metrics including build queue wait times, individual stage durations, overall pipeline execution time, and flaky test detection. It parses JUnit XML test reports to identify consistently failing tests, newly broken tests, and tests with high variance in execution time. For pipeline optimization, the agent analyzes stage-level timing data to identify bottlenecks and suggests parallelization opportunities. It monitors agent/node resource utilization and flags capacity issues that cause queue buildup. Supports Multibranch Pipeline scanning for branch-specific health dashboards and integrates with the Jenkins Credentials API for secure secret rotation reminders.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-monitor/)
