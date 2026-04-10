---
name: "TLS Certificate Chain Validator"
description: "Validates TLS/SSL certificate chains using OpenSSL x509 verification and checks OCSP stapling status. Integrates with Let's Encrypt ACME protocol for automated certificate renewal alerts and CT log monitoring via crt.sh API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tls-certificate-chain-validator/"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# TLS Certificate Chain Validator

The TLS Certificate Chain Validator skill provides comprehensive SSL/TLS certificate inspection and validation for agent workflows. It leverages OpenSSL's x509 command-line tools to parse certificate chains, verify intermediate CA trust paths, and detect expiring certificates before they cause outages.
Key capabilities include OCSP (Online Certificate Status Protocol) stapling verification to ensure certificates haven't been revoked, integration with Let's Encrypt's ACME protocol for automated renewal monitoring, and Certificate Transparency log queries via the crt.sh API to detect unauthorized certificate issuance for your domains.
The skill supports PEM, DER, and PKCS#12 certificate formats, can validate SAN (Subject Alternative Name) entries against expected domains, and provides cipher suite analysis for TLS 1.2 and 1.3 configurations. It outputs structured JSON reports suitable for compliance auditing and integrates with notification channels for expiry warnings at configurable thresholds (30, 14, 7, and 1 day).

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tls-certificate-chain-validator/)
