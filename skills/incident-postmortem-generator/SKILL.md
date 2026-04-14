---
title: "Incident Postmortem Generator"
description: "Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-postmortem-generator/"
category:
  - "Runbooks &amp; Diagnostics"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
