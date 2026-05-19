---
name: "Run computer-use agents inside cross-OS desktop sandboxes with CUA"
slug: "run-computer-use-agents-inside-cross-os-desktop-sandboxes-with-cua"
description: "Launch computer-use agents in Linux, macOS, Windows, or Android sandboxes and drive full desktop tasks through screenshots, mouse, keyboard, and shell controls."
github_stars: 13544
verification: "security_reviewed"
source: "https://github.com/trycua/cua"
author: "trycua"
publisher_type: "organization"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "trycua/cua"
  github_stars: 13544
---

# Run computer-use agents inside cross-OS desktop sandboxes with CUA

Launch computer-use agents in Linux, macOS, Windows, or Android sandboxes and drive full desktop tasks through screenshots, mouse, keyboard, and shell controls.

## Prerequisites

Python 3.11+ for the SDK or Node.js for cuabot, plus local QEMU or CUA cloud access depending on runtime choice.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install cua
- uv tool install -e . && cb image create linux-docker

Requirements and caveats from upstream:
- python
- # Requires Python 3.11 or later
- | [lumier](https://cua.ai/docs/lume/guide/advanced/lumier) | Docker-compatible interface for Lume VMs |

Basic usage or getting-started notes:
- result = await sb.shell.run("echo hello")
- cd cua-bench
- # Run benchmark with agent

- Source: https://github.com/trycua/cua
- Extracted from upstream docs: https://raw.githubusercontent.com/trycua/cua/HEAD/README.md

## Documentation

- https://cua.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-computer-use-agents-inside-cross-os-desktop-sandboxes-with-cua/)
