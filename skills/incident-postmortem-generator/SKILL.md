---
title: Incident Postmortem Generator
description: Incident Postmortem Generator automates the creation of blameless postmortem
  documents by aggregating data from your incident response toolchain. How It Works
  The skill pulls incident timeline data from PagerDuty’s REST API, conversation history
  from Slack incident channels, and performance graphs from Grafana dashboard snapshots.
  It synthesizes this data into a structured postmortem following the Google SRE template.
  Key Features Automated timeline construction from PagerDuty incident logs, Slack
  messages, and deployment events Impact analysis using Grafana queries to quantify
  error rates, latency percentiles, and affected users Root cause categorization aligned
  with categories like code change, configuration, dependency, capacity Action item
  extraction with owner assignment and priority ranking Output Generates documents
  in Confluence, Google Docs, or Markdown format. Tracks action item completion status.
  Supports recurring incident pattern detection across historical postmortems. Templates
  are customizable per team or service.
verification: security_reviewed
source: https://agentskillexchange.com/skills/incident-postmortem-generator/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Incident Postmortem Generator

Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain. How It Works The skill pulls incident timeline data from PagerDuty’s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template. Key Features Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users Root cause categorization aligned with categories like code change, configuration, dependency, capacity Action item extraction with owner assignment and priority ranking Output Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
