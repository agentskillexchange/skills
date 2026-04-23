---
title: "Metabase Dashboard Snapshot & Alerting"
description: "Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments."
verification: security_reviewed
source: "https://www.metabase.com/docs/latest/"
category:
  - "Data Extraction & Transformation"
framework:
  - "OpenClaw"
---

# Metabase Dashboard Snapshot & Alerting

Uses the Metabase REST API to export question results as CSV and render dashboard PNGs on schedule. Compares key metrics against user-defined thresholds and fires alerts to PagerDuty or Slack when anomalies are detected. Supports multi-instance Metabase deployments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/metabase-dashboard-snapshot-alerting-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/metabase-dashboard-snapshot-alerting-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metabase-dashboard-snapshot-alerting-2/)
