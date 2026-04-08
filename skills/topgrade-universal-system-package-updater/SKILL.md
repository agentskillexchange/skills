---
title: Topgrade Universal System Package Updater
description: What is Topgrade? Topgrade is an open-source command-line utility that
  upgrades everything on your system with a single command. Written in Rust by the
  topgrade-rs community (a continuation of the original project by r-darwish), it
  has over 3,500 GitHub stars, is licensed under GPL-3.0, and provides pre-built binaries
  for Linux, macOS, Windows, and FreeBSD. It is installable via Homebrew, Cargo, AUR,
  Nix, Winget, Scoop, and Chocolatey. How It Works When you run topgrade , it automatically
  detects which tools and package managers are installed on your system, then runs
  the appropriate update commands for each one. There is no manual configuration required
  for detection — if a package manager is present, Topgrade will find it and update
  through it. Supported sources include system package managers (apt, dnf, pacman,
  zypper, apk), language-specific managers (npm, pip, cargo, gem, go, composer, mix),
  application stores (Homebrew, Flatpak, Snap, Winget, Scoop, Chocolatey, MacPorts),
  container tools (Docker, Podman), editor plugins (Vim, Neovim, VS Code extensions),
  shell frameworks (Oh My Zsh, Fisher, antidote), firmware updates (fwupd), and many
  more — over 60 sources in total. Configuration is done through a TOML file ( ~/.config/topgrade/topgrade.toml
  ) where you can disable specific steps, add custom pre/post commands, set execution
  order, and configure behavior per package manager. The --dry-run flag previews what
  would be updated without making changes. The --cleanup flag runs post-update cleanup
  (cache clearing, autoremove) where supported. What It Produces Topgrade outputs
  a step-by-step log showing which package managers were detected, what updates were
  found, and whether each step succeeded or failed. At the end, it displays a summary
  table of all steps with their status. Failed steps can be retried. The tool respects
  sudo prompts and handles password requirements across different package managers.
  Use Cases Topgrade is ideal for developers and system administrators who maintain
  systems with multiple package managers and want to keep everything current without
  remembering individual update commands. It is especially useful for AI agents performing
  system maintenance, health checks, or environment setup tasks. When paired with
  cron or systemd timers, it provides automated system-wide updates with a single
  entry point.
verification: security_reviewed
source: https://github.com/topgrade-rs/topgrade
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: topgrade-rs/topgrade
  github_stars: 3619
---

# Topgrade Universal System Package Updater

What is Topgrade? Topgrade is an open-source command-line utility that upgrades everything on your system with a single command. Written in Rust by the topgrade-rs community (a continuation of the original project by r-darwish), it has over 3,500 GitHub stars, is licensed under GPL-3.0, and provides pre-built binaries for Linux, macOS, Windows, and FreeBSD. It is installable via Homebrew, Cargo, AUR, Nix, Winget, Scoop, and Chocolatey. How It Works When you run topgrade , it automatically detects which tools and package managers are installed on your system, then runs the appropriate update commands for each one. There is no manual configuration required for detection — if a package manager is present, Topgrade will find it and update through it. Supported sources include system package managers (apt, dnf, pacman, zypper, apk), language-specific managers (npm, pip, cargo, gem, go, composer, mix), application stores (Homebrew, Flatpak, Snap, Winget, Scoop, Chocolatey, MacPorts), container tools (Docker, Podman), editor plugins (Vim, Neovim, VS Code extensions), shell frameworks (Oh My Zsh, Fisher, antidote), firmware updates (fwupd), and many more — over 60 sources in total. Configuration is done through a TOML file ( ~/.config/topgrade/topgrade.toml ) where you can disable specific steps, add custom pre/post commands, set execution order, and configure behavior per package manager. The --dry-run flag previews what would be updated without making changes. The --cleanup flag runs post-update cleanup (cache clearing, autoremove) where supported. What It Produces Topgrade outputs a step-by-step log showing which package managers were detected, what updates were found, and whether each step succeeded or failed. At the end, it displays a summary table of all steps with their status. Failed steps can be retried. The tool respects sudo prompts and handles password requirements across different package managers. Use Cases Topgrade is ideal for developers and system administrators who maintain systems with multiple package managers and want to keep everything current without remembering individual update commands. It is especially useful for AI agents performing system maintenance, health checks, or environment setup tasks. When paired with cron or systemd timers, it provides automated system-wide updates with a single entry point.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/topgrade-universal-system-package-updater/)
