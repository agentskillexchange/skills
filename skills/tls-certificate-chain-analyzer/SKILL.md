---
title: "TLS Certificate Chain Analyzer"
description: "Analyzes TLS certificate chains using OpenSSL s_client and the crt.sh Certificate Transparency API. Detects weak algorithms, expiring intermediates, and CT log compliance issues."
slug: "tls-certificate-chain-analyzer"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/"
listed: true
---

# TLS Certificate Chain Analyzer

Analyzes TLS certificate chains using OpenSSL s_client and the crt.sh Certificate Transparency API. Detects weak algorithms, expiring intermediates, and CT log compliance issues.

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
clawhub install tls-certificate-chain-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The TLS Certificate Chain Analyzer skill performs deep inspection of TLS certificate chains for any domain or endpoint. It combines OpenSSL s_client probing with Certificate Transparency log queries via the crt.sh API (https://crt.sh) to build a comprehensive security picture of your PKI infrastructure.
The skill validates complete chain construction from leaf to root, checking for missing intermediates, incorrect chain ordering, and cross-signed certificate ambiguity. It flags weak signature algorithms (SHA-1, RSA-1024), detects certificates approaching expiration with configurable thresholds, and verifies OCSP stapling and CRL distribution point accessibility.
Certificate Transparency compliance checking queries multiple CT logs (Google Argon, Cloudflare Nimbus, DigiCert Yeti) to verify all certificates are properly logged. It can detect rogue certificates issued for your domains by monitoring CT logs for unexpected issuances. The skill also checks CAA DNS records, HSTS header configuration, and DANE/TLSA record validation. Outputs machine-readable JSON reports compatible with security compliance frameworks including SOC 2 and PCI DSS requirements.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/)
