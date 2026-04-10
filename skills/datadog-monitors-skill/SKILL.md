---
name: Datadog Monitors Skill
description: Manages Datadog monitors and dashboards via the Datadog API v2. Lists
  triggered monitors, mutes/unmutes alert groups, and queries metric timeseries. Supports
  composite monitors and SLO tracking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-monitors-skill/
category:
- Monitoring &amp; Alerts
framework:
- Codex
---
# Datadog Monitors Skill

The Datadog Monitors Skill connects Claude to Datadog's monitoring platform through the official API v2 endpoints. It retrieves monitor states, identifies triggered alerts, and provides context for incident investigation by querying associated metric timeseries data.
Core capabilities include listing monitors filtered by tag, state, or type; muting and unmuting specific monitor groups during maintenance; and querying the timeseries endpoint to pull metric values for the time window around an alert. The skill formats metric data as readable tables or inline sparklines for quick assessment.
Composite monitor support lets the skill decompose complex alert conditions into their constituent sub-monitors, showing which specific checks are failing within a composite rule. SLO (Service Level Objective) tracking queries burn rate and error budget remaining for business-critical services.
Dashboard integration retrieves widget configurations and their underlying queries, enabling Claude to explain what each dashboard panel monitors. The skill handles Datadog API authentication via DD-API-KEY and DD-APPLICATION-KEY headers, supports both US and EU site regions, and implements pagination for accounts with thousands of monitors. Essential for operations teams running production workloads on Datadog.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitors-skill/)
