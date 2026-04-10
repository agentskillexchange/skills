---
name: Jenkins Build Log Analyzer
description: Parses Jenkins build console logs via the Jenkins Remote Access API to
  extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics
  and the Jenkins Test Results API to correlate failures with specific changes. Outputs
  a triage report ranked by recurrence frequency.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
