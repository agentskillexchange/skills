---
name: Dockge Self-Hosted Docker Compose Stack Manager
description: Dockge is a self-hosted Docker Compose stack manager with a reactive
  web UI for managing compose.yaml files. Created by Louis Lam (author of Uptime Kuma),
  it provides an interactive editor, web terminal, and multi-agent support for managing
  Docker stacks across hosts.
verification: security_reviewed
source: https://github.com/louislam/dockge
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: louislam/dockge
  github_stars: 22685
  license: MIT
---
# Dockge Self-Hosted Docker Compose Stack Manager

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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockge-docker-compose-stack-manager/)
