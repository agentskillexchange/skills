---
name: "code-server VS Code in the Browser by Coder"
description: "code-server lets you run VS Code on any remote machine and access it through a web browser. It provides a consistent cloud-based development environment, offloads intensive tasks to a server, and preserves battery life on client devices."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/coder/code-server"
---
# code-server VS Code in the Browser by Coder

code-server lets you run VS Code on any remote machine and access it through a web browser. It provides a consistent cloud-based development environment, offloads intensive tasks to a server, and preserves battery life on client devices.

## Overview

Overview

code-server is an open source project by Coder that runs Microsoft Visual Studio Code on a remote server, accessible through any modern web browser. With over 70,000 GitHub stars and active development, it is one of the most popular remote development tools available. It enables developers to code from any device — tablets, laptops, or even phones — while running compute-intensive tasks on powerful server hardware.

How It Works

code-server packages VS Code as a Node.js server process that serves the full VS Code editor experience over HTTP. It binds to a configurable port and serves the editor UI to any browser client. Authentication, TLS, and proxy configuration are all handled through CLI flags or a YAML config file.

Key Features

- Full VS Code experience: Extensions, settings, keybindings, and themes all work as expected in the browser-based editor.

- Remote compute: Run builds, tests, and compilations on the server instead of the local machine, speeding up resource-intensive workflows.

- Consistent environment: Developers get the same environment regardless of which device they connect from, eliminating “works on my machine” issues.

- Easy installation: A single install script handles setup on most Linux distributions. Also supports Docker, devcontainers, and cloud deployment templates.

- Team deployment: Can be deployed via `coder/coder` for team-wide remote development environments with provisioning and access controls.

Agent Integration

Agents can provision code-server instances for on-demand development environments, manage extensions programmatically via the CLI, and integrate with CI/CD pipelines to provide live debugging sessions. The tool pairs well with containerized workflows where agents spin up disposable dev environments for code review or pair programming.

Installation
``# Quick install (Linux/macOS)
curl -fsSL https://code-server.dev/install.sh | sh

# Start code-server
code-server

# Or via Docker
docker run -it --name code-server -p 127.0.0.1:8080:8080 \
-v "$HOME/.local:/home/coder/.local" \
-v "$PWD:/home/coder/project" \
codercom/code-server:latest``

Requirements

Minimum: Linux machine with WebSockets enabled, 1 GB RAM, and 2 vCPUs. Also runs on macOS and in Docker containers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill code-server-vs-code-browser-coder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill code-server-vs-code-browser-coder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill code-server-vs-code-browser-coder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill code-server-vs-code-browser-coder -a codex
```

### OpenClaw

```bash
clawhub install code-server-vs-code-browser-coder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/code-server-vs-code-browser-coder/)
