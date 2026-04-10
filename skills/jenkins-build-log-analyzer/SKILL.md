---
title: "Jenkins Build Log Analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
slug: "jenkins-build-log-analyzer"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jenkins-build-log-analyzer/"
listed: true
---

# Jenkins Build Log Analyzer

Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

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
clawhub install jenkins-build-log-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill connects to a Jenkins instance using its Remote Access API (/api/json endpoints) with username/API-token authentication. It fetches the last N build console logs for a given job using the /logText/progressiveText endpoint and applies regex pattern matching to extract Java stack traces, Maven Surefire test failures, and Docker build errors. The Jenkins Test Report API (/testReport/api/json) is queried to identify test methods with high flakiness scores. Results are grouped by failure category (environment, test, build tool) and ranked by occurrence count across the time window. The skill also integrates with the Jenkins Change Sets API to correlate failures with specific committer emails, enabling targeted developer notifications. Output is a structured Markdown triage report with suggested next steps.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
