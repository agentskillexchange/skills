---
title: "GPG Encryption and Key Management Agent"
description: "Manages GPG key lifecycle and file encryption operations using GnuPG CLI and GPGME library. Handles keyserver synchronization, trust model management, and automated encrypted backup workflows."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
---

# GPG Encryption and Key Management Agent

The GPG Encryption and Key Management Agent provides comprehensive PGP/GPG cryptographic operations through the GnuPG CLI toolchain and GPGME (GnuPG Made Easy) library bindings. It manages the complete key lifecycle from generation through revocation. Key management includes generating RSA 4096-bit and Ed25519/Cv25519 key pairs, managing subkeys for signing, encryption, and authentication purposes, and configuring key expiration policies. The agent handles keyserver operations including publishing to keys.openpgp.org and SKS pools, key discovery via WKD (Web Key Directory), and automated key refresh schedules. The trust model management configures trust signatures, owner trust levels, and the Web of Trust calculation. It supports both the classic PGP trust model and the TOFU (Trust On First Use) model for simplified key verification workflows. Encrypted backup workflows automate symmetric and asymmetric encryption of files and directories with configurable cipher algorithms (AES-256, Camellia-256). The skill supports detached and inline signatures, cleartext signing for email, and S/MIME certificate interoperability. Batch operations handle encrypting to multiple recipients with per-recipient key selection and group definitions from gpg.conf.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gpg-encryption-key-management-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gpg-encryption-key-management-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gpg-encryption-key-management-agent/)
