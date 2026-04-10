---
title: "chezmoi Cross-Machine Dotfiles Manager"
description: "chezmoi manages dotfiles across multiple machines securely using a Git-backed source-of-truth model with templates, encryption, and cross-platform support. Written in Go with 18k+ GitHub stars, it handles machine-specific configs, secrets, and one-command bootstrap."
slug: "chezmoi-dotfiles-manager"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/twpayne/chezmoi"
tool_ecosystem:
  github_repo: "twpayne/chezmoi"
  github_stars: 18876
listed: true
---

# chezmoi Cross-Machine Dotfiles Manager

chezmoi manages dotfiles across multiple machines securely using a Git-backed source-of-truth model with templates, encryption, and cross-platform support. Written in Go with 18k+ GitHub stars, it handles machine-specific configs, secrets, and one-command bootstrap.

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
clawhub install chezmoi-dotfiles-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

chezmoi is a dotfiles manager that securely manages configuration files across multiple diverse machines. With over 18,000 GitHub stars, an MIT license, and active development, it has become the standard tool for developers who need consistent development environments across laptops, servers, and containers.
The core design principle of chezmoi is a Git-backed source directory that serves as the single source of truth for all managed dotfiles. When you run chezmoi apply, it computes the desired state from the source directory and applies only the necessary changes to the target system. This declarative approach means you always know what state your dotfiles are in, and you can preview changes before applying them with chezmoi diff.
Templates are a first-class feature. chezmoi uses Go text/template syntax to generate machine-specific configurations from a single source file. Variables like hostname, operating system, architecture, and custom data can drive conditional sections, so one template can produce the right config for macOS, Linux, or Windows. This eliminates the need for separate branches or symlink farms.
Security is built in. chezmoi integrates with 1Password, Bitwarden, gopass, KeePassXC, LastPass, pass, Vault, and macOS Keychain for secret management. Encrypted files can be stored directly in the dotfiles repository using age or GPG encryption, so sensitive configuration like API keys and SSH configs can be version-controlled safely.
For AI agents managing development environments, chezmoi provides a programmatic interface to inspect, modify, and apply dotfile changes. An agent can use chezmoi managed to list managed files, chezmoi data to inspect template variables, and chezmoi apply to deploy configuration changes. Bootstrap scripts enable one-command setup of new machines, making it ideal for automated provisioning workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chezmoi-dotfiles-manager/)
