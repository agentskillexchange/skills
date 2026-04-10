---
title: "Uptime Robot Multi-Check Coordinator"
description: "Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization."
slug: "uptime-robot-multi-check-coordinator"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/"
---

# Uptime Robot Multi-Check Coordinator

Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install uptime-robot-multi-check-coordinator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Uptime Robot Multi-Check Coordinator manages large-scale uptime monitoring configurations through the Uptime Robot API v2. It supports bulk creation and management of HTTP, HTTPS, keyword, ping, and port monitors across service portfolios. Monitor configurations include custom check intervals, timeout values, and HTTP authentication for protected endpoints. Alert contact management enables routing notifications to appropriate teams via email, Slack, PagerDuty, and webhook integrations with configurable escalation delays. The agent handles maintenance window scheduling to suppress alerts during planned downtime periods. Status page synchronization ensures public-facing status pages reflect current monitor states and incident timelines. Bulk operations support importing monitor configurations from CSV or JSON service catalogs. The tool provides uptime analytics by aggregating response time data and availability percentages across monitor groups. Custom alert thresholds enable differentiated monitoring for critical versus non-critical services with appropriate check frequencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/)
