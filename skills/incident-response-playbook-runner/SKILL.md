---
title: "Incident Response Playbook Runner"
description: "Executes structured incident response playbooks using PagerDuty Events API v2 for alerting, Slack Web API for communication, and Jira REST API for ticket creation. Automates evidence collection, timeline construction, and post-mortem generation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-response-playbook-runner/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
  - "Multi-Framework"
---

# Incident Response Playbook Runner

The Incident Response Playbook Runner orchestrates structured incident management workflows by integrating with PagerDuty Events API v2 for alert escalation, Slack Web API for team communication channels, and Jira REST API for incident ticket tracking. It follows customizable playbook templates that define step-by-step response procedures for different incident severity levels.

Evidence collection automates the gathering of relevant logs, metrics snapshots, and configuration states at the time of incident detection. The runner creates dedicated Slack channels with appropriate team members invited, posts structured status updates at configurable intervals, and maintains a real-time timeline of actions taken with timestamps and actor attribution.

Jira tickets are created with standardized fields including severity classification, affected services, customer impact assessment, and linked related incidents. Post-mortem generation compiles the incident timeline, root cause analysis prompts, action items, and metrics impact summary into a formatted document. The skill tracks SLA compliance for response and resolution times, alerting when targets are at risk. Historical incident data enables pattern detection across recurring issues.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-playbook-runner/)
