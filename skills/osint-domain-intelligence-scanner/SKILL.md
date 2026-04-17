---
title: "OSINT Domain Intelligence Scanner"
description: "The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance toolkit for security researchers and penetration testers. It integrates directly with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities on target infrastructure. SecurityTrails historical DNS data reveals domain ownership changes, past IP associations, and DNS record modifications over time.\nThe skill leverages Amass passive enumeration mode combined with certificate transparency log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP protocol queries provide structured registration data compliant with modern registry standards.\nResults are correlated and deduplicated across sources, producing a unified JSON report with risk scoring based on exposed services, known CVEs from the NVD database, and historical indicator patterns. The scanner supports batch processing of domain lists and can schedule recurring scans with delta reporting to track infrastructure changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/"
framework:
  - "OpenClaw"
---

# OSINT Domain Intelligence Scanner

The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance toolkit for security researchers and penetration testers. It integrates directly with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities on target infrastructure. SecurityTrails historical DNS data reveals domain ownership changes, past IP associations, and DNS record modifications over time.
The skill leverages Amass passive enumeration mode combined with certificate transparency log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP protocol queries provide structured registration data compliant with modern registry standards.
Results are correlated and deduplicated across sources, producing a unified JSON report with risk scoring based on exposed services, known CVEs from the NVD database, and historical indicator patterns. The scanner supports batch processing of domain lists and can schedule recurring scans with delta reporting to track infrastructure changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/osint-domain-intelligence-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/osint-domain-intelligence-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/)
