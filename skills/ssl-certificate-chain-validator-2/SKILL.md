---
name: "SSL Certificate Chain Validator"
slug: "ssl-certificate-chain-validator-2"
description: "Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status."
verification: "security_reviewed"
source: "https://datatracker.ietf.org/doc/html/rfc8446"
category: "Security & Verification"
framework: "Codex"
---

# SSL Certificate Chain Validator

Performs deep TLS certificate chain validation using OpenSSL and Certificate Transparency logs. Monitors expiration dates via the crt.sh API and checks OCSP responder status.

## Installation

Requirements and caveats from upstream:
- In the following example, "mandatory" is a vector that must contain
- If the server successfully selects parameters and does not require a
- may require rejecting 0-RTT (see Section 4.2.10 ).

Basic usage or getting-started notes:
- 5.5 . Limits on Key Usage ....................................... 84
- of protocols that run on top of TLS.
- following example) is formed (using C notation) by:

- Source: https://datatracker.ietf.org/doc/html/rfc8446

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-chain-validator-2/)
