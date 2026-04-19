---
title: "PagerDuty Incident Orchestrator"
description: "The PagerDuty Incident Orchestrator skill automates incident management workflows through the PagerDuty Events API v2 and REST API v2. It creates and manages incidents with proper severity classification, service assignment, and escalation policy routing. The skill automatically attaches relevant runbooks from a configured knowledge base when incidents match predefined alert patterns, using the PagerDuty Rulesets API for intelligent routing. It manages on-call schedule queries via the Schedules API to identify current responders, triggers incident actions through the Incident Workflows API, and generates post-incident timelines by correlating PagerDuty log entries with deployment events and monitoring alerts. The orchestrator supports incident merging for related alerts, configures response plays for common scenarios, and produces incident review documents with MTTD, MTTA, and MTTR metrics calculated from the Analytics API."
source: "https://github.com/PagerDuty/pdjs"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Orchestrator

The PagerDuty Incident Orchestrator skill automates incident management workflows through the PagerDuty Events API v2 and REST API v2. It creates and manages incidents with proper severity classification, service assignment, and escalation policy routing. The skill automatically attaches relevant runbooks from a configured knowledge base when incidents match predefined alert patterns, using the PagerDuty Rulesets API for intelligent routing. It manages on-call schedule queries via the Schedules API to identify current responders, triggers incident actions through the Incident Workflows API, and generates post-incident timelines by correlating PagerDuty log entries with deployment events and monitoring alerts. The orchestrator supports incident merging for related alerts, configures response plays for common scenarios, and produces incident review documents with MTTD, MTTA, and MTTR metrics calculated from the Analytics API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-orchestrator-2/)
