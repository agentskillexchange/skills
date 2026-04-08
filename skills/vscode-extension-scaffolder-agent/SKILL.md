---
title: VS Code Extension Scaffolder
description: The VS Code Extension Scaffolder automates the creation of VS Code extensions
  by generating complete TypeScript projects with proper activation events, contribution
  points, and extension manifest configuration. It supports scaffolding commands with
  keybindings, webview panels with message passing between extension host and webview
  context, custom tree view providers with drag-and-drop support, and language server
  protocol (LSP) implementations using vscode-languageclient. The agent configures
  webpack bundling for production builds, sets up esbuild for fast development compilation,
  and generates comprehensive test suites using the @vscode/test-electron runner.
  It handles authentication provider registration, custom editor implementations for
  binary file formats, and notebook controller creation for Jupyter-compatible notebook
  types. The scaffolder includes CI configuration for publishing to the VS Code Marketplace
  via vsce and Open VSX Registry, with automatic version bumping and changelog generation
  from conventional commits.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/)
