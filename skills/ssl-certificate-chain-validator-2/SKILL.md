---
title: SSL Certificate Chain Validator
description: End-to-end SSL/TLS certificate chain validation agent that verifies the
  complete trust chain from leaf certificate through intermediates to root CA. Uses
  OpenSSL s_client for handshake analysis and certificate extraction. Queries Certificate
  Transparency logs via the crt.sh API to detect unauthorized certificate issuance.
  Checks Online Certificate Status Protocol (OCSP) responders and Certificate Revocation
  Lists (CRLs) for revocation status. Monitors certificate expiration with configurable
  warning thresholds at 30, 14, and 7 days. Validates Subject Alternative Names (SANs)
  against expected domains. Tests cipher suite strength and protocol version support
  including TLS 1.3 compliance. Generates compliance reports for PCI DSS and SOC 2
  certificate requirements. Supports bulk scanning of domain lists with concurrent
  validation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/
category:
- Security &amp; Verification
framework:
- Codex
---

# SSL Certificate Chain Validator

End-to-end SSL/TLS certificate chain validation agent that verifies the complete trust chain from leaf certificate through intermediates to root CA. Uses OpenSSL s_client for handshake analysis and certificate extraction. Queries Certificate Transparency logs via the crt.sh API to detect unauthorized certificate issuance. Checks Online Certificate Status Protocol (OCSP) responders and Certificate Revocation Lists (CRLs) for revocation status. Monitors certificate expiration with configurable warning thresholds at 30, 14, and 7 days. Validates Subject Alternative Names (SANs) against expected domains. Tests cipher suite strength and protocol version support including TLS 1.3 compliance. Generates compliance reports for PCI DSS and SOC 2 certificate requirements. Supports bulk scanning of domain lists with concurrent validation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/)
