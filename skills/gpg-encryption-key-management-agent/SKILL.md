---
title: GPG Encryption and Key Management Agent
description: The GPG Encryption and Key Management Agent provides comprehensive PGP/GPG
  cryptographic operations through the GnuPG CLI toolchain and GPGME (GnuPG Made Easy)
  library bindings. It manages the complete key lifecycle from generation through
  revocation. Key management includes generating RSA 4096-bit and Ed25519/Cv25519
  key pairs, managing subkeys for signing, encryption, and authentication purposes,
  and configuring key expiration policies. The agent handles keyserver operations
  including publishing to keys.openpgp.org and SKS pools, key discovery via WKD (Web
  Key Directory), and automated key refresh schedules. The trust model management
  configures trust signatures, owner trust levels, and the Web of Trust calculation.
  It supports both the classic PGP trust model and the TOFU (Trust On First Use) model
  for simplified key verification workflows. Encrypted backup workflows automate symmetric
  and asymmetric encryption of files and directories with configurable cipher algorithms
  (AES-256, Camellia-256). The skill supports detached and inline signatures, cleartext
  signing for email, and S/MIME certificate interoperability. Batch operations handle
  encrypting to multiple recipients with per-recipient key selection and group definitions
  from gpg.conf.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# GPG Encryption and Key Management Agent

The GPG Encryption and Key Management Agent provides comprehensive PGP/GPG cryptographic operations through the GnuPG CLI toolchain and GPGME (GnuPG Made Easy) library bindings. It manages the complete key lifecycle from generation through revocation. Key management includes generating RSA 4096-bit and Ed25519/Cv25519 key pairs, managing subkeys for signing, encryption, and authentication purposes, and configuring key expiration policies. The agent handles keyserver operations including publishing to keys.openpgp.org and SKS pools, key discovery via WKD (Web Key Directory), and automated key refresh schedules. The trust model management configures trust signatures, owner trust levels, and the Web of Trust calculation. It supports both the classic PGP trust model and the TOFU (Trust On First Use) model for simplified key verification workflows. Encrypted backup workflows automate symmetric and asymmetric encryption of files and directories with configurable cipher algorithms (AES-256, Camellia-256). The skill supports detached and inline signatures, cleartext signing for email, and S/MIME certificate interoperability. Batch operations handle encrypting to multiple recipients with per-recipient key selection and group definitions from gpg.conf.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/)
