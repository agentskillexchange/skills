---
title: "Prometheus Alert Router"
description: "The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Router

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-router
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-router` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
