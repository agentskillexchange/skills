---
title: "Crush Agentic AI Coding CLI by Charmbracelet"
description: "What is Crush?\nCrush is an agentic AI coding assistant designed to run in your terminal. Built by Charmbracelet — the team behind Glow, Bubble Tea, and other popular terminal tools — Crush connects your code, tools, and workflows directly to the LLM of your choice. It replaces the archived Mods project with a full-featured agent that understands your codebase through LSP integration and can be extended via Model Context Protocol (MCP) servers.\nHow It Works\nInstall Crush via Homebrew, npm, Winget, or package managers for Arch, Nix, Debian, and Fedora. Run crush in your terminal to start an interactive session. Crush maintains session-based context per project, so switching between repos preserves conversation history. You can configure multiple LLM providers (OpenAI, Anthropic, local models via OpenAI-compatible APIs) and switch between them mid-conversation without losing context.\nKey Capabilities\nCrush reads your codebase through Language Server Protocol (LSP) support — the same mechanism your editor uses for autocompletion and type checking. This gives the LLM real structural understanding of your code rather than just raw text. You can extend Crush with MCP servers over HTTP, stdio, or SSE transports, adding capabilities like database access, documentation lookup, or custom tooling. The tool runs natively on macOS, Linux, Windows (PowerShell and WSL), Android, FreeBSD, OpenBSD, and NetBSD.\nNon-Interactive Mode\nBeyond the interactive TUI, Crush provides crush run for pipeline integration. Pipe command output or file contents into Crush for formatting, analysis, or transformation — similar to the workflow the now-archived Mods project provided, but with the added context of the full agent runtime.\nIntegration Points\nCrush integrates with any OpenAI-compatible or Anthropic-compatible API endpoint. It supports MCP for tool extensibility, LSP for code understanding, and standard Unix pipes for non-interactive workflows. Session state persists between runs, making it practical for ongoing development work across multiple projects."
verification: security_reviewed
source: "https://github.com/charmbracelet/crush"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "charmbracelet/crush"
  github_stars: 22213
---

# Crush Agentic AI Coding CLI by Charmbracelet

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crush-agentic-ai-coding-cli-charmbracelet
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/crush-agentic-ai-coding-cli-charmbracelet` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crush-agentic-ai-coding-cli-charmbracelet/)
