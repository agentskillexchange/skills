---
title: "Shodan Network Reconnaissance Agent"
description: "The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring."
source: "https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
---

# Shodan Network Reconnaissance Agent

The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/)
