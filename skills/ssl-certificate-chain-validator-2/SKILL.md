---
title: "SSL Certificate Chain Validator"
description: "Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status."
slug: "ssl-certificate-chain-validator-2"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/"
---

# SSL Certificate Chain Validator

Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status.

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
clawhub install ssl-certificate-chain-validator-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

End-to-end SSL/TLS certificate chain validation agent that verifies the complete trust chain from leaf certificate through intermediates to root CA. Uses OpenSSL s_client for handshake analysis and certificate extraction. Queries Certificate Transparency logs via the crt.sh API to detect unauthorized certificate issuance. Checks Online Certificate Status Protocol (OCSP) responders and Certificate Revocation Lists (CRLs) for revocation status. Monitors certificate expiration with configurable warning thresholds at 30, 14, and 7 days. Validates Subject Alternative Names (SANs) against expected domains. Tests cipher suite strength and protocol version support including TLS 1.3 compliance. Generates compliance reports for PCI DSS and SOC 2 certificate requirements. Supports bulk scanning of domain lists with concurrent validation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/)
