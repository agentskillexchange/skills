---
title: "Incident Postmortem Generator"
description: "Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain.\nHow It Works\nThe skill pulls incident timeline data from PagerDuty’s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template.\nKey Features\n\nAutomated timeline construction from PagerDuty incident logs, Slack messages, and deployment events\nImpact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users\nRoot cause categorization aligned with categories like code change, configuration, dependency, capacity\nAction item extraction with owner assignment and priority ranking\n\nOutput\nGenerates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-postmortem-generator/"
framework:
  - "ChatGPT Agents"
---

# Incident Postmortem Generator

Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain.
How It Works
The skill pulls incident timeline data from PagerDuty’s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template.
Key Features

Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events
Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users
Root cause categorization aligned with categories like code change, configuration, dependency, capacity
Action item extraction with owner assignment and priority ranking

Output
Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/incident-postmortem-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/incident-postmortem-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
