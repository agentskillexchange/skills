---
title: "Cloudflare Analytics Health Monitor"
description: "Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached."
verification: security_reviewed
source: "https://developers.cloudflare.com/analytics/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# Cloudflare Analytics Health Monitor

The Cloudflare Analytics Health Monitor provides continuous surveillance of web application performance and security metrics through the Cloudflare API v4 GraphQL Analytics endpoint. It queries zone-level analytics including total requests, cached versus uncached ratios, bandwidth consumption, and geographic distribution of traffic. The monitor establishes dynamic baselines using rolling statistical analysis, automatically adjusting alert thresholds based on historical traffic patterns rather than static values. WAF event monitoring tracks managed rule triggers, rate limiting activations, and bot score distributions, correlating spikes with specific attack patterns. When configured thresholds are breached, alerts are dispatched through PagerDuty Events API v2 with structured payloads containing relevant metrics, affected zones, and suggested remediation steps. The skill supports multi-zone monitoring for organizations managing multiple domains, with consolidated dashboards showing comparative performance metrics. Edge cache performance tracking identifies URLs with poor cache hit ratios, suggesting Page Rule or Cache Rule optimizations. Integration with Cloudflare Workers analytics provides function-level latency and error rate monitoring for serverless workloads.

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
