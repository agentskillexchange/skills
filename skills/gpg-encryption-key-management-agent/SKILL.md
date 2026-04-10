---
name: GPG Encryption and Key Management Agent
description: Manages GPG key lifecycle and file encryption operations using GnuPG
  CLI and GPGME library. Handles keyserver synchronization, trust model management,
  and automated encrypted backup workflows.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/
category:
- Security &amp; Verification
framework:
- OpenClaw
---
# GPG Encryption and Key Management Agent

The GPG Encryption and Key Management Agent provides comprehensive PGP/GPG cryptographic operations through the GnuPG CLI toolchain and GPGME (GnuPG Made Easy) library bindings. It manages the complete key lifecycle from generation through revocation.
Key management includes generating RSA 4096-bit and Ed25519/Cv25519 key pairs, managing subkeys for signing, encryption, and authentication purposes, and configuring key expiration policies. The agent handles keyserver operations including publishing to keys.openpgp.org and SKS pools, key discovery via WKD (Web Key Directory), and automated key refresh schedules.
The trust model management configures trust signatures, owner trust levels, and the Web of Trust calculation. It supports both the classic PGP trust model and the TOFU (Trust On First Use) model for simplified key verification workflows.
Encrypted backup workflows automate symmetric and asymmetric encryption of files and directories with configurable cipher algorithms (AES-256, Camellia-256). The skill supports detached and inline signatures, cleartext signing for email, and S/MIME certificate interoperability. Batch operations handle encrypting to multiple recipients with per-recipient key selection and group definitions from gpg.conf.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/)
