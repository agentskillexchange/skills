---
name: "TLS Certificate Chain Analyzer"
description: "Analyzes TLS certificate chains using OpenSSL s_client and the crt.sh Certificate Transparency API. Detects weak algorithms, expiring intermediates, and CT log compliance issues."
category: "Security & Verification"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/"
---
# TLS Certificate Chain Analyzer

Analyzes TLS certificate chains using OpenSSL s_client and the crt.sh Certificate Transparency API. Detects weak algorithms, expiring intermediates, and CT log compliance issues.

## Overview

The TLS Certificate Chain Analyzer skill performs deep inspection of TLS certificate chains for any domain or endpoint. It combines OpenSSL s_client probing with Certificate Transparency log queries via the crt.sh API (https://crt.sh) to build a comprehensive security picture of your PKI infrastructure.

The skill validates complete chain construction from leaf to root, checking for missing intermediates, incorrect chain ordering, and cross-signed certificate ambiguity. It flags weak signature algorithms (SHA-1, RSA-1024), detects certificates approaching expiration with configurable thresholds, and verifies OCSP stapling and CRL distribution point accessibility.

Certificate Transparency compliance checking queries multiple CT logs (Google Argon, Cloudflare Nimbus, DigiCert Yeti) to verify all certificates are properly logged. It can detect rogue certificates issued for your domains by monitoring CT logs for unexpected issuances. The skill also checks CAA DNS records, HSTS header configuration, and DANE/TLSA record validation. Outputs machine-readable JSON reports compatible with security compliance frameworks including SOC 2 and PCI DSS requirements.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-analyzer -a codex
```

### OpenClaw

```bash
clawhub install tls-certificate-chain-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/)
