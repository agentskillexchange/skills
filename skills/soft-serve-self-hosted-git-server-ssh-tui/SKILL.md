---
title: "Soft Serve Self-Hosted Git Server with SSH TUI"
description: "Soft Serve is a self-hostable Git server by Charmbracelet that provides a beautiful terminal UI accessible over SSH. It supports cloning over SSH, HTTP, and Git protocol, Git LFS, access control with SSH keys, and on-demand repository creation."
slug: "soft-serve-self-hosted-git-server-ssh-tui"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/charmbracelet/soft-serve"
tool_ecosystem:
  github_repo: "charmbracelet/soft-serve"
  github_stars: 6756
---

# Soft Serve Self-Hosted Git Server with SSH TUI

Soft Serve is a self-hostable Git server by Charmbracelet that provides a beautiful terminal UI accessible over SSH. It supports cloning over SSH, HTTP, and Git protocol, Git LFS, access control with SSH keys, and on-demand repository creation.

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
clawhub install soft-serve-self-hosted-git-server-ssh-tui
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Soft Serve is an open-source, self-hosted Git server built by the Charmbracelet team, known for their elegant terminal tools. It provides a complete Git hosting solution in a single binary, with a standout feature: a beautiful terminal user interface accessible directly over SSH.
Users can browse repositories, view files with syntax highlighting and line numbers, explore commit history, and navigate directory trees — all through an SSH connection. The command ssh git.charm.sh demonstrates the experience on the project’s public demo server. Repository browsing commands include repo tree, repo blob, and repo log.
Soft Serve supports cloning repositories over SSH, HTTP, and the native Git protocol. It includes Git LFS support with both HTTP and SSH backends, making it suitable for projects with large binary files. Repositories can be created on demand simply by pushing to a new path.
Access control is handled through SSH public keys. Repositories can be public or private, collaborators can be added via their SSH keys, and user access tokens provide API authentication. Anonymous access can be allowed or disallowed per configuration. An initial admin key is set via environment variable on first run.
Installation is available via Homebrew, apt, yum, Nix, winget, Docker, and Go install. Configuration lives in a YAML file within the data directory. Systemd service units are included with the packaged distributions. The single-binary architecture makes deployment straightforward on any server.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/soft-serve-self-hosted-git-server-ssh-tui/)
