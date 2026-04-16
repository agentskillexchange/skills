---
title: "SSL Certificate Chain Validator"
description: "Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# SSL Certificate Chain Validator

End-to-end SSL/TLS certificate chain validation agent that verifies the complete trust chain from leaf certificate through intermediates to root CA. Uses OpenSSL s_client for handshake analysis and certificate extraction. Queries Certificate Transparency logs via the crt.sh API to detect unauthorized certificate issuance. Checks Online Certificate Status Protocol (OCSP) responders and Certificate Revocation Lists (CRLs) for revocation status. Monitors certificate expiration with configurable warning thresholds at 30, 14, and 7 days. Validates Subject Alternative Names (SANs) against expected domains. Tests cipher suite strength and protocol version support including TLS 1.3 compliance. Generates compliance reports for PCI DSS and SOC 2 certificate requirements. Supports bulk scanning of domain lists with concurrent validation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/)
