---
title: Censys Attack Surface Monitor
description: The Censys Attack Surface Monitor provides continuous visibility into
  an organization internet-exposed infrastructure using the Censys Search API v2.
  It performs automated host discovery queries based on organization identifiers including
  AS numbers, IP ranges, and domain names resolved through Censys certificate datasets.
  The monitor tracks all observed services with protocol-level detail including HTTP
  response headers, TLS certificate chains, SSH key fingerprints, and banner information.
  Certificate enumeration discovers assets through CT log analysis and Censys certificate
  search, identifying shadow IT and forgotten infrastructure that traditional asset
  inventories miss. Delta detection compares current scan results against historical
  baselines to identify new hosts, changed services, expired certificates, and deprecated
  TLS configurations. Alerts route through configurable webhook integrations to Slack,
  Microsoft Teams, PagerDuty, or custom HTTP endpoints with severity classification
  based on exposure type and service criticality. The skill maintains an asset inventory
  database with tagging for business unit ownership and compliance scope tracking.
  Regular reports summarize attack surface trends and remediation progress.
verification: security_reviewed
source: https://agentskillexchange.com/skills/censys-attack-surface-monitor/
category:
- Research &amp; Scraping
framework:
- Custom Agents
---

# Censys Attack Surface Monitor

The Censys Attack Surface Monitor provides continuous visibility into an organization internet-exposed infrastructure using the Censys Search API v2. It performs automated host discovery queries based on organization identifiers including AS numbers, IP ranges, and domain names resolved through Censys certificate datasets. The monitor tracks all observed services with protocol-level detail including HTTP response headers, TLS certificate chains, SSH key fingerprints, and banner information. Certificate enumeration discovers assets through CT log analysis and Censys certificate search, identifying shadow IT and forgotten infrastructure that traditional asset inventories miss. Delta detection compares current scan results against historical baselines to identify new hosts, changed services, expired certificates, and deprecated TLS configurations. Alerts route through configurable webhook integrations to Slack, Microsoft Teams, PagerDuty, or custom HTTP endpoints with severity classification based on exposure type and service criticality. The skill maintains an asset inventory database with tagging for business unit ownership and compliance scope tracking. Regular reports summarize attack surface trends and remediation progress.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/censys-attack-surface-monitor/)
