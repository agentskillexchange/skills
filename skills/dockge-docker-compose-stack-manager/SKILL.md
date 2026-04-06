---
name: Dockge Self-Hosted Docker Compose Stack Manager
description: Dockge is a self-hosted Docker Compose stack manager with a reactive
  web UI for managing compose.yaml files. Created by Louis Lam (author of Uptime Kuma),
  it provides an interactive editor, web terminal, and multi-agent support for managing
  Docker stacks across hosts.
category: Developer Tools
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/louislam/dockge"
tool_ecosystem:
  github_repo: "https://github.com/louislam/dockge"
  github_stars: 22685
  license: MIT
---
# Dockge Self-Hosted Docker Compose Stack Manager

Dockge is a self-hosted Docker Compose stack manager with a reactive web UI for managing compose.yaml files. Created by Louis Lam (author of Uptime Kuma), it provides an interactive editor, web terminal, and multi-agent support for managing Docker stacks across hosts.

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

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dockge-docker-compose-stack-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dockge-docker-compose-stack-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dockge-docker-compose-stack-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dockge-docker-compose-stack-manager -a codex
```

### OpenClaw

```bash
clawhub install dockge-docker-compose-stack-manager
```


## Source

- [GitHub](https://github.com/louislam/dockge)
