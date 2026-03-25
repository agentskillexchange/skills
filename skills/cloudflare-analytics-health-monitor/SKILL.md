---
name: "Cloudflare Analytics Health Monitor"
description: "Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached."
category: "Monitoring & Alerts"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cloudflare"  # from ase_tool_match
  github_stars: 1946  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1035304  # from ase_npm_downloads
  github_repo: "cloudflare/cloudflare-go"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cloudflare Analytics Health Monitor

Monitors Cloudflare zone analytics via the Cloudflare API v4 GraphQL Analytics endpoint, tracking request rates, cache hit ratios, and WAF event spikes. Sends alerts through PagerDuty Events API v2 when thresholds are breached.

## Overview

The Cloudflare Analytics Health Monitor provides continuous surveillance of web application performance and security metrics through the Cloudflare API v4 GraphQL Analytics endpoint. It queries zone-level analytics including total requests, cached versus uncached ratios, bandwidth consumption, and geographic distribution of traffic. The monitor establishes dynamic baselines using rolling statistical analysis, automatically adjusting alert thresholds based on historical traffic patterns rather than static values. WAF event monitoring tracks managed rule triggers, rate limiting activations, and bot score distributions, correlating spikes with specific attack patterns. When configured thresholds are breached, alerts are dispatched through PagerDuty Events API v2 with structured payloads containing relevant metrics, affected zones, and suggested remediation steps. The skill supports multi-zone monitoring for organizations managing multiple domains, with consolidated dashboards showing comparative performance metrics. Edge cache performance tracking identifies URLs with poor cache hit ratios, suggesting Page Rule or Cache Rule optimizations. Integration with Cloudflare Workers analytics provides function-level latency and error rate monitoring for serverless workloads.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudflare-analytics-health-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudflare-analytics-health-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudflare-analytics-health-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudflare-analytics-health-monitor -a codex
```

### OpenClaw

```bash
clawhub install cloudflare-analytics-health-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cloudflare-analytics-health-monitor/
