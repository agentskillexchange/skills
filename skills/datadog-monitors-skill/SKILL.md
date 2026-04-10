---
title: "Datadog Monitors Skill"
description: "Manages Datadog monitors and dashboards via the Datadog API v2. Lists triggered monitors, mutes/unmutes alert groups, and queries metric timeseries. Supports composite monitors and SLO tracking."
slug: "datadog-monitors-skill"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-monitors-skill/"
---

# Datadog Monitors Skill

Manages Datadog monitors and dashboards via the Datadog API v2. Lists triggered monitors, mutes/unmutes alert groups, and queries metric timeseries. Supports composite monitors and SLO tracking.

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
clawhub install datadog-monitors-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Monitors Skill connects Claude to Datadog’s monitoring platform through the official API v2 endpoints. It retrieves monitor states, identifies triggered alerts, and provides context for incident investigation by querying associated metric timeseries data.
Core capabilities include listing monitors filtered by tag, state, or type; muting and unmuting specific monitor groups during maintenance; and querying the timeseries endpoint to pull metric values for the time window around an alert. The skill formats metric data as readable tables or inline sparklines for quick assessment.
Composite monitor support lets the skill decompose complex alert conditions into their constituent sub-monitors, showing which specific checks are failing within a composite rule. SLO (Service Level Objective) tracking queries burn rate and error budget remaining for business-critical services.
Dashboard integration retrieves widget configurations and their underlying queries, enabling Claude to explain what each dashboard panel monitors. The skill handles Datadog API authentication via DD-API-KEY and DD-APPLICATION-KEY headers, supports both US and EU site regions, and implements pagination for accounts with thousands of monitors. Essential for operations teams running production workloads on Datadog.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitors-skill/)
