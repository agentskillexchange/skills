---
title: "Datadog Synthetics Failure Triage Skill"
description: "Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm."
slug: "datadog-synthetics-failure-triage-skill"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/DataDog/datadog-api-client-python"
tool_ecosystem:
  github_repo: "DataDog/datadog-api-client-python"
  github_stars: 158
---

# Datadog Synthetics Failure Triage Skill

Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm.

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
clawhub install datadog-synthetics-failure-triage-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Datadog Synthetics Failure Triage Skill helps agents move from a failed synthetic result to a grounded explanation of what probably went wrong. It relies on the Datadog Synthetics API for test runs and step details, the Monitors API for alert state and history, and the Logs Search API for the surrounding evidence. That makes it useful for browser journeys, API checks, and uptime monitors that fail intermittently and leave teams guessing whether the root cause is networking, auth, a backend regression, or a third-party dependency.
The workflow can inspect failure locations, compare the latest run against recent history, and correlate the failed step with logs, tags, and affected services. It is also a good fit for organizations that want agents to prepare a concise triage packet before a human jumps in. Instead of handing off only a failing test name, the skill can surface monitor state, timestamps, environment tags, and the most relevant error traces.
Use this skill when synthetic monitoring is already in place but the first investigation step still takes too long and too much manual dashboard hopping.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/)
