---
title: "GPG Encryption and Key Management Agent"
description: "Manages GPG key lifecycle and file encryption operations using GnuPG CLI and GPGME library. Handles keyserver synchronization, trust model management, and automated encrypted backup workflows."
slug: "gpg-encryption-key-management-agent"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/"
---

# GPG Encryption and Key Management Agent

Manages GPG key lifecycle and file encryption operations using GnuPG CLI and GPGME library. Handles keyserver synchronization, trust model management, and automated encrypted backup workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install gpg-encryption-key-management-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GPG Encryption and Key Management Agent provides comprehensive PGP/GPG cryptographic operations through the GnuPG CLI toolchain and GPGME (GnuPG Made Easy) library bindings. It manages the complete key lifecycle from generation through revocation.
Key management includes generating RSA 4096-bit and Ed25519/Cv25519 key pairs, managing subkeys for signing, encryption, and authentication purposes, and configuring key expiration policies. The agent handles keyserver operations including publishing to keys.openpgp.org and SKS pools, key discovery via WKD (Web Key Directory), and automated key refresh schedules.
The trust model management configures trust signatures, owner trust levels, and the Web of Trust calculation. It supports both the classic PGP trust model and the TOFU (Trust On First Use) model for simplified key verification workflows.
Encrypted backup workflows automate symmetric and asymmetric encryption of files and directories with configurable cipher algorithms (AES-256, Camellia-256). The skill supports detached and inline signatures, cleartext signing for email, and S/MIME certificate interoperability. Batch operations handle encrypting to multiple recipients with per-recipient key selection and group definitions from gpg.conf.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/)
