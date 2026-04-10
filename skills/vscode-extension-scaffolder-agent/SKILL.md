---
title: "VS Code Extension Scaffolder"
description: "Scaffolds VS Code extensions using the vscode-extension API with TypeScript, including commands, webview panels, language servers via LSP, and custom tree view providers."
slug: "vscode-extension-scaffolder-agent"
category:
  - "Developer Tools"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/"
listed: true
---

# VS Code Extension Scaffolder

Scaffolds VS Code extensions using the vscode-extension API with TypeScript, including commands, webview panels, language servers via LSP, and custom tree view providers.

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
clawhub install vscode-extension-scaffolder-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The VS Code Extension Scaffolder automates the creation of VS Code extensions by generating complete TypeScript projects with proper activation events, contribution points, and extension manifest configuration. It supports scaffolding commands with keybindings, webview panels with message passing between extension host and webview context, custom tree view providers with drag-and-drop support, and language server protocol (LSP) implementations using vscode-languageclient. The agent configures webpack bundling for production builds, sets up esbuild for fast development compilation, and generates comprehensive test suites using the @vscode/test-electron runner. It handles authentication provider registration, custom editor implementations for binary file formats, and notebook controller creation for Jupyter-compatible notebook types. The scaffolder includes CI configuration for publishing to the VS Code Marketplace via vsce and Open VSX Registry, with automatic version bumping and changelog generation from conventional commits.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/)
