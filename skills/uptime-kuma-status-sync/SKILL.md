---
title: Uptime Kuma Status Sync
description: The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring
  with enterprise incident management platforms. It connects to Uptime Kuma via its
  Socket.IO-based API, subscribing to real-time heartbeat events and monitor status
  changes across HTTP, TCP, DNS, and Docker monitors. When monitors transition between
  UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian
  Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and
  resolving incidents with appropriate component impact levels (none, degraded_performance,
  partial_outage, major_outage). For significant outages, the skill triggers incident
  workflows in Rootly via its GraphQL API, automatically assembling response teams
  based on affected service ownership defined in a ServiceNow CMDB integration. The
  skill maintains a local SQLite database tracking historical uptime percentages,
  mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are
  generated in PDF format using the Puppeteer rendering engine and distributed via
  SendGrid Email API v3 to stakeholder distribution lists.
verification: security_reviewed
source: https://agentskillexchange.com/skills/uptime-kuma-status-sync/
category:
- Monitoring &amp; Alerts
framework:
- Claude Agents
---

# Uptime Kuma Status Sync

The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors. When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage). For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
