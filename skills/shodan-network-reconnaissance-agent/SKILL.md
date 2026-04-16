---
title: "Shodan Network Reconnaissance Agent"
description: "Performs network reconnaissance using the Shodan REST API and Shodan InternetDB. Discovers exposed services, CVE mappings, and generates asset inventories with risk scores for security teams."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
---

# Shodan Network Reconnaissance Agent

The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/)
