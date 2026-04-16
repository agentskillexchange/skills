---
title: "Tealdeer Fast Rust Implementation of tldr Command-Line Help Pages"
description: "Tealdeer is a very fast Rust implementation of the tldr project — simplified, example-based man pages for command-line tools. It provides quick reference with syntax highlighting, offline caching, and configurable output."
verification: "security_reviewed"
source: "https://github.com/tealdeer-rs/tealdeer"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tealdeer-rs/tealdeer"
  github_stars: 6115
  license: "MIT/Apache-2.0"
---

# Tealdeer Fast Rust Implementation of tldr Command-Line Help Pages

Overview

Tealdeer is a blazing-fast implementation of the tldr pages client written in Rust. The tldr project provides simplified, community-driven help pages for common command-line tools, offering practical examples instead of the dense, exhaustive format of traditional man pages. Tealdeer is one of the fastest tldr clients available, executing in roughly 13 milliseconds on cold cache — orders of magnitude faster than the Node.js reference client at 407ms.

Key Features

Tealdeer downloads and caches tldr pages locally, so it works completely offline after the initial cache fetch. It supports advanced syntax highlighting with configurable color schemes, custom page directories for adding your own documentation, platform-specific page filtering (Linux, macOS, Windows), and language selection for multilingual tldr pages. The client complies with the official tldr client specification.

How It Works

Run tldr tar to see practical examples of the tar command. Run tldr --update to refresh the local cache from the tldr-pages repository. Use tldr --list to see all available pages. Custom pages can be added to ~/.local/share/tealdeer/pages/. Configuration lives in ~/.config/tealdeer/config.toml where you can customize colors, display settings, and auto-update behavior.

Performance

Benchmarks using Hyperfine show tealdeer completing lookups in 13.2ms mean on a cold disk cache, compared to 407ms for the Node.js client and 87ms for the Python client. This speed comes from Rust’s zero-cost abstractions and tealdeer’s efficient cache implementation. The binary is small and has minimal resource usage.

Installation

Install via package managers: brew install tealdeer (macOS), pacman -S tealdeer (Arch), apt install tealdeer (Debian/Ubuntu), cargo install tealdeer (Rust). Static binaries are available on the GitHub releases page for all major platforms. After install, run tldr --update to fetch the page cache.

Agent Integration

Agents can use tealdeer as a quick-reference lookup tool when they need to recall the correct flags or syntax for command-line tools. Instead of parsing verbose man pages, an agent can query tldr for concise, example-driven help. The offline cache means no network calls during lookups, and the sub-20ms response time adds negligible latency to agent workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tealdeer-fast-tldr-client-rust/)
