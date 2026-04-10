---
name: "age Modern File Encryption Tool"
description: "Encrypt and decrypt files with age (FiloSottile/age), a simple, modern encryption tool with small explicit keys, post-quantum support, no config options, and UNIX-style composability. A practical replacement for GPG in most workflows."
verification: security_reviewed
source: "https://github.com/FiloSottile/age"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "FiloSottile/age"
  github_stars: 21824
---

# age Modern File Encryption Tool

age is a simple, modern, and secure file encryption tool created by Filippo Valsorda. It provides a clean alternative to GPG for file encryption with a design philosophy centered on simplicity — small explicit keys, no configuration options, and composability with standard UNIX pipes. The project has over 21,000 GitHub stars and is packaged in every major Linux distribution, Homebrew, and Windows package managers.
The tool uses X25519 key pairs by default, with optional passphrase-based encryption. Keys are short, human-readable strings (age1&#8230;) that are easy to copy and share. age supports encrypting to multiple recipients, SSH public keys (both ed25519 and RSA), and plugin-based recipients like YubiKey hardware tokens via age-plugin-yubikey. Recent versions include post-quantum cryptography support, future-proofing encrypted data against quantum computing threats.
age follows the UNIX philosophy of doing one thing well. It reads from stdin and writes to stdout by default, making it composable with tar, curl, and other command-line tools. A typical workflow pipes data through age for encryption: tar czf - ~/data | age -r age1recipient&#8230; > backup.tar.gz.age. Decryption works the same way in reverse. The format specification is published at age-encryption.org/v1, and interoperable implementations exist in Rust (rage), TypeScript (typage), and other languages.
This skill enables agents to manage file encryption workflows using age. Agents can generate key pairs, encrypt files or directories for specific recipients, decrypt data using identity files, manage recipient lists, and integrate age into backup scripts and CI/CD pipelines. The skill outputs encrypted files, key management guidance, and encryption pipeline configurations.
Integration points include SOPS (Mozilla's secrets management tool uses age as a backend), Git-based secret management, automated backup encryption, and secure file transfer workflows. age is distributed as a single static binary under the BSD-3-Clause license, with no runtime dependencies.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/age-modern-file-encryption-tool/)
