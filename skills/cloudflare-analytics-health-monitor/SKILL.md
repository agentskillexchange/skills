---
title: "Cloudflare Analytics Health Monitor"
slug: "cloudflare-analytics-health-monitor"
description: "Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached."
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://developers.cloudflare.com/analytics/"
---

# Cloudflare Analytics Health Monitor

Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/)
