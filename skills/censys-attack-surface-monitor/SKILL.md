---
name: "Censys Attack Surface Monitor"
description: "Monitors internet-facing assets using Censys Search API v2 for host discovery and certificate enumeration. Tracks exposed services, TLS configurations, and new asset appearances with delta alerting via webhook integrations."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/censys-attack-surface-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/censys-attack-surface-monitor/
