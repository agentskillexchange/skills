---
title: Datadog Monitors Skill
description: The Datadog Monitors Skill connects Claude to Datadog’s monitoring platform
  through the official API v2 endpoints. It retrieves monitor states, identifies triggered
  alerts, and provides context for incident investigation by querying associated metric
  timeseries data. Core capabilities include listing monitors filtered by tag, state,
  or type; muting and unmuting specific monitor groups during maintenance; and querying
  the timeseries endpoint to pull metric values for the time window around an alert.
  The skill formats metric data as readable tables or inline sparklines for quick
  assessment. Composite monitor support lets the skill decompose complex alert conditions
  into their constituent sub-monitors, showing which specific checks are failing within
  a composite rule. SLO (Service Level Objective) tracking queries burn rate and error
  budget remaining for business-critical services. Dashboard integration retrieves
  widget configurations and their underlying queries, enabling Claude to explain what
  each dashboard panel monitors. The skill handles Datadog API authentication via
  DD-API-KEY and DD-APPLICATION-KEY headers, supports both US and EU site regions,
  and implements pagination for accounts with thousands of monitors. Essential for
  operations teams running production workloads on Datadog.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-monitors-skill/
category:
- Monitoring &amp; Alerts
framework:
- Codex
---

# Datadog Monitors Skill

The Datadog Monitors Skill connects Claude to Datadog’s monitoring platform through the official API v2 endpoints. It retrieves monitor states, identifies triggered alerts, and provides context for incident investigation by querying associated metric timeseries data. Core capabilities include listing monitors filtered by tag, state, or type; muting and unmuting specific monitor groups during maintenance; and querying the timeseries endpoint to pull metric values for the time window around an alert. The skill formats metric data as readable tables or inline sparklines for quick assessment. Composite monitor support lets the skill decompose complex alert conditions into their constituent sub-monitors, showing which specific checks are failing within a composite rule. SLO (Service Level Objective) tracking queries burn rate and error budget remaining for business-critical services. Dashboard integration retrieves widget configurations and their underlying queries, enabling Claude to explain what each dashboard panel monitors. The skill handles Datadog API authentication via DD-API-KEY and DD-APPLICATION-KEY headers, supports both US and EU site regions, and implements pagination for accounts with thousands of monitors. Essential for operations teams running production workloads on Datadog.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitors-skill/)
