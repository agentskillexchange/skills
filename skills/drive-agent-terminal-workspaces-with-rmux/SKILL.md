---
name: "Drive agent terminal workspaces with Rmux"
slug: "drive-agent-terminal-workspaces-with-rmux"
description: "Use Rmux to create and automate cross-platform terminal sessions for agent CLIs, with tmux-compatible commands, typed SDKs, web sharing, and Claude Code teammate mode."
github_stars: 2379
verification: "security_reviewed"
source: "https://github.com/Helvesec/rmux"
author: "Rmux contributors"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Helvesec/rmux"
  github_stars: 2379
  npm_package: "@rmux/sdk"
  npm_weekly_downloads: 236
---

# Drive agent terminal workspaces with Rmux

Use Rmux to create and automate cross-platform terminal sessions for agent CLIs, with tmux-compatible commands, typed SDKs, web sharing, and Claude Code teammate mode.

## Prerequisites

Rmux CLI, optional Rust SDK, Python librmux package, TypeScript @rmux/sdk package, optional Claude Code and web-share setup

## Installation

Use the upstream install or setup path that matches your environment:
- cargo add rmux-sdk
- pip install librmux
- npm install @rmux/sdk
- cargo fmt --all -- --check

Requirements and caveats from upstream:
- RMUX now provides Python and TypeScript SDKs: [librmux](https://pypi.org/project/librmux/), [@rmux/sdk](https://www.npmjs.com/package/@rmux/sdk).
- RMUX is an async, typed terminal multiplexer engine written in Rust. It implements 90+ tmux commands and runs natively on Linux, macOS, and Windows with no WSL required.
- Use it as a standalone CLI, embed it in Rust terminal apps, or drive it through typed SDKs for Rust, Python, and TypeScript.

Basic usage or getting-started notes:
- <div><picture><source media="(min-width: 1360px) and (prefers-color-scheme: dark)" srcset="docs/sidebar/readme-desktop-sidebar-row-top-dark-v4.svg"><source media="(min-width: 1360px)" srcset="docs/sidebar/readme-deskt...
- For Unix .tar.gz downloads, run ./install.sh --prefix ~/.local from the
- Run Claude Code inside a local RMUX workspace with

- Source: https://github.com/Helvesec/rmux
- Extracted from upstream docs: https://raw.githubusercontent.com/Helvesec/rmux/HEAD/README.md

## Documentation

- https://rmux.io/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-agent-terminal-workspaces-with-rmux/)
