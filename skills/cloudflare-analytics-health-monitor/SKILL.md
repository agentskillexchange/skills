---
title: "Cloudflare Analytics Health Monitor"
description: "Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached."
verification: security_reviewed
source: "https://developers.cloudflare.com/analytics/"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
---

# Cloudflare Analytics Health Monitor

The Cloudflare Analytics Health Monitor provides continuous surveillance of web application performance and security metrics through the Cloudflare API v4 GraphQL Analytics endpoint. It queries zone-level analytics including total requests, cached versus uncached ratios, bandwidth consumption, and geographic distribution of traffic. The monitor establishes dynamic baselines using rolling statistical analysis, automatically adjusting alert thresholds based on historical traffic patterns rather than static values. WAF event monitoring tracks managed rule triggers, rate limiting activations, and bot score distributions, correlating spikes with specific attack patterns. When configured thresholds are breached, alerts are dispatched through PagerDuty Events API v2 with structured payloads containing relevant metrics, affected zones, and suggested remediation steps. The skill supports multi-zone monitoring for organizations managing multiple domains, with consolidated dashboards showing comparative performance metrics. Edge cache performance tracking identifies URLs with poor cache hit ratios, suggesting Page Rule or Cache Rule optimizations. Integration with Cloudflare Workers analytics provides function-level latency and error rate monitoring for serverless workloads.

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
