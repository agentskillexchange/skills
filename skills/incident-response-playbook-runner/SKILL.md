---
name: Incident Response Playbook Runner
description: Executes structured incident response playbooks using PagerDuty Events
  API v2 for alerting, Slack Web API for communication, and Jira REST API for ticket
  creation. Automates evidence collection, timeline construction, and post-mortem
  generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/incident-response-playbook-runner/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
- Multi-Framework
---
# Incident Response Playbook Runner

The Incident Response Playbook Runner orchestrates structured incident management workflows by integrating with PagerDuty Events API v2 for alert escalation, Slack Web API for team communication channels, and Jira REST API for incident ticket tracking. It follows customizable playbook templates that define step-by-step response procedures for different incident severity levels.
Evidence collection automates the gathering of relevant logs, metrics snapshots, and configuration states at the time of incident detection. The runner creates dedicated Slack channels with appropriate team members invited, posts structured status updates at configurable intervals, and maintains a real-time timeline of actions taken with timestamps and actor attribution.
Jira tickets are created with standardized fields including severity classification, affected services, customer impact assessment, and linked related incidents. Post-mortem generation compiles the incident timeline, root cause analysis prompts, action items, and metrics impact summary into a formatted document. The skill tracks SLA compliance for response and resolution times, alerting when targets are at risk. Historical incident data enables pattern detection across recurring issues.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-playbook-runner/)
