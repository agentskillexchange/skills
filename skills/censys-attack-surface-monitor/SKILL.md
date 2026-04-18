---
title: "Censys Attack Surface Monitor"
description: "Monitors internet-facing assets using Censys Search API v2 for host discovery and certificate enumeration. Tracks exposed services, TLS configurations, and new asset appearances with delta alerting via webhook integrations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/censys-attack-surface-monitor/"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
---

# Censys Attack Surface Monitor

The Censys Attack Surface Monitor provides continuous visibility into an organization internet-exposed infrastructure using the Censys Search API v2. It performs automated host discovery queries based on organization identifiers including AS numbers, IP ranges, and domain names resolved through Censys certificate datasets.

The monitor tracks all observed services with protocol-level detail including HTTP response headers, TLS certificate chains, SSH key fingerprints, and banner information. Certificate enumeration discovers assets through CT log analysis and Censys certificate search, identifying shadow IT and forgotten infrastructure that traditional asset inventories miss.

Delta detection compares current scan results against historical baselines to identify new hosts, changed services, expired certificates, and deprecated TLS configurations. Alerts route through configurable webhook integrations to Slack, Microsoft Teams, PagerDuty, or custom HTTP endpoints with severity classification based on exposure type and service criticality. The skill maintains an asset inventory database with tagging for business unit ownership and compliance scope tracking. Regular reports summarize attack surface trends and remediation progress.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/censys-attack-surface-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/censys-attack-surface-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/censys-attack-surface-monitor/)
