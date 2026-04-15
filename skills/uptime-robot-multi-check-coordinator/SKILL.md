---
title: "Uptime Robot Multi-Check Coordinator"
description: "Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
---

# Uptime Robot Multi-Check Coordinator

The Uptime Robot Multi-Check Coordinator manages large-scale uptime monitoring configurations through the Uptime Robot API v2. It supports bulk creation and management of HTTP, HTTPS, keyword, ping, and port monitors across service portfolios. Monitor configurations include custom check intervals, timeout values, and HTTP authentication for protected endpoints. Alert contact management enables routing notifications to appropriate teams via email, Slack, PagerDuty, and webhook integrations with configurable escalation delays. The agent handles maintenance window scheduling to suppress alerts during planned downtime periods. Status page synchronization ensures public-facing status pages reflect current monitor states and incident timelines. Bulk operations support importing monitor configurations from CSV or JSON service catalogs. The tool provides uptime analytics by aggregating response time data and availability percentages across monitor groups. Custom alert thresholds enable differentiated monitoring for critical versus non-critical services with appropriate check frequencies.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/uptime-robot-multi-check-coordinator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/uptime-robot-multi-check-coordinator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/)
