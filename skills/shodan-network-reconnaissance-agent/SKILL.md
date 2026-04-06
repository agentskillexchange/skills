---
name: Shodan Network Reconnaissance Agent
description: Performs network reconnaissance using the Shodan REST API and Shodan
  InternetDB. Discovers exposed services, CVE mappings, and generates asset inventories
  with risk scores for security teams.
category: "Research &amp; Scraping"
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/"
---
# Shodan Network Reconnaissance Agent

Performs network reconnaissance using the Shodan REST API and Shodan InternetDB. Discovers exposed services, CVE mappings, and generates asset inventories with risk scores for security teams.

The Shodan Network Reconnaissance Agent automates external attack surface discovery by querying the Shodan REST API for exposed hosts, services, and vulnerabilities across IP ranges and domains. It uses the Shodan Search API with Dorking filters to identify specific service types, software versions, and misconfigurations. The agent cross-references discovered services with the Shodan InternetDB for rapid IP enrichment without consuming API query credits. CVE mappings are extracted from Shodan vulnerability data and enriched with CVSS scores from the NVD API. Asset inventories are built with service fingerprints, SSL certificate details, and geolocation data. Risk scores are calculated based on exposed service criticality, known vulnerability severity, and internet exposure level. The tool generates executive-ready reports with heat maps showing geographic distribution of assets and risk concentration. Differential scanning detects new exposures, closed services, and configuration changes between scan cycles for continuous monitoring.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill shodan-network-reconnaissance-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill shodan-network-reconnaissance-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill shodan-network-reconnaissance-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill shodan-network-reconnaissance-agent -a codex
```

### OpenClaw

```bash
clawhub install shodan-network-reconnaissance-agent
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shodan-network-reconnaissance-agent/)
