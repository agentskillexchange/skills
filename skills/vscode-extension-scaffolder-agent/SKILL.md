---
title: "VS Code Extension Scaffolder"
description: "Scaffolds VS Code extensions using the vscode-extension API with TypeScript, including commands, webview panels, language servers via LSP, and custom tree view providers."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# VS Code Extension Scaffolder

The VS Code Extension Scaffolder automates the creation of VS Code extensions by generating complete TypeScript projects with proper activation events, contribution points, and extension manifest configuration. It supports scaffolding commands with keybindings, webview panels with message passing between extension host and webview context, custom tree view providers with drag-and-drop support, and language server protocol (LSP) implementations using vscode-languageclient. The agent configures webpack bundling for production builds, sets up esbuild for fast development compilation, and generates comprehensive test suites using the @vscode/test-electron runner. It handles authentication provider registration, custom editor implementations for binary file formats, and notebook controller creation for Jupyter-compatible notebook types. The scaffolder includes CI configuration for publishing to the VS Code Marketplace via vsce and Open VSX Registry, with automatic version bumping and changelog generation from conventional commits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/)
