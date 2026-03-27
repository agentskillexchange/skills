---
name: "SSL Certificate Auditor"
description: "Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification."
category: "Security & Verification"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/"
tool_ecosystem:
  tool: sendgrid
  github_stars: 3054
  npm_weekly_downloads: 3287627
  github_repo: sendgrid/sendgrid-nodejs
  license: MIT
  maintained: true
---

# SSL Certificate Auditor

Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification.

## Overview

The SSL Certificate Auditor performs comprehensive TLS/SSL security assessments for web services using the sslyze Python library for direct protocol analysis and the Qualys SSL Labs API v3 for industry-standard grading. It validates complete certificate chains from leaf to root CA, checking expiration dates, key sizes, and signature algorithms against current best practices. The skill tests for deprecated protocols (SSLv3, TLS 1.0/1.1) and weak cipher suites using sslyze’s cipher suite enumeration. HSTS header analysis verifies proper max-age values, includeSubDomains directives, and preload eligibility. OCSP stapling status is checked by examining the TLS handshake for stapled responses. Certificate Transparency log verification queries Google’s CT log aggregator API to ensure certificates appear in public logs as required by Chrome’s CT policy. The skill generates remediation reports with specific Nginx/Apache configuration snippets for fixing identified issues. Automated monitoring schedules periodic re-scans with email alerts via SendGrid API when certificates approach expiration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-auditor-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-auditor-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-auditor-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-auditor-agent -a codex
```

### OpenClaw

```bash
clawhub install ssl-certificate-auditor-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/
