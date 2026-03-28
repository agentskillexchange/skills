---
name: "LazyDocker Terminal UI for Docker Management"
description: "LazyDocker is a terminal UI for Docker and Docker Compose that provides container management, log viewing, resource monitoring, and image inspection through a keyboard-driven interface. Created by Jesse Duffield with 50,000+ GitHub stars."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/jesseduffield/lazydocker"
---

# LazyDocker Terminal UI for Docker Management

LazyDocker is a terminal UI for Docker and Docker Compose that provides container management, log viewing, resource monitoring, and image inspection through a keyboard-driven interface. Created by Jesse Duffield with 50,000+ GitHub stars.

## Overview

LazyDocker is an open-source terminal user interface for managing Docker containers, images, volumes, and networks, available at [github.com/jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) with over 50,000 GitHub stars. Written in Go by Jesse Duffield (who also created lazygit), it replaces the constant switching between docker and docker-compose CLI commands with a single, persistent dashboard view.

The interface is split into panels showing containers, images, volumes, and their associated details. For each container, developers can view live logs with filtering, inspect resource usage (CPU, memory, network I/O), read the full container configuration, exec into the container shell, and perform lifecycle actions like start, stop, restart, remove, and rebuild. All operations are bound to single-key shortcuts with a context-sensitive help panel that shows available actions for the currently selected item.

Docker Compose projects get first-class support. LazyDocker reads docker-compose.yml files and presents services as manageable units, allowing developers to rebuild specific services, view their logs independently, and monitor their resource consumption side by side. Bulk operations like bringing up or tearing down entire stacks are accessible from the services panel.

The tool is customizable through a YAML configuration file at ~/.config/jesseduffield/lazydocker/config.yml where users can define custom command templates, adjust keybindings, configure log settings, and set UI panel layouts. Custom commands can be attached to containers or services, enabling project-specific workflows like running database migrations or triggering test suites from within the interface.

Installation is available via Homebrew, scoop, chocolatey, pacman, Go install, and Docker itself (though running LazyDocker inside Docker has known limitations with log viewing and CPU stats). Binary releases are provided for Linux, macOS, and Windows.

For agent skills that involve Docker-based development environments, deployment management, or container troubleshooting, LazyDocker provides a structured way to inspect container state, monitor resource usage, and execute management operations without constructing complex docker CLI commands. Agents can use it to quickly diagnose container issues, inspect logs, and manage multi-service application stacks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lazydocker-terminal-docker-management
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lazydocker-terminal-docker-management -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lazydocker-terminal-docker-management -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lazydocker-terminal-docker-management -a codex
```

### OpenClaw

```bash
clawhub install lazydocker-terminal-docker-management
```

## Source

- Marketplace: https://agentskillexchange.com/skills/lazydocker-terminal-docker-management/
