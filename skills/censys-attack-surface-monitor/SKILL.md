---
name: "Censys Attack Surface Monitor"
description: "Monitors internet-facing assets using Censys Search API v2 for host discovery and certificate enumeration. Tracks exposed services, TLS configurations, and new asset appearances with delta alerting via webhook integrations."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/censys-attack-surface-monitor/"
tool_ecosystem:
  tool: pagerduty
  github_stars: 69
  npm_weekly_downloads: 210829
  github_repo: PagerDuty/pdjs
  license: Apache-2.0
  maintained: false
---
# Censys Attack Surface Monitor

Monitors internet-facing assets using Censys Search API v2 for host discovery and certificate enumeration. Tracks exposed services, TLS configurations, and new asset appearances with delta alerting via webhook integrations.

## Overview

The Censys Attack Surface Monitor provides continuous visibility into an organization internet-exposed infrastructure using the Censys Search API v2. It performs automated host discovery queries based on organization identifiers including AS numbers, IP ranges, and domain names resolved through Censys certificate datasets.

The monitor tracks all observed services with protocol-level detail including HTTP response headers, TLS certificate chains, SSH key fingerprints, and banner information. Certificate enumeration discovers assets through CT log analysis and Censys certificate search, identifying shadow IT and forgotten infrastructure that traditional asset inventories miss.

Delta detection compares current scan results against historical baselines to identify new hosts, changed services, expired certificates, and deprecated TLS configurations. Alerts route through configurable webhook integrations to Slack, Microsoft Teams, PagerDuty, or custom HTTP endpoints with severity classification based on exposure type and service criticality. The skill maintains an asset inventory database with tagging for business unit ownership and compliance scope tracking. Regular reports summarize attack surface trends and remediation progress.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill censys-attack-surface-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill censys-attack-surface-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill censys-attack-surface-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill censys-attack-surface-monitor -a codex
```

### OpenClaw

```bash
clawhub install censys-attack-surface-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/censys-attack-surface-monitor/)
