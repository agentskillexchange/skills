---
name: "SpiderFoot Open Source Intelligence Automation Framework"
description: "SpiderFoot is an open-source OSINT automation tool that queries over 200 data sources to gather intelligence about IP addresses, domain names, email addresses, and other targets. Written in Python, it provides both a web UI and CLI for reconnaissance, threat intelligence, and attack surface mapping."
category: "Research & Scraping"
framework: "Multi-Framework"
verification: listed
source: "https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/"
---

# SpiderFoot Open Source Intelligence Automation Framework

SpiderFoot is an open-source OSINT automation tool that queries over 200 data sources to gather intelligence about IP addresses, domain names, email addresses, and other targets. Written in Python, it provides both a web UI and CLI for reconnaissance, threat intelligence, and attack surface mapping.

## Installation

Install this skill using one of the following methods:

### Any AI Agent (npx)
```bash
npx @anthropic/agentskill add https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/
```

### Claude Code
```bash
npx @anthropic/agentskill add https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/
```

### Cursor
```bash
npx @anthropic/agentskill add https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/
```

### Codex
```bash
npx @anthropic/agentskill add https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/
```

### OpenClaw
```bash
clawhub install https://agentskillexchange.com/skills/spiderfoot-osint-automation-framework/
```

SpiderFoot is a comprehensive open-source intelligence (OSINT) automation framework with over 17,000 GitHub stars and a mature codebase spanning more than a decade of active development. Built in Python 3 under the MIT license, it automates the process of gathering intelligence from public sources about any target — whether an IP address, domain name, hostname, email address, person name, or network subnet.

### Data Source Integration

SpiderFoot integrates with over 200 data sources and modules, including AlienVault OTX, Shodan, VirusTotal, Have I Been Pwned, Hunter.io, SecurityTrails, Censys, BinaryEdge, BuiltWith, Archive.org, Whois registries, DNS resolvers, and dozens more. Each module is independently configurable, so agents can enable only the sources relevant to their investigation scope and API key availability.

### Scan Types and Modes

The tool supports multiple scan types: a broad “all” scan that queries every enabled module, targeted footprint scans for attack surface enumeration, investigation scans for deep-dive intelligence on a specific entity, and passive-only scans that avoid directly touching the target. This flexibility lets agents balance thoroughness against stealth and API quota consumption.

### Web UI and CLI

SpiderFoot ships with a built-in web interface (Flask-based) that provides a dashboard for managing scans, browsing results in a graph or tabular view, correlating data across entities, and exporting findings. For agent integration, the CLI mode and REST API enable headless operation — agents can launch scans, poll for completion, and retrieve structured results programmatically without browser interaction.

### Correlation and Visualization

Results are automatically correlated across modules: a domain scan might discover subdomains, which resolve to IPs, which link to open ports, which reveal technologies, which connect to known vulnerabilities. SpiderFoot builds a knowledge graph of these relationships, which agents can traverse to identify attack paths, data exposure risks, or brand impersonation attempts.

### Use Cases for Agent Workflows

AI agents can leverage SpiderFoot for security reconnaissance (mapping an organization’s external attack surface), threat intelligence (checking indicators of compromise against multiple feeds), due diligence (investigating a company’s digital footprint), and competitive research (understanding a competitor’s technology stack and infrastructure). The structured output format makes it straightforward to feed results into downstream analysis pipelines.

### Deployment

SpiderFoot can be installed via pip, run from source, or deployed as a Docker container. It stores scan data in a local SQLite database and requires no external infrastructure beyond optional API keys for premium data sources.