---
title: "Datadog Triage Playbook"
description: "Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
---

# Datadog Triage Playbook

Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/datadog-triage-playbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-triage-playbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/datadog-triage-playbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
