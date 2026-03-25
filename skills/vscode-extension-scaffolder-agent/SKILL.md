---
name: "VS Code Extension Scaffolder"
description: "Scaffolds VS Code extensions using the vscode-extension API with TypeScript, including commands, webview panels, language servers via LSP, and custom tree view providers."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "webpack"  # from ase_tool_match
  github_stars: 66013  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 44849699  # from ase_npm_downloads
  github_repo: "webpack/webpack"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# VS Code Extension Scaffolder

Scaffolds VS Code extensions using the vscode-extension API with TypeScript, including commands, webview panels, language servers via LSP, and custom tree view providers.

## Overview

The VS Code Extension Scaffolder automates the creation of VS Code extensions by generating complete TypeScript projects with proper activation events, contribution points, and extension manifest configuration. It supports scaffolding commands with keybindings, webview panels with message passing between extension host and webview context, custom tree view providers with drag-and-drop support, and language server protocol (LSP) implementations using vscode-languageclient. The agent configures webpack bundling for production builds, sets up esbuild for fast development compilation, and generates comprehensive test suites using the @vscode/test-electron runner. It handles authentication provider registration, custom editor implementations for binary file formats, and notebook controller creation for Jupyter-compatible notebook types. The scaffolder includes CI configuration for publishing to the VS Code Marketplace via vsce and Open VSX Registry, with automatic version bumping and changelog generation from conventional commits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-scaffolder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-scaffolder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-scaffolder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-scaffolder-agent -a codex
```

### OpenClaw

```bash
clawhub install vscode-extension-scaffolder-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/vscode-extension-scaffolder-agent/
