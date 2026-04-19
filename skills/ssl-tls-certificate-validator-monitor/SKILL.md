---
title: "SSL/TLS Certificate Validator and Monitor"
description: "This skill provides comprehensive SSL/TLS certificate validation and monitoring for web services. It uses OpenSSL s_client to connect and extract certificate chains, validating each certificate for proper chain of trust, key sizes, and signature algorithms. The skill queries crt.sh Certificate Transparency logs to discover all certificates issued for a domain, identifying unauthorized or misissued certificates. It checks OCSP stapling configuration and responder availability, validates HSTS headers and preload list inclusion, and tests for deprecated protocol versions (SSLv3, TLS 1.0/1.1). Integration with the Qualys SSLLabs API provides industry-standard grading with detailed findings on cipher suite configuration, forward secrecy support, and vulnerability exposure (BEAST, POODLE, Heartbleed). The skill monitors certificate expiry dates and sends alerts at configurable thresholds, checks CAA DNS records for issuance authorization, and verifies DANE/TLSA records when present."
source: "https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# SSL/TLS Certificate Validator and Monitor

This skill provides comprehensive SSL/TLS certificate validation and monitoring for web services. It uses OpenSSL s_client to connect and extract certificate chains, validating each certificate for proper chain of trust, key sizes, and signature algorithms. The skill queries crt.sh Certificate Transparency logs to discover all certificates issued for a domain, identifying unauthorized or misissued certificates. It checks OCSP stapling configuration and responder availability, validates HSTS headers and preload list inclusion, and tests for deprecated protocol versions (SSLv3, TLS 1.0/1.1). Integration with the Qualys SSLLabs API provides industry-standard grading with detailed findings on cipher suite configuration, forward secrecy support, and vulnerability exposure (BEAST, POODLE, Heartbleed). The skill monitors certificate expiry dates and sends alerts at configurable thresholds, checks CAA DNS records for issuance authorization, and verifies DANE/TLSA records when present.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-tls-certificate-validator-monitor/)
