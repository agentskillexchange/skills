---
title: "Crush Agentic AI Coding CLI by Charmbracelet"
description: "Crush is a terminal-native AI coding agent built by Charmbracelet that connects your code, tools, and workflows to any LLM. It supports multi-model switching mid-session, MCP extensibility, and LSP-enhanced context across every major platform."
slug: "crush-agentic-ai-coding-cli-charmbracelet"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/charmbracelet/crush"
tool_ecosystem:
  github_repo: "charmbracelet/crush"
  github_stars: 22213
listed: true
---

# Crush Agentic AI Coding CLI by Charmbracelet

Crush is a terminal-native AI coding agent built by Charmbracelet that connects your code, tools, and workflows to any LLM. It supports multi-model switching mid-session, MCP extensibility, and LSP-enhanced context across every major platform.

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
clawhub install crush-agentic-ai-coding-cli-charmbracelet
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

What is Crush?
Crush is an agentic AI coding assistant designed to run in your terminal. Built by Charmbracelet — the team behind Glow, Bubble Tea, and other popular terminal tools — Crush connects your code, tools, and workflows directly to the LLM of your choice. It replaces the archived Mods project with a full-featured agent that understands your codebase through LSP integration and can be extended via Model Context Protocol (MCP) servers.
How It Works
Install Crush via Homebrew, npm, Winget, or package managers for Arch, Nix, Debian, and Fedora. Run crush in your terminal to start an interactive session. Crush maintains session-based context per project, so switching between repos preserves conversation history. You can configure multiple LLM providers (OpenAI, Anthropic, local models via OpenAI-compatible APIs) and switch between them mid-conversation without losing context.
Key Capabilities
Crush reads your codebase through Language Server Protocol (LSP) support — the same mechanism your editor uses for autocompletion and type checking. This gives the LLM real structural understanding of your code rather than just raw text. You can extend Crush with MCP servers over HTTP, stdio, or SSE transports, adding capabilities like database access, documentation lookup, or custom tooling. The tool runs natively on macOS, Linux, Windows (PowerShell and WSL), Android, FreeBSD, OpenBSD, and NetBSD.
Non-Interactive Mode
Beyond the interactive TUI, Crush provides crush run for pipeline integration. Pipe command output or file contents into Crush for formatting, analysis, or transformation — similar to the workflow the now-archived Mods project provided, but with the added context of the full agent runtime.
Integration Points
Crush integrates with any OpenAI-compatible or Anthropic-compatible API endpoint. It supports MCP for tool extensibility, LSP for code understanding, and standard Unix pipes for non-interactive workflows. Session state persists between runs, making it practical for ongoing development work across multiple projects.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crush-agentic-ai-coding-cli-charmbracelet/)
