---
name: "Uptime Robot Multi-Check Coordinator"
description: "Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/"
tool_ecosystem:
  tool: pagerduty
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: PagerDuty/pdjs
  license: Apache-2.0
  maintained: false
---

# Uptime Robot Multi-Check Coordinator

Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization.

## Overview

The Uptime Robot Multi-Check Coordinator manages large-scale uptime monitoring configurations through the Uptime Robot API v2. It supports bulk creation and management of HTTP, HTTPS, keyword, ping, and port monitors across service portfolios. Monitor configurations include custom check intervals, timeout values, and HTTP authentication for protected endpoints. Alert contact management enables routing notifications to appropriate teams via email, Slack, PagerDuty, and webhook integrations with configurable escalation delays. The agent handles maintenance window scheduling to suppress alerts during planned downtime periods. Status page synchronization ensures public-facing status pages reflect current monitor states and incident timelines. Bulk operations support importing monitor configurations from CSV or JSON service catalogs. The tool provides uptime analytics by aggregating response time data and availability percentages across monitor groups. Custom alert thresholds enable differentiated monitoring for critical versus non-critical services with appropriate check frequencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-multi-check-coordinator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-multi-check-coordinator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-multi-check-coordinator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill uptime-robot-multi-check-coordinator -a codex
```

### OpenClaw

```bash
clawhub install uptime-robot-multi-check-coordinator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/
