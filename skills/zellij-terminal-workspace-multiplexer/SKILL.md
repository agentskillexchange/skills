---
name: "Zellij Terminal Workspace and Multiplexer"
description: "Zellij is a Rust-powered terminal workspace and multiplexer with floating panes, WebAssembly plugins, layout persistence, multiplayer collaboration, and a built-in web client. A modern replacement for tmux and screen."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zellij-terminal-workspace-multiplexer/"
---

# Zellij Terminal Workspace and Multiplexer

Zellij is a Rust-powered terminal workspace and multiplexer with floating panes, WebAssembly plugins, layout persistence, multiplayer collaboration, and a built-in web client. A modern replacement for tmux and screen.

## Overview

Zellij is a terminal workspace written in Rust that serves as a modern replacement for traditional terminal multiplexers like tmux and screen. With over 30,000 GitHub stars, it has emerged as one of the most actively developed terminal tools, built around the philosophy that simplicity and power can coexist.

The skill enables agents to manage terminal sessions, layouts, and pane configurations through Zellij’s structured interface. Unlike traditional multiplexers that require memorizing key combinations, Zellij provides discoverable keybindings and a built-in UI that guides users through available actions. This makes it suitable for both interactive use and automated workflows.

Zellij’s plugin system uses WebAssembly, allowing plugins written in any language that compiles to WASM to extend functionality. The built-in layout system lets users define workspace configurations declaratively, specifying pane arrangements, default commands, and tab structures. These layouts can be version-controlled and shared across team members.

Key features include floating and stacked panes for flexible window management, true multiplayer collaboration where multiple users can share a session in real time, and a built-in web client that makes a local terminal optional. The session persistence system automatically saves and restores workspace state across restarts.

Agents can use Zellij to orchestrate multi-pane development environments, run parallel build and test processes, manage long-running services, and create reproducible workspace configurations. The tool supports custom keybindings, themes, and extensive configuration through its KDLTL-based config format. Zellij runs on Linux and macOS with packages available through most system package managers, Homebrew, and Cargo.

## Installation

### Claude Code
```bash
npx skills add agentskillexchange/skills/skills/zellij-terminal-workspace-multiplexer
```

### Cursor
```bash
npx skills add agentskillexchange/skills/skills/zellij-terminal-workspace-multiplexer
```

### Codex
```bash
npx skills add agentskillexchange/skills/skills/zellij-terminal-workspace-multiplexer
```

### OpenClaw
```bash
clawhub install zellij-terminal-workspace-multiplexer
```

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills/skills/zellij-terminal-workspace-multiplexer
```
