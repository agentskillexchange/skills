---
title: Jenkins Build Log Analyzer
description: This skill connects to a Jenkins instance using its Remote Access API
  (/api/json endpoints) with username/API-token authentication. It fetches the last
  N build console logs for a given job using the /logText/progressiveText endpoint
  and applies regex pattern matching to extract Java stack traces, Maven Surefire
  test failures, and Docker build errors. The Jenkins Test Report API (/testReport/api/json)
  is queried to identify test methods with high flakiness scores. Results are grouped
  by failure category (environment, test, build tool) and ranked by occurrence count
  across the time window. The skill also integrates with the Jenkins Change Sets API
  to correlate failures with specific committer emails, enabling targeted developer
  notifications. Output is a structured Markdown triage report with suggested next
  steps.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-build-log-analyzer/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Jenkins Build Log Analyzer

This skill connects to a Jenkins instance using its Remote Access API (/api/json endpoints) with username/API-token authentication. It fetches the last N build console logs for a given job using the /logText/progressiveText endpoint and applies regex pattern matching to extract Java stack traces, Maven Surefire test failures, and Docker build errors. The Jenkins Test Report API (/testReport/api/json) is queried to identify test methods with high flakiness scores. Results are grouped by failure category (environment, test, build tool) and ranked by occurrence count across the time window. The skill also integrates with the Jenkins Change Sets API to correlate failures with specific committer emails, enabling targeted developer notifications. Output is a structured Markdown triage report with suggested next steps.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
