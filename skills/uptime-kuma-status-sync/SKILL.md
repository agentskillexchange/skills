---
title: "Uptime Kuma Status Sync"
description: "Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-kuma-status-sync/"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Agents"
---

# Uptime Kuma Status Sync

The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors.

When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage).

For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/uptime-kuma-status-sync
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/uptime-kuma-status-sync` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
