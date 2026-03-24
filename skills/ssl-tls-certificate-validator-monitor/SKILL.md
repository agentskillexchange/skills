---
name: "SSL/TLS Certificate Validator and Monitor"
description: "Validates SSL/TLS certificates using OpenSSL s_client, checks OCSP stapling status, and monitors expiry dates. Integrates with crt.sh Certificate Transparency logs and SSLLabs API for grading."
category: "Security & Verification"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/"
---

# SSL/TLS Certificate Validator and Monitor

Validates SSL/TLS certificates using OpenSSL s_client, checks OCSP stapling status, and monitors expiry dates. Integrates with crt.sh Certificate Transparency logs and SSLLabs API for grading.

## Overview

This skill provides comprehensive SSL/TLS certificate validation and monitoring for web services. It uses OpenSSL s_client to connect and extract certificate chains, validating each certificate for proper chain of trust, key sizes, and signature algorithms. The skill queries crt.sh Certificate Transparency logs to discover all certificates issued for a domain, identifying unauthorized or misissued certificates. It checks OCSP stapling configuration and responder availability, validates HSTS headers and preload list inclusion, and tests for deprecated protocol versions (SSLv3, TLS 1.0/1.1). Integration with the Qualys SSLLabs API provides industry-standard grading with detailed findings on cipher suite configuration, forward secrecy support, and vulnerability exposure (BEAST, POODLE, Heartbleed). The skill monitors certificate expiry dates and sends alerts at configurable thresholds, checks CAA DNS records for issuance authorization, and verifies DANE/TLSA records when present.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ssl-tls-certificate-validator-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ssl-tls-certificate-validator-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ssl-tls-certificate-validator-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ssl-tls-certificate-validator-monitor -a codex
```

### OpenClaw

```bash
clawhub install ssl-tls-certificate-validator-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/
