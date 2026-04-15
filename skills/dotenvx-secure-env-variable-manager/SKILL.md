---
title: "dotenvx Secure Environment Variable Manager and Encryptor"
description: "dotenvx is a secure, cross-platform environment variable manager from the creator of dotenv. It provides encrypted .env files, multi-environment support, and works with any programming language or framework through its CLI runner."
verification: listed
source: "https://github.com/dotenvx/dotenvx"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dotenvx/dotenvx"
  github_stars: 5309
---

# dotenvx Secure Environment Variable Manager and Encryptor

dotenvx is the next-generation evolution of the widely-used dotenv library, created by the same author (Mot). It addresses the critical security gap in traditional .env file management by providing built-in encryption, multi-environment support, and a universal CLI runner that works across every major programming language and framework.

Core Capabilities
The dotenvx CLI provides three primary functions: run, encrypt, and decrypt. The dotenvx run command injects environment variables from .env files into any process, regardless of language — Node.js, Python, Ruby, Go, Rust, Java, PHP, Deno, Bun, and more. The dotenvx encrypt command encrypts your .env files in-place using AES-256-GCM encryption, making them safe to commit to version control. The corresponding dotenvx decrypt reverses the process when needed.

Multi-Environment Workflows
dotenvx natively supports multiple environments through file naming conventions: .env.development, .env.staging, .env.production. The CLI accepts a -f flag to specify which environment file to load, and supports loading multiple files with precedence rules. Each environment can be independently encrypted with its own key pair, stored in the corresponding .env.keys file.

Security Model
Unlike traditional dotenv which stores secrets in plaintext, dotenvx uses public-key cryptography. Each .env file gets a unique keypair. The public key encrypts values inline in the .env file, while the private key (stored in .env.keys or the DOTENV_PRIVATE_KEY environment variable) decrypts at runtime. This means encrypted .env files can safely live in your repository, and only team members or CI systems with the private key can decrypt them.

Installation and Integration
dotenvx is available through npm (npm i -g @dotenvx/dotenvx), Homebrew (brew install dotenvx/brew/dotenvx), curl installer, Docker, GitHub releases, and winget for Windows. It also provides a Node.js SDK via require("@dotenvx/dotenvx").config() for in-code usage, serving as a drop-in replacement for the original dotenv package with encryption support added.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dotenvx-secure-env-variable-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dotenvx-secure-env-variable-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dotenvx-secure-env-variable-manager/)
