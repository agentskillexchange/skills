---
name: "Datadog Synthetics Failure Triage Skill"
description: "Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm."
verification: security_reviewed
source: "https://github.com/DataDog/datadog-api-client-python"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "DataDog/datadog-api-client-python"
  github_stars: 158
---

# Datadog Synthetics Failure Triage Skill

Datadog Synthetics Failure Triage Skill helps agents move from a failed synthetic result to a grounded explanation of what probably went wrong. It relies on the Datadog Synthetics API for test runs and step details, the Monitors API for alert state and history, and the Logs Search API for the surrounding evidence. That makes it useful for browser journeys, API checks, and uptime monitors that fail intermittently and leave teams guessing whether the root cause is networking, auth, a backend regression, or a third-party dependency.
The workflow can inspect failure locations, compare the latest run against recent history, and correlate the failed step with logs, tags, and affected services. It is also a good fit for organizations that want agents to prepare a concise triage packet before a human jumps in. Instead of handing off only a failing test name, the skill can surface monitor state, timestamps, environment tags, and the most relevant error traces.
Use this skill when synthetic monitoring is already in place but the first investigation step still takes too long and too much manual dashboard hopping.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/)
