---
title: "Datadog Synthetics Failure Triage Skill"
description: "Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm."
verification: "security_reviewed"
source: "https://github.com/DataDog/datadog-api-client-python"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "DataDog/datadog-api-client-python"
  github_stars: 158
---

# Datadog Synthetics Failure Triage Skill

Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-synthetics-failure-triage-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-synthetics-failure-triage-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/)
