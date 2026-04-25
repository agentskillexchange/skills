---
title: "Incident Timeline Builder"
description: "Constructs incident timelines from PagerDuty Events API v2, Datadog Monitors API, and Slack message archives. Correlates alerts with deployment events for root cause analysis."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/incident-timeline-builder/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
---

# Incident Timeline Builder

The Incident Timeline Builder skill automates the construction of detailed incident timelines by aggregating data from multiple operational tools. It queries the PagerDuty Events API v2 for alert triggers, acknowledgments, and escalations, the Datadog Monitors API for metric anomalies and threshold breaches, and Slack message archives for human communication context. The builder correlates these events with deployment timestamps from CI/CD systems (GitHub Deployments API, ArgoCD Application API) to identify change-triggered incidents. It uses temporal proximity analysis and service dependency mapping to establish probable causation chains between deployments and subsequent alerts. For each incident, the skill generates a structured timeline document with color-coded severity indicators, responsible team assignments, and mean-time-to-detect (MTTD) and mean-time-to-resolve (MTTR) calculations. It identifies communication gaps where alerts fired but no human response occurred within SLA thresholds. The skill supports retrospective analysis by comparing incident patterns across time windows, identifying recurring failure modes, and suggesting preventive measures. Output formats include Markdown for Confluence/Notion pages, HTML for email distribution, and structured JSON for ingestion by incident management platforms.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/incident-timeline-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/incident-timeline-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/incident-timeline-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-timeline-builder/)
