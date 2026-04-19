---
title: "TLS Certificate Chain Analyzer"
description: "The TLS Certificate Chain Analyzer skill performs deep inspection of TLS certificate chains for any domain or endpoint. It combines OpenSSL s_client probing with Certificate Transparency log queries via the crt.sh API (https://crt.sh) to build a comprehensive security picture of your PKI infrastructure. The skill validates complete chain construction from leaf to root, checking for missing intermediates, incorrect chain ordering, and cross-signed certificate ambiguity. It flags weak signature algorithms (SHA-1, RSA-1024), detects certificates approaching expiration with configurable thresholds, and verifies OCSP stapling and CRL distribution point accessibility. Certificate Transparency compliance checking queries multiple CT logs (Google Argon, Cloudflare Nimbus, DigiCert Yeti) to verify all certificates are properly logged. It can detect rogue certificates issued for your domains by monitoring CT logs for unexpected issuances. The skill also checks CAA DNS records, HSTS header configuration, and DANE/TLSA record validation. Outputs machine-readable JSON reports compatible with security compliance frameworks including SOC 2 and PCI DSS requirements."
source: "https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
---

# TLS Certificate Chain Analyzer

The TLS Certificate Chain Analyzer skill performs deep inspection of TLS certificate chains for any domain or endpoint. It combines OpenSSL s_client probing with Certificate Transparency log queries via the crt.sh API (https://crt.sh) to build a comprehensive security picture of your PKI infrastructure. The skill validates complete chain construction from leaf to root, checking for missing intermediates, incorrect chain ordering, and cross-signed certificate ambiguity. It flags weak signature algorithms (SHA-1, RSA-1024), detects certificates approaching expiration with configurable thresholds, and verifies OCSP stapling and CRL distribution point accessibility. Certificate Transparency compliance checking queries multiple CT logs (Google Argon, Cloudflare Nimbus, DigiCert Yeti) to verify all certificates are properly logged. It can detect rogue certificates issued for your domains by monitoring CT logs for unexpected issuances. The skill also checks CAA DNS records, HSTS header configuration, and DANE/TLSA record validation. Outputs machine-readable JSON reports compatible with security compliance frameworks including SOC 2 and PCI DSS requirements.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tls-certificate-chain-analyzer/)
