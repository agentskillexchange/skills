---
title: "PagerDuty Incident Escalator"
description: "Manages PagerDuty incident lifecycle using the PagerDuty REST API v2 /incidents endpoint. Automates escalation policies, merges related incidents, and generates postmortem templates from incident timelines."
slug: "pagerduty-incident-escalator"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pagerduty-incident-escalator/"
---

# PagerDuty Incident Escalator

Manages PagerDuty incident lifecycle using the PagerDuty REST API v2 /incidents endpoint. Automates escalation policies, merges related incidents, and generates postmortem templates from incident timelines.

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
clawhub install pagerduty-incident-escalator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PagerDuty Incident Escalator skill automates incident management through the PagerDuty REST API v2. It creates incidents via POST /incidents with proper urgency levels, escalation_policy references, and service associations. The skill monitors incident status transitions using GET /incidents with status filters and date_range parameters. Related incidents are automatically detected through title similarity scoring and merged via PUT /incidents merge to reduce alert fatigue. Escalation policy management uses the /escalation_policies endpoint to dynamically adjust on-call rotations based on incident severity and team availability queried from /oncalls. The skill generates postmortem templates by reconstructing incident timelines from log_entries with full context. Priority classification leverages /priorities to map business impact to PagerDuty priority levels (P1-P5). Response play automation triggers predefined response procedures for critical incidents. Integration with services and integrations endpoints enables automatic incident creation from monitoring tool webhooks. Analytics data from /analytics/metrics/incidents provides mean-time-to-acknowledge and mean-time-to-resolve metrics for continuous improvement tracking.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-escalator/)
