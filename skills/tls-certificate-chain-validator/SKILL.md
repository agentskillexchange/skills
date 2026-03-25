---
name: "TLS Certificate Chain Validator"
description: "Validates TLS/SSL certificate chains using OpenSSL x509 verification and checks OCSP stapling status. Integrates with Let’s Encrypt ACME protocol for automated certificate renewal alerts and CT log monitoring via crt.sh API."
category: "Security & Verification"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tls-certificate-chain-validator/"
---

# TLS Certificate Chain Validator

Validates TLS/SSL certificate chains using OpenSSL x509 verification and checks OCSP stapling status. Integrates with Let’s Encrypt ACME protocol for automated certificate renewal alerts and CT log monitoring via crt.sh API.

## Overview

The TLS Certificate Chain Validator skill provides comprehensive SSL/TLS certificate inspection and validation for agent workflows. It leverages OpenSSL’s x509 command-line tools to parse certificate chains, verify intermediate CA trust paths, and detect expiring certificates before they cause outages.

Key capabilities include OCSP (Online Certificate Status Protocol) stapling verification to ensure certificates haven’t been revoked, integration with Let’s Encrypt’s ACME protocol for automated renewal monitoring, and Certificate Transparency log queries via the crt.sh API to detect unauthorized certificate issuance for your domains.

The skill supports PEM, DER, and PKCS#12 certificate formats, can validate SAN (Subject Alternative Name) entries against expected domains, and provides cipher suite analysis for TLS 1.2 and 1.3 configurations. It outputs structured JSON reports suitable for compliance auditing and integrates with notification channels for expiry warnings at configurable thresholds (30, 14, 7, and 1 day).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tls-certificate-chain-validator -a codex
```

### OpenClaw

```bash
clawhub install tls-certificate-chain-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/tls-certificate-chain-validator/
