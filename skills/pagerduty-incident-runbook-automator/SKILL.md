---
title: "PagerDuty Incident Runbook Automator"
description: "Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity."
slug: "pagerduty-incident-runbook-automator"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/"
---

# PagerDuty Incident Runbook Automator

Automates incident response runbooks using the PagerDuty Events API v2 and REST API. Manages incident creation, escalation policies, and automated diagnostics triggered by alert severity.

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
clawhub install pagerduty-incident-runbook-automator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PagerDuty Incident Runbook Automator skill integrates with the PagerDuty Events API v2 (events.pagerduty.com/v2/enqueue) and REST API (api.pagerduty.com) to automate incident response workflows. It creates incidents via the Events API with routing_key, event_action (trigger, acknowledge, resolve), and severity levels (critical, error, warning, info).
The skill manages incident lifecycle through REST API endpoints: POST /incidents for manual creation, PUT /incidents/{id} for status updates and reassignment, POST /incidents/{id}/notes for timeline annotations, and GET /incidents/{id}/log_entries for audit trail retrieval. It configures escalation policies using /escalation_policies with multi-level escalation rules and timeout-based progression.
Key capabilities include automated runbook execution triggered by webhook events (incident.trigger, incident.acknowledge), integration with monitoring tools via Events API v2 change events and alert grouping (time-based, intelligent, content-based), service dependency mapping through /service_dependencies for impact analysis, and response play automation with /response_plays for coordinated team mobilization. The automator also supports maintenance window management, on-call schedule rotation queries via /oncalls, and status page integration for external communication during incidents.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-automator/)
