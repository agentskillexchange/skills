---
title: "Datadog Monitor Blueprint Generator"
description: "Creates Datadog monitor definitions using the Datadog API v2 with metric, log, APM trace, and composite monitor types. Generates Terraform datadog_monitor resources with threshold and anomaly detection."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Blueprint Generator

Creates Datadog monitor definitions using the Datadog API v2 with metric, log, APM trace, and composite monitor types. Generates Terraform datadog_monitor resources with threshold and anomaly detection.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitor-blueprint-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-monitor-blueprint-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/)
