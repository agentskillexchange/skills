---
name: VS Code Extension Scaffolder
description: Scaffolds VS Code extensions using the vscode-extension API with TypeScript,
  including commands, webview panels, language servers via LSP, and custom tree view
  providers.
verification: security_reviewed
source: https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/
category:
- Developer Tools
framework:
- Cursor
---
# VS Code Extension Scaffolder

The VS Code Extension Scaffolder automates the creation of VS Code extensions by generating complete TypeScript projects with proper activation events, contribution points, and extension manifest configuration. It supports scaffolding commands with keybindings, webview panels with message passing between extension host and webview context, custom tree view providers with drag-and-drop support, and language server protocol (LSP) implementations using vscode-languageclient. The agent configures webpack bundling for production builds, sets up esbuild for fast development compilation, and generates comprehensive test suites using the @vscode/test-electron runner. It handles authentication provider registration, custom editor implementations for binary file formats, and notebook controller creation for Jupyter-compatible notebook types. The scaffolder includes CI configuration for publishing to the VS Code Marketplace via vsce and Open VSX Registry, with automatic version bumping and changelog generation from conventional commits.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/)
