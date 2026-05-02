---
title: "SSL Certificate Auditor"
description: "Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification."
verification: "security_reviewed"
source: "https://github.com/nabla-c0d3/sslyze"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "nabla-c0d3/sslyze"
  github_stars: 3755
---

# SSL Certificate Auditor

The SSL Certificate Auditor performs comprehensive TLS/SSL security assessments for web services using the sslyze Python library for direct protocol analysis and the Qualys SSL Labs API v3 for industry-standard grading. It validates complete certificate chains from leaf to root CA, checking expiration dates, key sizes, and signature algorithms against current best practices. The skill tests for deprecated protocols (SSLv3, TLS 1.0/1.1) and weak cipher suites using sslyze’s cipher suite enumeration. HSTS header analysis verifies proper max-age values, includeSubDomains directives, and preload eligibility. OCSP stapling status is checked by examining the TLS handshake for stapled responses. Certificate Transparency log verification queries Google’s CT log aggregator API to ensure certificates appear in public logs as required by Chrome’s CT policy. The skill generates remediation reports with specific Nginx/Apache configuration snippets for fixing identified issues. Automated monitoring schedules periodic re-scans with email alerts via SendGrid API when certificates approach expiration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ssl-certificate-auditor-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ssl-certificate-auditor-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/)
