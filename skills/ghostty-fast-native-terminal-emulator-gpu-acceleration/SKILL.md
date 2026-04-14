---
title: "Ghostty Fast Native Terminal Emulator with GPU Acceleration"
description: "Ghostty is a fast, feature-rich, cross-platform terminal emulator that uses platform-native UI and GPU acceleration. Created by Mitchell Hashimoto, it provides a native experience on macOS and Linux while supporting modern terminal protocols including Kitty graphics and synchronized rendering."
verification: security_reviewed
source: "https://github.com/ghostty-org/ghostty"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ghostty-org/ghostty"
  github_stars: 49204
---

# Ghostty Fast Native Terminal Emulator with GPU Acceleration

Ghostty is an open-source terminal emulator created by Mitchell Hashimoto (co-founder of HashiCorp) that prioritizes speed, features, and native platform integration. Unlike Electron-based alternatives, Ghostty uses platform-native UI toolkits — AppKit on macOS and GTK on Linux — delivering a terminal that feels like a first-class application on each platform.

The terminal emulator uses GPU acceleration for rendering, achieving competitive performance benchmarks while supporting rich features. Ghostty implements comprehensive terminal emulation standards including ECMA-48 and supports modern protocols like the Kitty graphics protocol, Kitty keyboard protocol, synchronized rendering, light/dark mode notifications, and clipboard sequences.

Ghostty supports multi-window, tabbing, and split panes natively. Its configuration is done through a simple key-value config file with sensible defaults. The terminal handles font rendering with subpixel antialiasing, ligature support, and font fallback chains.

Beyond the standalone application, Ghostty provides libghostty, a C-compatible library for embedding terminal emulation in third-party applications. This library enables other projects to leverage Ghostty’s terminal implementation without building from scratch.

The project is licensed under MIT and has been adopted by millions of users since its public release. Installation packages are available for macOS (DMG) and Linux (various package managers). The project maintains active development with regular releases and a responsive community on GitHub Discussions and Discord.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ghostty-fast-native-terminal-emulator-gpu-acceleration/)
