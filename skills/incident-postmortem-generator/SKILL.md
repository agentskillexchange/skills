---
name: Incident Postmortem Generator
description: Generates structured incident postmortems by aggregating data from PagerDuty
  incidents API, Slack channel history, and Grafana dashboard snapshots. Produces
  blameless postmortem documents following the Google SRE template format.
verification: security_reviewed
source: https://agentskillexchange.com/skills/incident-postmortem-generator/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---
# Incident Postmortem Generator

Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain.
How It Works
The skill pulls incident timeline data from PagerDuty's REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template.
Key Features

Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events
Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users
Root cause categorization aligned with categories like code change, configuration, dependency, capacity
Action item extraction with owner assignment and priority ranking

Output
Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
