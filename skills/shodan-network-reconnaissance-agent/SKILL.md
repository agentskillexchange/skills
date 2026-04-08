---
title: Shodan Network Reconnaissance Agent
description: The Shodan Network Reconnaissance Agent automates external attack surface
  discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities
  across IP ranges and domains. It uses the Shodan Search API with Dorking filters
  to identify specific service types, software versions, and misconfigurations. The
  agent cross-references discovered services with the Shodan InternetDB for rapid
  IP enrichment without consuming API query credits. CVE mappings are extracted from
  Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset
  inventories are built with service fingerprints, SSL certificate details, and geolocation
  data. Risk scores are calculated based on exposed service criticality, known vulnerability
  severity, and internet exposure level. The tool generates executive-ready reports
  with heat maps showing geographic distribution of assets and risk concentration.
  Differential scanning detects new exposures, closed services, and configuration
  changes between scan cycles for continuous monitoring.
verification: security_reviewed
source: https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# Shodan Network Reconnaissance Agent

The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/)
