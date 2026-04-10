---
title: "Dockge Self-Hosted Docker Compose Stack Manager"
description: "Dockge is a self-hosted Docker Compose stack manager with a reactive web UI for managing compose.yaml files. Created by Louis Lam (author of Uptime Kuma), it provides an interactive editor, web terminal, and multi-agent support for managing Docker stacks across hosts."
slug: "dockge-docker-compose-stack-manager"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/louislam/dockge"
tool_ecosystem:
  github_repo: "louislam/dockge"
  github_stars: 22685
listed: true
---

# Dockge Self-Hosted Docker Compose Stack Manager

Dockge is a self-hosted Docker Compose stack manager with a reactive web UI for managing compose.yaml files. Created by Louis Lam (author of Uptime Kuma), it provides an interactive editor, web terminal, and multi-agent support for managing Docker stacks across hosts.

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
clawhub install dockge-docker-compose-stack-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Dockge is a fancy, easy-to-use, and reactive self-hosted Docker Compose stack manager created by Louis Lam, the developer behind Uptime Kuma. It provides a modern web interface for managing docker compose.yaml files without requiring deep Docker or nginx knowledge.
Core Capabilities
Dockge focuses on docker compose.yaml stack management with full lifecycle support: create, edit, start, stop, restart, and delete stacks through its web UI. It includes an interactive YAML editor with syntax highlighting, a built-in web terminal for debugging containers, and the ability to convert docker run commands into compose.yaml format automatically.
Multi-Host Management
Since version 1.4, Dockge supports multiple agents, allowing users to manage Docker stacks across different hosts from a single interface. This makes it suitable for managing distributed container deployments across development, staging, and production environments.
File-Based Architecture
Unlike some container management tools, Dockge uses a file-based approach where compose files are stored on disk in their standard format. Users can continue to use standard docker compose CLI commands alongside the web UI. Dockge does not lock users into its interface — removing Dockge leaves all applications running normally.
Agent Integration Points
AI agents can use Dockge for automated container orchestration tasks: deploying application stacks, monitoring container status, managing Docker image updates, and coordinating multi-service deployments. The web UI runs on a configurable port and the stack definitions are standard compose.yaml files that agents can generate and manage programmatically.
Installation
Dockge runs as a Docker container itself. The recommended installation uses docker compose with volumes mounted for the Dockge data directory and the stacks directory. It requires Docker Engine 20.10+ and supports Linux, with the web UI accessible on port 5001 by default.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockge-docker-compose-stack-manager/)
