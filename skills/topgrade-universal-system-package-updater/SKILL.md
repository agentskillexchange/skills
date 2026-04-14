---
title: "Topgrade Universal System Package Updater"
description: "Topgrade is a CLI tool written in Rust that detects all package managers and updatable sources on your system and runs the appropriate update commands in one shot. It supports over 60 package managers including apt, brew, npm, pip, cargo, flatpak, snap, firmware updates, and more."
verification: security_reviewed
source: "https://github.com/topgrade-rs/topgrade"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "topgrade-rs/topgrade"
  github_stars: 3619
---

# Topgrade Universal System Package Updater

What is Topgrade?
Topgrade is an open-source command-line utility that upgrades everything on your system with a single command. Written in Rust by the topgrade-rs community (a continuation of the original project by r-darwish), it has over 3,500 GitHub stars, is licensed under GPL-3.0, and provides pre-built binaries for Linux, macOS, Windows, and FreeBSD. It is installable via Homebrew, Cargo, AUR, Nix, Winget, Scoop, and Chocolatey.

How It Works
When you run topgrade, it automatically detects which tools and package managers are installed on your system, then runs the appropriate update commands for each one. There is no manual configuration required for detection — if a package manager is present, Topgrade will find it and update through it. Supported sources include system package managers (apt, dnf, pacman, zypper, apk), language-specific managers (npm, pip, cargo, gem, go, composer, mix), application stores (Homebrew, Flatpak, Snap, Winget, Scoop, Chocolatey, MacPorts), container tools (Docker, Podman), editor plugins (Vim, Neovim, VS Code extensions), shell frameworks (Oh My Zsh, Fisher, antidote), firmware updates (fwupd), and many more — over 60 sources in total.

Configuration is done through a TOML file (~/.config/topgrade/topgrade.toml) where you can disable specific steps, add custom pre/post commands, set execution order, and configure behavior per package manager. The --dry-run flag previews what would be updated without making changes. The --cleanup flag runs post-update cleanup (cache clearing, autoremove) where supported.

What It Produces
Topgrade outputs a step-by-step log showing which package managers were detected, what updates were found, and whether each step succeeded or failed. At the end, it displays a summary table of all steps with their status. Failed steps can be retried. The tool respects sudo prompts and handles password requirements across different package managers.

Use Cases
Topgrade is ideal for developers and system administrators who maintain systems with multiple package managers and want to keep everything current without remembering individual update commands. It is especially useful for AI agents performing system maintenance, health checks, or environment setup tasks. When paired with cron or systemd timers, it provides automated system-wide updates with a single entry point.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/topgrade-universal-system-package-updater/)
