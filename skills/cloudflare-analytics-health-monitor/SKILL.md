---
title: Cloudflare Analytics Health Monitor
description: The Cloudflare Analytics Health Monitor provides continuous surveillance
  of web application performance and security metrics through the Cloudflare API v4
  GraphQL Analytics endpoint. It queries zone-level analytics including total requests,
  cached versus uncached ratios, bandwidth consumption, and geographic distribution
  of traffic. The monitor establishes dynamic baselines using rolling statistical
  analysis, automatically adjusting alert thresholds based on historical traffic patterns
  rather than static values. WAF event monitoring tracks managed rule triggers, rate
  limiting activations, and bot score distributions, correlating spikes with specific
  attack patterns. When configured thresholds are breached, alerts are dispatched
  through PagerDuty Events API v2 with structured payloads containing relevant metrics,
  affected zones, and suggested remediation steps. The skill supports multi-zone monitoring
  for organizations managing multiple domains, with consolidated dashboards showing
  comparative performance metrics. Edge cache performance tracking identifies URLs
  with poor cache hit ratios, suggesting Page Rule or Cache Rule optimizations. Integration
  with Cloudflare Workers analytics provides function-level latency and error rate
  monitoring for serverless workloads.
verification: security_reviewed
source: https://developers.cloudflare.com/analytics/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# Cloudflare Analytics Health Monitor

The Cloudflare Analytics Health Monitor provides continuous surveillance of web application performance and security metrics through the Cloudflare API v4 GraphQL Analytics endpoint. It queries zone-level analytics including total requests, cached versus uncached ratios, bandwidth consumption, and geographic distribution of traffic. The monitor establishes dynamic baselines using rolling statistical analysis, automatically adjusting alert thresholds based on historical traffic patterns rather than static values. WAF event monitoring tracks managed rule triggers, rate limiting activations, and bot score distributions, correlating spikes with specific attack patterns. When configured thresholds are breached, alerts are dispatched through PagerDuty Events API v2 with structured payloads containing relevant metrics, affected zones, and suggested remediation steps. The skill supports multi-zone monitoring for organizations managing multiple domains, with consolidated dashboards showing comparative performance metrics. Edge cache performance tracking identifies URLs with poor cache hit ratios, suggesting Page Rule or Cache Rule optimizations. Integration with Cloudflare Workers analytics provides function-level latency and error rate monitoring for serverless workloads.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/)
