---
title: "Prometheus Alert Router"
description: "Routes and escalates Prometheus AlertManager notifications based on severity and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs for multi-channel incident routing."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Router

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prometheus-alert-router/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-router
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prometheus-alert-router`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
