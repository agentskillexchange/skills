---
name: Cloudflare Analytics Health Monitor
description: Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL
  Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes.
  Sends alerts through PagerDuty Events API v2 when thresholds are breached.
category: Monitoring & Alerts
framework: OpenClaw
verification: security_reviewed
source: https://developers.cloudflare.com/analytics/
---
# Cloudflare Analytics Health Monitor
Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudflare-analytics-health-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cloudflare-analytics-health-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/)
