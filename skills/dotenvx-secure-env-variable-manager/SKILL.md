---
name: "dotenvx Secure Environment Variable Manager and Encryptor"
description: "dotenvx is a secure, cross-platform environment variable manager from the creator of dotenv. It provides encrypted .env files, multi-environment support, and works with any programming language or framework through its CLI runner."
category: "Security & Verification"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/dotenvx/dotenvx"
tool_ecosystem:
  github_repo: "dotenvx/dotenvx"
  github_stars: 5302
---
# dotenvx Secure Environment Variable Manager and Encryptor

dotenvx is a secure, cross-platform environment variable manager from the creator of dotenv. It provides encrypted .env files, multi-environment support, and works with any programming language or framework through its CLI runner.

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dotenvx-secure-env-variable-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dotenvx-secure-env-variable-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dotenvx-secure-env-variable-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dotenvx-secure-env-variable-manager -a codex
```

### OpenClaw

```bash
clawhub install dotenvx-secure-env-variable-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dotenvx-secure-env-variable-manager/)
