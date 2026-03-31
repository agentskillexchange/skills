---
name: "Prometheus Alert Router"
description: "Routes and escalates Prometheus AlertManager notifications based on severity and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs for multi-channel incident routing."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-router/"
---
# Prometheus Alert Router

Routes and escalates Prometheus AlertManager notifications based on severity and label matchers. Integrates with PagerDuty, Opsgenie, and Slack webhook APIs for multi-channel incident routing.

## Overview

The Prometheus Alert Router skill provides intelligent routing of Prometheus AlertManager webhook payloads to the appropriate incident response channels. It parses alert labels and annotations to determine severity, team ownership, and escalation path. Supports PagerDuty Events API v2 for creating and resolving incidents, Opsgenie Alert API for on-call scheduling integration, and Slack Incoming Webhooks for real-time team notifications. The skill includes configurable routing rules using label matchers (regex and exact match), silence management via the AlertManager API, and deduplication logic to prevent alert storms. Features automatic grouping of related alerts, customizable templates for notification messages, and runbook URL injection. Built-in retry logic handles transient API failures with exponential backoff.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-router -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-router
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-router/)
