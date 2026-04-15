---
title: "Shodan Network Reconnaissance Agent"
description: "Performs network reconnaissance using the Shodan REST API and Shodan InternetDB. Discovers exposed services, CVE mappings, and generates asset inventories with risk scores for security teams."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
---

# Shodan Network Reconnaissance Agent

The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/shodan-network-reconnaissance-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/shodan-network-reconnaissance-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/)
