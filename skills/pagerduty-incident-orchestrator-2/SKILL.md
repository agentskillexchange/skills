---
title: PagerDuty Incident Orchestrator
description: The PagerDuty Incident Orchestrator skill automates incident management
  workflows through the PagerDuty Events API v2 and REST API v2. It creates and manages
  incidents with proper severity classification, service assignment, and escalation
  policy routing. The skill automatically attaches relevant runbooks from a configured
  knowledge base when incidents match predefined alert patterns, using the PagerDuty
  Rulesets API for intelligent routing. It manages on-call schedule queries via the
  Schedules API to identify current responders, triggers incident actions through
  the Incident Workflows API, and generates post-incident timelines by correlating
  PagerDuty log entries with deployment events and monitoring alerts. The orchestrator
  supports incident merging for related alerts, configures response plays for common
  scenarios, and produces incident review documents with MTTD, MTTA, and MTTR metrics
  calculated from the Analytics API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-orchestrator-2/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# PagerDuty Incident Orchestrator

The PagerDuty Incident Orchestrator skill automates incident management workflows through the PagerDuty Events API v2 and REST API v2. It creates and manages incidents with proper severity classification, service assignment, and escalation policy routing. The skill automatically attaches relevant runbooks from a configured knowledge base when incidents match predefined alert patterns, using the PagerDuty Rulesets API for intelligent routing. It manages on-call schedule queries via the Schedules API to identify current responders, triggers incident actions through the Incident Workflows API, and generates post-incident timelines by correlating PagerDuty log entries with deployment events and monitoring alerts. The orchestrator supports incident merging for related alerts, configures response plays for common scenarios, and produces incident review documents with MTTD, MTTA, and MTTR metrics calculated from the Analytics API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-orchestrator-2/)
