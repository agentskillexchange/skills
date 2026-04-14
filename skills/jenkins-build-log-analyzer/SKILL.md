---
title: "Jenkins Build Log Analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
verification: listed
source: "https://agentskillexchange.com/skills/jenkins-build-log-analyzer/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Jenkins Build Log Analyzer

Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

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
