---
title: "SSL/TLS Certificate Validator and Monitor"
description: "Validates SSL/TLS certificates using OpenSSL s_client, checks OCSP stapling status, and monitors expiry dates. Integrates with crt.sh Certificate Transparency logs and SSLLabs API for grading."
slug: "ssl-tls-certificate-validator-monitor"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/"
listed: true
---

# SSL/TLS Certificate Validator and Monitor

Validates SSL/TLS certificates using OpenSSL s_client, checks OCSP stapling status, and monitors expiry dates. Integrates with crt.sh Certificate Transparency logs and SSLLabs API for grading.

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
clawhub install ssl-tls-certificate-validator-monitor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides comprehensive SSL/TLS certificate validation and monitoring for web services. It uses OpenSSL s_client to connect and extract certificate chains, validating each certificate for proper chain of trust, key sizes, and signature algorithms. The skill queries crt.sh Certificate Transparency logs to discover all certificates issued for a domain, identifying unauthorized or misissued certificates. It checks OCSP stapling configuration and responder availability, validates HSTS headers and preload list inclusion, and tests for deprecated protocol versions (SSLv3, TLS 1.0/1.1). Integration with the Qualys SSLLabs API provides industry-standard grading with detailed findings on cipher suite configuration, forward secrecy support, and vulnerability exposure (BEAST, POODLE, Heartbleed). The skill monitors certificate expiry dates and sends alerts at configurable thresholds, checks CAA DNS records for issuance authorization, and verifies DANE/TLSA records when present.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/)
