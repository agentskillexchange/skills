---
title: "OSINT Domain Intelligence Scanner"
description: "Performs deep OSINT analysis on domains using Shodan API, SecurityTrails DNS history, and WHOIS RDAP lookups. Aggregates subdomain enumeration via Amass and certificate transparency logs from crt.sh for comprehensive attack surface mapping."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# OSINT Domain Intelligence Scanner

The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance toolkit for security researchers and penetration testers. It integrates directly with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities on target infrastructure. SecurityTrails historical DNS data reveals domain ownership changes, past IP associations, and DNS record modifications over time.

The skill leverages Amass passive enumeration mode combined with certificate transparency log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP protocol queries provide structured registration data compliant with modern registry standards.

Results are correlated and deduplicated across sources, producing a unified JSON report with risk scoring based on exposed services, known CVEs from the NVD database, and historical indicator patterns. The scanner supports batch processing of domain lists and can schedule recurring scans with delta reporting to track infrastructure changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/)
