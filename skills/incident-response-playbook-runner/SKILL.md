---
title: "Incident Response Playbook Runner"
description: "Executes structured incident response playbooks using PagerDuty Events API v2 for alerting, Slack Web API for communication, and Jira REST API for ticket creation. Automates evidence collection, timeline construction, and post-mortem generation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-response-playbook-runner/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
  - "Multi-Framework"
---

# Incident Response Playbook Runner

The Incident Response Playbook Runner orchestrates structured incident management workflows by integrating with PagerDuty Events API v2 for alert escalation, Slack Web API for team communication channels, and Jira REST API for incident ticket tracking. It follows customizable playbook templates that define step-by-step response procedures for different incident severity levels.

Evidence collection automates the gathering of relevant logs, metrics snapshots, and configuration states at the time of incident detection. The runner creates dedicated Slack channels with appropriate team members invited, posts structured status updates at configurable intervals, and maintains a real-time timeline of actions taken with timestamps and actor attribution.

Jira tickets are created with standardized fields including severity classification, affected services, customer impact assessment, and linked related incidents. Post-mortem generation compiles the incident timeline, root cause analysis prompts, action items, and metrics impact summary into a formatted document. The skill tracks SLA compliance for response and resolution times, alerting when targets are at risk. Historical incident data enables pattern detection across recurring issues.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/incident-response-playbook-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/incident-response-playbook-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-playbook-runner/)
