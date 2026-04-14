---
title: "Incident Timeline Builder"
description: "Constructs incident timelines from PagerDuty Events API v2, Datadog Monitors API, and Slack message archives. Correlates alerts with deployment events for root cause analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/incident-timeline-builder/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Incident Timeline Builder

The Incident Timeline Builder skill automates the construction of detailed incident timelines by aggregating data from multiple operational tools. It queries the PagerDuty Events API v2 for alert triggers, acknowledgments, and escalations, the Datadog Monitors API for metric anomalies and threshold breaches, and Slack message archives for human communication context.

The builder correlates these events with deployment timestamps from CI/CD systems (GitHub Deployments API, ArgoCD Application API) to identify change-triggered incidents. It uses temporal proximity analysis and service dependency mapping to establish probable causation chains between deployments and subsequent alerts.

For each incident, the skill generates a structured timeline document with color-coded severity indicators, responsible team assignments, and mean-time-to-detect (MTTD) and mean-time-to-resolve (MTTR) calculations. It identifies communication gaps where alerts fired but no human response occurred within SLA thresholds.

The skill supports retrospective analysis by comparing incident patterns across time windows, identifying recurring failure modes, and suggesting preventive measures. Output formats include Markdown for Confluence/Notion pages, HTML for email distribution, and structured JSON for ingestion by incident management platforms.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-timeline-builder/)
