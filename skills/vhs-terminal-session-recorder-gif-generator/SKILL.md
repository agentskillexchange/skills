---
name: "VHS Terminal Session Recorder and GIF Generator"
slug: "vhs-terminal-session-recorder-gif-generator"
description: "Create terminal session recordings as GIFs, videos, or images using VHS (charmbracelet/vhs). Write declarative .tape scripts that define typed commands, delays, and settings — then render pixel-perfect terminal demos automatically."
github_stars: 19204
verification: "security_reviewed"
source: "https://github.com/charmbracelet/vhs"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "charmbracelet/vhs"
  github_stars: 19204
---

# VHS Terminal Session Recorder and GIF Generator

Create terminal session recordings as GIFs, videos, or images using VHS (charmbracelet/vhs). Write declarative .tape scripts that define typed commands, delays, and settings — then render pixel-perfect terminal demos automatically.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install vhs
- Or, use Docker to run VHS directly, dependencies included:
- docker run --rm -v $PWD:/vhs ghcr.io/charmbracelet/vhs <cassette>.tape
- go install github.com/charmbracelet/vhs@latest

Requirements and caveats from upstream:
- VHS requires [ttyd](https://github.com/tsl0922/ttyd) and [ffmpeg](https://ffmpeg.org) to be installed and available on your PATH.
- [Require <program>](#require): specify required programs for tape file
- ### Require

Basic usage or getting-started notes:
- The above example was generated with VHS ([view source](./examples/neofetch/neofetch.tape)).
- # Run the command by pressing enter.
- [!NOTE]

- Source: https://github.com/charmbracelet/vhs
- Extracted from upstream docs: https://raw.githubusercontent.com/charmbracelet/vhs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vhs-terminal-session-recorder-gif-generator/)
