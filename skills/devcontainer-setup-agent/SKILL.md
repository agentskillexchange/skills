---
name: "Devcontainer Setup Agent"
slug: "devcontainer-setup-agent"
description: ""
github_stars: 2637
verification: "listed"
source: "https://github.com/devcontainers/cli"
author: "devcontainers"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "devcontainers/cli"
  github_stars: 2637
  npm_package: "@devcontainers/cli"
  npm_weekly_downloads: 260579
---

# Devcontainer Setup Agent



## Prerequisites

Node.js, Docker

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @devcontainers/cli
- git clone https://github.com/microsoft/vscode-remote-try-rust
- yarn
- yarn compile

Requirements and caveats from upstream:
- You can install the CLI with a standalone script that downloads a bundled Node.js runtime, so no pre-installed Node.js is required. It works on Linux and macOS (x64 and arm64):
- To install the npm package you will need Python and C/C++ installed to build one of the dependencies (see, e.g., [here](https://github.com/microsoft/vscode/wiki/How-to-Contribute) for instructions).
- [165 ms] Start: Run: docker build -f /home/node/vscode-remote-try-rust/.devcontainer/Dockerfile -t vsc-vscode-remote-try-rust-89420ad7399ba74f55921e49cc3ecfd2 --build-arg VARIANT=bullseye /home/node/vscode-remote-try-...

Basic usage or getting-started notes:
- A development container allows you to use a container as a full-featured development environment. It can be used to run an application, to separate tools, libraries, or runtimes needed for working with a codebase, and...
- [x] devcontainer run-user-commands - Runs lifecycle commands like postCreateCommand
- bash

- Source: https://github.com/devcontainers/cli
- Extracted from upstream docs: https://raw.githubusercontent.com/devcontainers/cli/HEAD/README.md

## Documentation

- https://github.com/devcontainers/cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-setup-agent/)
