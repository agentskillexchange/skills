---
title: "Jenkins Build Log Analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
verification: security_reviewed
source: "https://github.com/jenkinsci/jenkins"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "jenkinsci/jenkins"
  github_stars: 25189
---

# Jenkins Build Log Analyzer

This skill connects to a Jenkins instance using its Remote Access API (/api/json endpoints) with username/API-token authentication. It fetches the last N build console logs for a given job using the /logText/progressiveText endpoint and applies regex pattern matching to extract Java stack traces, Maven Surefire test failures, and Docker build errors. The Jenkins Test Report API (/testReport/api/json) is queried to identify test methods with high flakiness scores. Results are grouped by failure category (environment, test, build tool) and ranked by occurrence count across the time window. The skill also integrates with the Jenkins Change Sets API to correlate failures with specific committer emails, enabling targeted developer notifications. Output is a structured Markdown triage report with suggested next steps.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
