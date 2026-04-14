---
title: "Cloudflare Analytics Health Monitor"
description: "Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached."
verification: security_reviewed
source: "https://developers.cloudflare.com/analytics/"
category:
  - "Monitoring &amp; Alerts"
---

# Cloudflare Analytics Health Monitor

Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/)
