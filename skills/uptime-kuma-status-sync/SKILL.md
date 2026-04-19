---
title: "Uptime Kuma Status Sync"
description: "The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors. When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage). For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists."
source: "https://agentskillexchange.com/skills/uptime-kuma-status-sync/"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
---

# Uptime Kuma Status Sync

The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors. When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage). For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
