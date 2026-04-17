---
title: "Datadog Monitors Skill"
description: "Manages Datadog monitors and dashboards via the Datadog API v2. Lists triggered monitors, mutes/unmutes alert groups, and queries metric timeseries. Supports composite monitors and SLO tracking."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitors Skill

The Datadog Monitors Skill connects Claude to Datadog’s monitoring platform through the official API v2 endpoints. It retrieves monitor states, identifies triggered alerts, and provides context for incident investigation by querying associated metric timeseries data.

Core capabilities include listing monitors filtered by tag, state, or type; muting and unmuting specific monitor groups during maintenance; and querying the timeseries endpoint to pull metric values for the time window around an alert. The skill formats metric data as readable tables or inline sparklines for quick assessment.

Composite monitor support lets the skill decompose complex alert conditions into their constituent sub-monitors, showing which specific checks are failing within a composite rule. SLO (Service Level Objective) tracking queries burn rate and error budget remaining for business-critical services.

Dashboard integration retrieves widget configurations and their underlying queries, enabling Claude to explain what each dashboard panel monitors. The skill handles Datadog API authentication via DD-API-KEY and DD-APPLICATION-KEY headers, supports both US and EU site regions, and implements pagination for accounts with thousands of monitors. Essential for operations teams running production workloads on Datadog.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitors-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-monitors-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitors-skill/)
