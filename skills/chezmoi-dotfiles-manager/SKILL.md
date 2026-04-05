---
name: "chezmoi Cross-Machine Dotfiles Manager"
description: "chezmoi manages dotfiles across multiple machines securely using a Git-backed source-of-truth model with templates, encryption, and cross-platform support. Written in Go with 18k+ GitHub stars, it handles machine-specific configs, secrets, and one-command bootstrap."
category: "Developer Tools"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/twpayne/chezmoi"
tool_ecosystem:
  tool: chezmoi
  github_repo: twpayne/chezmoi
  github_stars: 18876
---
# chezmoi Cross-Machine Dotfiles Manager

chezmoi manages dotfiles across multiple machines securely using a Git-backed source-of-truth model with templates, encryption, and cross-platform support. Written in Go with 18k+ GitHub stars, it handles machine-specific configs, secrets, and one-command bootstrap.

## Overview

chezmoi is a dotfiles manager that securely manages configuration files across multiple diverse machines. With over 18,000 GitHub stars, an MIT license, and active development, it has become the standard tool for developers who need consistent development environments across laptops, servers, and containers.

The core design principle of chezmoi is a Git-backed source directory that serves as the single source of truth for all managed dotfiles. When you run chezmoi apply, it computes the desired state from the source directory and applies only the necessary changes to the target system. This declarative approach means you always know what state your dotfiles are in, and you can preview changes before applying them with chezmoi diff.

Templates are a first-class feature. chezmoi uses Go text/template syntax to generate machine-specific configurations from a single source file. Variables like hostname, operating system, architecture, and custom data can drive conditional sections, so one template can produce the right config for macOS, Linux, or Windows. This eliminates the need for separate branches or symlink farms.

Security is built in. chezmoi integrates with 1Password, Bitwarden, gopass, KeePassXC, LastPass, pass, Vault, and macOS Keychain for secret management. Encrypted files can be stored directly in the dotfiles repository using age or GPG encryption, so sensitive configuration like API keys and SSH configs can be version-controlled safely.

For AI agents managing development environments, chezmoi provides a programmatic interface to inspect, modify, and apply dotfile changes. An agent can use chezmoi managed to list managed files, chezmoi data to inspect template variables, and chezmoi apply to deploy configuration changes. Bootstrap scripts enable one-command setup of new machines, making it ideal for automated provisioning workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill chezmoi-dotfiles-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill chezmoi-dotfiles-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill chezmoi-dotfiles-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill chezmoi-dotfiles-manager -a codex
```

### OpenClaw

```bash
clawhub install chezmoi-dotfiles-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chezmoi-dotfiles-manager/)
