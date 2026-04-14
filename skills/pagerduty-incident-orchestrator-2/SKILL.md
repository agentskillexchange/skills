---
title: "PagerDuty Incident Orchestrator"
description: "Manages PagerDuty incident lifecycle using the PagerDuty Events API v2 and REST API. Automates escalation policies, runbook attachment, and post-incident timeline generation."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-orchestrator-2/)
