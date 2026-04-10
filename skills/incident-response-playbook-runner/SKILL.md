---
title: "Incident Response Playbook Runner"
description: "Executes structured incident response playbooks using PagerDuty Events API v2 for alerting, Slack Web API for communication, and Jira REST API for ticket creation. Automates evidence collection, timeline construction, and post-mortem generation."
slug: "incident-response-playbook-runner"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-response-playbook-runner/"
---

# Incident Response Playbook Runner

Executes structured incident response playbooks using PagerDuty Events API v2 for alerting, Slack Web API for communication, and Jira REST API for ticket creation. Automates evidence collection, timeline construction, and post-mortem generation.

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
clawhub install incident-response-playbook-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Incident Response Playbook Runner orchestrates structured incident management workflows by integrating with PagerDuty Events API v2 for alert escalation, Slack Web API for team communication channels, and Jira REST API for incident ticket tracking. It follows customizable playbook templates that define step-by-step response procedures for different incident severity levels.
Evidence collection automates the gathering of relevant logs, metrics snapshots, and configuration states at the time of incident detection. The runner creates dedicated Slack channels with appropriate team members invited, posts structured status updates at configurable intervals, and maintains a real-time timeline of actions taken with timestamps and actor attribution.
Jira tickets are created with standardized fields including severity classification, affected services, customer impact assessment, and linked related incidents. Post-mortem generation compiles the incident timeline, root cause analysis prompts, action items, and metrics impact summary into a formatted document. The skill tracks SLA compliance for response and resolution times, alerting when targets are at risk. Historical incident data enables pattern detection across recurring issues.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-response-playbook-runner/)
