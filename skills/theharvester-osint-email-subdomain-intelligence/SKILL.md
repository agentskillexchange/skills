---
title: "theHarvester OSINT Email and Subdomain Intelligence Gatherer"
description: "theHarvester is a well-established open-source intelligence (OSINT) tool written in Python, designed for the reconnaissance phase of penetration testing and red team engagements. It automates the collection of emails, subdomains, hosts, employee names, open ports, and banners from multiple public data sources. How It Works theHarvester queries a wide range of passive and active data sources to enumerate information about a target domain. Supported sources include Bing, Google, LinkedIn, Twitter, Shodan, DNSdumpster, CertSpotter, Rapiddns, and many more. The tool aggregates results from these sources, deduplicates them, and presents a consolidated view of the target&#8217;s external footprint. Key Capabilities Email harvesting: Discovers email addresses associated with a domain by querying search engines and public databases Subdomain enumeration: Finds subdomains through certificate transparency logs, DNS brute-force, and search engine results Host discovery: Identifies IP addresses and hostnames associated with the target Shodan integration: Queries Shodan for open ports, banners, and service information on discovered hosts DNS resolution: Performs forward and reverse DNS lookups on discovered assets Screenshot capture: Can take screenshots of discovered web services for visual reconnaissance Integration Points theHarvester can be run as a CLI tool or integrated into automated reconnaissance pipelines. It outputs results in XML and JSON formats, making it straightforward to feed data into other tools in a security assessment workflow. The tool is included by default in Kali Linux and is installable via pip from PyPI. It supports API key configuration for premium data sources like Shodan, VirusTotal, and SecurityTrails. Use Cases for AI Agents An agent skill wrapping theHarvester enables automated attack surface mapping, domain intelligence gathering, and security audit preparation. Agents can use it to enumerate assets before running vulnerability scanners, build target profiles for social engineering assessments, or monitor an organization&#8217;s external exposure over time."
source: "https://github.com/laramies/theHarvester"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "laramies/theHarvester"
  github_stars: 15942
---

# theHarvester OSINT Email and Subdomain Intelligence Gatherer

theHarvester is a well-established open-source intelligence (OSINT) tool written in Python, designed for the reconnaissance phase of penetration testing and red team engagements. It automates the collection of emails, subdomains, hosts, employee names, open ports, and banners from multiple public data sources. How It Works theHarvester queries a wide range of passive and active data sources to enumerate information about a target domain. Supported sources include Bing, Google, LinkedIn, Twitter, Shodan, DNSdumpster, CertSpotter, Rapiddns, and many more. The tool aggregates results from these sources, deduplicates them, and presents a consolidated view of the target&#8217;s external footprint. Key Capabilities Email harvesting: Discovers email addresses associated with a domain by querying search engines and public databases Subdomain enumeration: Finds subdomains through certificate transparency logs, DNS brute-force, and search engine results Host discovery: Identifies IP addresses and hostnames associated with the target Shodan integration: Queries Shodan for open ports, banners, and service information on discovered hosts DNS resolution: Performs forward and reverse DNS lookups on discovered assets Screenshot capture: Can take screenshots of discovered web services for visual reconnaissance Integration Points theHarvester can be run as a CLI tool or integrated into automated reconnaissance pipelines. It outputs results in XML and JSON formats, making it straightforward to feed data into other tools in a security assessment workflow. The tool is included by default in Kali Linux and is installable via pip from PyPI. It supports API key configuration for premium data sources like Shodan, VirusTotal, and SecurityTrails. Use Cases for AI Agents An agent skill wrapping theHarvester enables automated attack surface mapping, domain intelligence gathering, and security audit preparation. Agents can use it to enumerate assets before running vulnerability scanners, build target profiles for social engineering assessments, or monitor an organization&#8217;s external exposure over time.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/theharvester-osint-email-subdomain-intelligence/)
