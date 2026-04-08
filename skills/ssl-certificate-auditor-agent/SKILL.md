---
title: SSL Certificate Auditor
description: The SSL Certificate Auditor performs comprehensive TLS/SSL security assessments
  for web services using the sslyze Python library for direct protocol analysis and
  the Qualys SSL Labs API v3 for industry-standard grading. It validates complete
  certificate chains from leaf to root CA, checking expiration dates, key sizes, and
  signature algorithms against current best practices. The skill tests for deprecated
  protocols (SSLv3, TLS 1.0/1.1) and weak cipher suites using sslyze’s cipher suite
  enumeration. HSTS header analysis verifies proper max-age values, includeSubDomains
  directives, and preload eligibility. OCSP stapling status is checked by examining
  the TLS handshake for stapled responses. Certificate Transparency log verification
  queries Google’s CT log aggregator API to ensure certificates appear in public logs
  as required by Chrome’s CT policy. The skill generates remediation reports with
  specific Nginx/Apache configuration snippets for fixing identified issues. Automated
  monitoring schedules periodic re-scans with email alerts via SendGrid API when certificates
  approach expiration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# SSL Certificate Auditor

The SSL Certificate Auditor performs comprehensive TLS/SSL security assessments for web services using the sslyze Python library for direct protocol analysis and the Qualys SSL Labs API v3 for industry-standard grading. It validates complete certificate chains from leaf to root CA, checking expiration dates, key sizes, and signature algorithms against current best practices. The skill tests for deprecated protocols (SSLv3, TLS 1.0/1.1) and weak cipher suites using sslyze’s cipher suite enumeration. HSTS header analysis verifies proper max-age values, includeSubDomains directives, and preload eligibility. OCSP stapling status is checked by examining the TLS handshake for stapled responses. Certificate Transparency log verification queries Google’s CT log aggregator API to ensure certificates appear in public logs as required by Chrome’s CT policy. The skill generates remediation reports with specific Nginx/Apache configuration snippets for fixing identified issues. Automated monitoring schedules periodic re-scans with email alerts via SendGrid API when certificates approach expiration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/)
