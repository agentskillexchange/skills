---
title: "SSL Certificate Auditor"
description: "Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification."
slug: "ssl-certificate-auditor-agent"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/"
listed: true
---

# SSL Certificate Auditor

Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ssl-certificate-auditor-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SSL Certificate Auditor performs comprehensive TLS/SSL security assessments for web services using the sslyze Python library for direct protocol analysis and the Qualys SSL Labs API v3 for industry-standard grading. It validates complete certificate chains from leaf to root CA, checking expiration dates, key sizes, and signature algorithms against current best practices. The skill tests for deprecated protocols (SSLv3, TLS 1.0/1.1) and weak cipher suites using sslyze’s cipher suite enumeration. HSTS header analysis verifies proper max-age values, includeSubDomains directives, and preload eligibility. OCSP stapling status is checked by examining the TLS handshake for stapled responses. Certificate Transparency log verification queries Google’s CT log aggregator API to ensure certificates appear in public logs as required by Chrome’s CT policy. The skill generates remediation reports with specific Nginx/Apache configuration snippets for fixing identified issues. Automated monitoring schedules periodic re-scans with email alerts via SendGrid API when certificates approach expiration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/)
