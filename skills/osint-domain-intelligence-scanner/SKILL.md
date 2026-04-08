---
title: OSINT Domain Intelligence Scanner
description: The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance
  toolkit for security researchers and penetration testers. It integrates directly
  with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities
  on target infrastructure. SecurityTrails historical DNS data reveals domain ownership
  changes, past IP associations, and DNS record modifications over time. The skill
  leverages Amass passive enumeration mode combined with certificate transparency
  log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP
  protocol queries provide structured registration data compliant with modern registry
  standards. Results are correlated and deduplicated across sources, producing a unified
  JSON report with risk scoring based on exposed services, known CVEs from the NVD
  database, and historical indicator patterns. The scanner supports batch processing
  of domain lists and can schedule recurring scans with delta reporting to track infrastructure
  changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard.
verification: security_reviewed
source: https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/
category:
- Research &amp; Scraping
framework:
- OpenClaw
---

# OSINT Domain Intelligence Scanner

The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance toolkit for security researchers and penetration testers. It integrates directly with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities on target infrastructure. SecurityTrails historical DNS data reveals domain ownership changes, past IP associations, and DNS record modifications over time. The skill leverages Amass passive enumeration mode combined with certificate transparency log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP protocol queries provide structured registration data compliant with modern registry standards. Results are correlated and deduplicated across sources, producing a unified JSON report with risk scoring based on exposed services, known CVEs from the NVD database, and historical indicator patterns. The scanner supports batch processing of domain lists and can schedule recurring scans with delta reporting to track infrastructure changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/)
