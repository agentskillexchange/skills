---
name: "theHarvester OSINT Email and Subdomain Intelligence Gatherer"
description: "theHarvester is an open-source OSINT tool for gathering emails, subdomains, hosts, employee names, open ports, and banners from public sources. Used during reconnaissance in penetration testing and red team assessments, it queries search engines, PGP key servers, the Shodan API, and other data sources to map an organization’s external threat surface."
category: "Research &amp; Scraping"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/laramies/theHarvester"
tool_ecosystem:
  github_repo: "https://github.com/laramies/theharvester"
  github_stars: 15942
---
# theHarvester OSINT Email and Subdomain Intelligence Gatherer

theHarvester is an open-source OSINT tool for gathering emails, subdomains, hosts, employee names, open ports, and banners from public sources. Used during reconnaissance in penetration testing and red team assessments, it queries search engines, PGP key servers, the Shodan API, and other data sources to map an organization’s external threat surface.

theHarvester is a well-established open-source intelligence (OSINT) tool written in Python, designed for the reconnaissance phase of penetration testing and red team engagements. It automates the collection of emails, subdomains, hosts, employee names, open ports, and banners from multiple public data sources.

How It Works

theHarvester queries a wide range of passive and active data sources to enumerate information about a target domain. Supported sources include Bing, Google, LinkedIn, Twitter, Shodan, DNSdumpster, CertSpotter, Rapiddns, and many more. The tool aggregates results from these sources, deduplicates them, and presents a consolidated view of the target’s external footprint.

Key Capabilities

- Email harvesting: Discovers email addresses associated with a domain by querying search engines and public databases

- Subdomain enumeration: Finds subdomains through certificate transparency logs, DNS brute-force, and search engine results

- Host discovery: Identifies IP addresses and hostnames associated with the target

- Shodan integration: Queries Shodan for open ports, banners, and service information on discovered hosts

- DNS resolution: Performs forward and reverse DNS lookups on discovered assets

- Screenshot capture: Can take screenshots of discovered web services for visual reconnaissance

Integration Points

theHarvester can be run as a CLI tool or integrated into automated reconnaissance pipelines. It outputs results in XML and JSON formats, making it straightforward to feed data into other tools in a security assessment workflow. The tool is included by default in Kali Linux and is installable via pip from PyPI. It supports API key configuration for premium data sources like Shodan, VirusTotal, and SecurityTrails.

Use Cases for AI Agents

An agent skill wrapping theHarvester enables automated attack surface mapping, domain intelligence gathering, and security audit preparation. Agents can use it to enumerate assets before running vulnerability scanners, build target profiles for social engineering assessments, or monitor an organization’s external exposure over time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill theharvester-osint-email-subdomain-intelligence
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill theharvester-osint-email-subdomain-intelligence -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill theharvester-osint-email-subdomain-intelligence -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill theharvester-osint-email-subdomain-intelligence -a codex
```

### OpenClaw

```bash
clawhub install theharvester-osint-email-subdomain-intelligence
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/theharvester-osint-email-subdomain-intelligence/)
