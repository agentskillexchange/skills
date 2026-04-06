---
name: OSINT Domain Intelligence Scanner
description: Performs deep OSINT analysis on domains using Shodan API, SecurityTrails
  DNS history, and WHOIS RDAP lookups. Aggregates subdomain enumeration via Amass
  and certificate transparency logs from crt.sh for comprehensive attack surface mapping.
category: "Research &amp; Scraping"
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/"
---
# OSINT Domain Intelligence Scanner

Performs deep OSINT analysis on domains using Shodan API, SecurityTrails DNS history, and WHOIS RDAP lookups. Aggregates subdomain enumeration via Amass and certificate transparency logs from crt.sh for comprehensive attack surface mapping.

The OSINT Domain Intelligence Scanner provides a comprehensive reconnaissance toolkit for security researchers and penetration testers. It integrates directly with the Shodan InternetDB API to enumerate open ports, services, and known vulnerabilities on target infrastructure. SecurityTrails historical DNS data reveals domain ownership changes, past IP associations, and DNS record modifications over time.

The skill leverages Amass passive enumeration mode combined with certificate transparency log queries via crt.sh to discover subdomains without active scanning. WHOIS RDAP protocol queries provide structured registration data compliant with modern registry standards.

Results are correlated and deduplicated across sources, producing a unified JSON report with risk scoring based on exposed services, known CVEs from the NVD database, and historical indicator patterns. The scanner supports batch processing of domain lists and can schedule recurring scans with delta reporting to track infrastructure changes over time. Output formats include JSON, CSV, and a rendered HTML dashboard.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill osint-domain-intelligence-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill osint-domain-intelligence-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill osint-domain-intelligence-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill osint-domain-intelligence-scanner -a codex
```

### OpenClaw

```bash
clawhub install osint-domain-intelligence-scanner
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/osint-domain-intelligence-scanner/)
