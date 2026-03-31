---
name: "PagerDuty Incident Runbook Linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/"
---
# PagerDuty Incident Runbook Linker

Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries.

## Overview

The PagerDuty Incident Runbook Linker bridges the gap between alerting and response by automatically associating PagerDuty incidents with relevant operational runbooks. It uses the PagerDuty REST API v2 to monitor incident creation events and extract service context, alert descriptions, and urgency levels. Runbook matching uses Elasticsearch fuzzy queries against a runbook index built from Confluence, Notion, or Markdown documentation repositories. The skill maintains a mapping between PagerDuty services, escalation policies, and runbook collections. When an incident fires, it posts the top-matched runbook links as incident notes and updates the incident custom fields with runbook metadata. Integration with the PagerDuty Events API v2 allows enriching alerts with runbook links before they create incidents. The skill tracks runbook effectiveness by correlating MTTR with runbook usage, identifying which runbooks lead to fastest resolution times and which need updating.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-linker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-linker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-linker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pagerduty-incident-runbook-linker -a codex
```

### OpenClaw

```bash
clawhub install pagerduty-incident-runbook-linker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
