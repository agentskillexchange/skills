---
title: "Incident Postmortem Generator"
description: "Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain. How It Works The skill pulls incident timeline data from PagerDuty&#8217;s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template. Key Features Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users Root cause categorization aligned with categories like code change, configuration, dependency, capacity Action item extraction with owner assignment and priority ranking Output Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service."
source: "https://agentskillexchange.com/skills/incident-postmortem-generator/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Incident Postmortem Generator

Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain. How It Works The skill pulls incident timeline data from PagerDuty&#8217;s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template. Key Features Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users Root cause categorization aligned with categories like code change, configuration, dependency, capacity Action item extraction with owner assignment and priority ranking Output Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
