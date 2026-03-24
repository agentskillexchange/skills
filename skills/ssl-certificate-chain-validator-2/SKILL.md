---
name: "SSL Certificate Chain Validator"
description: "Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/"
---

# SSL Certificate Chain Validator

Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status.

## Overview

End-to-end SSL/TLS certificate chain validation agent that verifies the complete trust chain from leaf certificate through intermediates to root CA. Uses OpenSSL s_client for handshake analysis and certificate extraction. Queries Certificate Transparency logs via the crt.sh API to detect unauthorized certificate issuance. Checks Online Certificate Status Protocol (OCSP) responders and Certificate Revocation Lists (CRLs) for revocation status. Monitors certificate expiration with configurable warning thresholds at 30, 14, and 7 days. Validates Subject Alternative Names (SANs) against expected domains. Tests cipher suite strength and protocol version support including TLS 1.3 compliance. Generates compliance reports for PCI DSS and SOC 2 certificate requirements. Supports bulk scanning of domain lists with concurrent validation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-chain-validator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-chain-validator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-chain-validator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-chain-validator-2 -a codex
```

### OpenClaw

```bash
clawhub install ssl-certificate-chain-validator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/
