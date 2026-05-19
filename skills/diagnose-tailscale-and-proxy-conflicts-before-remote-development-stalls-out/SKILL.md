---
name: "Diagnose Tailscale and proxy conflicts before remote development stalls out"
slug: "diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out"
description: "Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis."
verification: "security_reviewed"
source: "https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md"
author: "daymade"
publisher_type: "github_skill"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
---

# Diagnose Tailscale and proxy conflicts before remote development stalls out

Use tunnel-doctor in Claude Code when Tailscale partially works but SSH, browser, git, or Docker paths fail because proxy, route, or double-tunneling conflicts need a structured diagnosis.

## Prerequisites

Read, Grep, Edit, Bash

## Installation

Use the upstream install or setup path that matches your environment:
- uv run --with weasyprint scripts/md_to_pdf.py input.md output.pdf
- npx promptfoo@latest init
- npx promptfoo@latest eval
- npx promptfoo@latest view

Requirements and caveats from upstream:
- Require data visualization and charts
- **Requirements**: Python 3.8+, FFmpeg/FFprobe (install via brew install ffmpeg, apt install ffmpeg, or winget install ffmpeg)
- **Requirements**: Python 3.8+, pandoc (system install), weasyprint (or Chrome as fallback backend)

Basic usage or getting-started notes:
- text
- /plugin marketplace add daymade/claude-code-skills
- Then:

- Source: https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md
- Extracted from upstream docs: https://raw.githubusercontent.com/daymade/claude-code-skills/HEAD/README.md

## Documentation

- https://github.com/daymade/claude-code-skills/blob/main/tunnel-doctor/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-tailscale-and-proxy-conflicts-before-remote-development-stalls-out/)
