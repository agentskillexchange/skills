---
name: "Ghostty Fast Native Terminal Emulator with GPU Acceleration"
description: "Ghostty is a fast, feature-rich, cross-platform terminal emulator that uses platform-native UI and GPU acceleration. Created by Mitchell Hashimoto, it provides a native experience on macOS and Linux while supporting modern terminal protocols including Kitty graphics and synchronized rendering."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/ghostty-org/ghostty"
tool_ecosystem:
  tool: ghostty
  github_repo: ghostty-org/ghostty
  github_stars: 49204
  license: MIT
  maintained: true
---
# Ghostty Fast Native Terminal Emulator with GPU Acceleration

Ghostty is a fast, feature-rich, cross-platform terminal emulator that uses platform-native UI and GPU acceleration. Created by Mitchell Hashimoto, it provides a native experience on macOS and Linux while supporting modern terminal protocols including Kitty graphics and synchronized rendering.

## Overview

Ghostty is an open-source terminal emulator created by Mitchell Hashimoto (co-founder of HashiCorp) that prioritizes speed, features, and native platform integration. Unlike Electron-based alternatives, Ghostty uses platform-native UI toolkits — AppKit on macOS and GTK on Linux — delivering a terminal that feels like a first-class application on each platform.

The terminal emulator uses GPU acceleration for rendering, achieving competitive performance benchmarks while supporting rich features. Ghostty implements comprehensive terminal emulation standards including ECMA-48 and supports modern protocols like the Kitty graphics protocol, Kitty keyboard protocol, synchronized rendering, light/dark mode notifications, and clipboard sequences.

Ghostty supports multi-window, tabbing, and split panes natively. Its configuration is done through a simple key-value config file with sensible defaults. The terminal handles font rendering with subpixel antialiasing, ligature support, and font fallback chains.

Beyond the standalone application, Ghostty provides libghostty, a C-compatible library for embedding terminal emulation in third-party applications. This library enables other projects to leverage Ghostty's terminal implementation without building from scratch.

The project is licensed under MIT and has been adopted by millions of users since its public release. Installation packages are available for macOS (DMG) and Linux (various package managers). The project maintains active development with regular releases and a responsive community on GitHub Discussions and Discord.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ghostty-fast-native-terminal-emulator-gpu-acceleration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ghostty-fast-native-terminal-emulator-gpu-acceleration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ghostty-fast-native-terminal-emulator-gpu-acceleration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ghostty-fast-native-terminal-emulator-gpu-acceleration -a codex
```

### OpenClaw

```bash
clawhub install ghostty-fast-native-terminal-emulator-gpu-acceleration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ghostty-fast-native-terminal-emulator-gpu-acceleration/)
