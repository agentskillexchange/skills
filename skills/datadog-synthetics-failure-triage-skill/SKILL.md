---
name: Datadog Synthetics Failure Triage Skill
description: Investigates broken checks with the Datadog Synthetics API, Monitors
  API, and Logs Search API to connect failed browser or API tests with the signals
  that explain them. Handy for turning a red synthetic check into an actionable diagnosis
  instead of a vague outage alarm.
category: Runbooks & Diagnostics
framework: Claude Code
verification: security_reviewed
source: https://github.com/DataDog/datadog-api-client-python
tool_ecosystem:
  github_repo: DataDog/datadog-api-client-python
  github_stars: 158
  tool: datadog-api-client-python
---
# Datadog Synthetics Failure Triage Skill
Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-synthetics-failure-triage-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-synthetics-failure-triage-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/)
