---
name: "Uptime Kuma Status Sync"
description: "Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly."
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-kuma-status-sync/"
---
# Uptime Kuma Status Sync

Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly.

The Uptime Kuma Status Sync skill bridges self-hosted uptime monitoring with enterprise incident management platforms. It connects to Uptime Kuma via its Socket.IO-based API, subscribing to real-time heartbeat events and monitor status changes across HTTP, TCP, DNS, and Docker monitors.



When monitors transition between UP, DOWN, and PENDING states, the skill synchronizes status information to Atlassian Statuspage.io through its REST API (/v1/pages/{page_id}/incidents), creating and resolving incidents with appropriate component impact levels (none, degraded_performance, partial_outage, major_outage).



For significant outages, the skill triggers incident workflows in Rootly via its GraphQL API, automatically assembling response teams based on affected service ownership defined in a ServiceNow CMDB integration. The skill maintains a local SQLite database tracking historical uptime percentages, mean time to recovery (MTTR), and SLA compliance metrics. Scheduled reports are generated in PDF format using the Puppeteer rendering engine and distributed via SendGrid Email API v3 to stakeholder distribution lists.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill uptime-kuma-status-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill uptime-kuma-status-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill uptime-kuma-status-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill uptime-kuma-status-sync -a codex
```

### OpenClaw

```bash
clawhub install uptime-kuma-status-sync
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
