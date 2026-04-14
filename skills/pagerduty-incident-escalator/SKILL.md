---
title: "PagerDuty Incident Escalator"
description: "Manages PagerDuty incident lifecycle using the PagerDuty REST API v2 /incidents endpoint. Automates escalation policies, merges related incidents, and generates postmortem templates from incident timelines."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Escalator

The PagerDuty Incident Escalator skill automates incident management through the PagerDuty REST API v2. It creates incidents via POST /incidents with proper urgency levels, escalation_policy references, and service associations. The skill monitors incident status transitions using GET /incidents with status filters and date_range parameters. Related incidents are automatically detected through title similarity scoring and merged via PUT /incidents merge to reduce alert fatigue. Escalation policy management uses the /escalation_policies endpoint to dynamically adjust on-call rotations based on incident severity and team availability queried from /oncalls. The skill generates postmortem templates by reconstructing incident timelines from log_entries with full context. Priority classification leverages /priorities to map business impact to PagerDuty priority levels (P1-P5). Response play automation triggers predefined response procedures for critical incidents. Integration with services and integrations endpoints enables automatic incident creation from monitoring tool webhooks. Analytics data from /analytics/metrics/incidents provides mean-time-to-acknowledge and mean-time-to-resolve metrics for continuous improvement tracking.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-escalator/)
