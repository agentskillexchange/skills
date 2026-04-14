---
title: "SSL/TLS Certificate Validator and Monitor"
description: "Validates SSL/TLS certificates using OpenSSL s_client, checks OCSP stapling status, and monitors expiry dates. Integrates with crt.sh Certificate Transparency logs and SSLLabs API for grading."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# SSL/TLS Certificate Validator and Monitor

This skill provides comprehensive SSL/TLS certificate validation and monitoring for web services. It uses OpenSSL s_client to connect and extract certificate chains, validating each certificate for proper chain of trust, key sizes, and signature algorithms. The skill queries crt.sh Certificate Transparency logs to discover all certificates issued for a domain, identifying unauthorized or misissued certificates. It checks OCSP stapling configuration and responder availability, validates HSTS headers and preload list inclusion, and tests for deprecated protocol versions (SSLv3, TLS 1.0/1.1). Integration with the Qualys SSLLabs API provides industry-standard grading with detailed findings on cipher suite configuration, forward secrecy support, and vulnerability exposure (BEAST, POODLE, Heartbleed). The skill monitors certificate expiry dates and sends alerts at configurable thresholds, checks CAA DNS records for issuance authorization, and verifies DANE/TLSA records when present.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/)
