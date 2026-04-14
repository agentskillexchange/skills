---
title: "Uptime Kuma Status Sync"
description: "Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-kuma-status-sync/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
---

# Uptime Kuma Status Sync

The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors.

When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage).

For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
