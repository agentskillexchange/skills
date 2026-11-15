---
name: "Drive ComfyUI generation workflows through comfyui-mcp"
slug: "drive-comfyui-generation-workflows-through-comfyui-mcp"
description: "Use comfyui-mcp to let an MCP-capable agent author, run, debug, and manage ComfyUI image, video, audio, model, and custom-node workflows from natural-language instructions."
github_stars: 386
verification: "security_reviewed"
source: "https://github.com/artokun/comfyui-mcp"
author: "artokun"
publisher_type: "open_source"
category: "Image & Creative Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "artokun/comfyui-mcp"
  github_stars: 386
  npm_package: "comfyui-mcp"
  npm_weekly_downloads: 86436
---

# Drive ComfyUI generation workflows through comfyui-mcp

Use comfyui-mcp to let an MCP-capable agent author, run, debug, and manage ComfyUI image, video, audio, model, and custom-node workflows from natural-language instructions.

## Prerequisites

ComfyUI; Node.js 22 or newer; an MCP-capable client such as Claude Code, Claude Desktop, Cursor, VS Code, or another MCP client; optional Claude Code plugin; optional RunPod/VPS/LAN/Comfy Cloud environment

## Installation

Use the upstream install or setup path that matches your environment:
- npm run generations:stats
- npx -y comfyui-mcp@latest --comfyui-url http://localhost:8188 --force-remote
- npx -y comfyui-mcp@latest
- npx -y comfyui-mcp@latest --http

Requirements and caveats from upstream:
- [![Node.js](https://img.shields.io/badge/node-%3E%3D22.0.0-brightgreen)](https://nodejs.org)
- **108 MCP tools** | **32 AI skills** (Flux · WAN · LTX 2.3 video · Qwen · Z-Image · Ideogram 4 · ERNIE · ANIMA · model registry · Civitai · node authoring · launch/perf flags) | **13 installer packs** | **11 slash com...
- The plugin ships **expert skills that grow with every release** — model-specific generation guides with curated download URLs, workflow recipes, troubleshooting, and custom-node authoring — so Claude knows the right s...

Basic usage or getting-started notes:
- [![Deploy on RunPod](https://img.shields.io/badge/Deploy_on-RunPod-673AB7?style=for-the-badge)](https://console.runpod.io/deploy?template=bnqtkvcer3&ref=dkx71w9b) [![Join the Discord](https://img.shields.io/badge/Disc...
- /plugin marketplace add artokun/comfyui-mcp
- /plugin install comfy

- Source: https://github.com/artokun/comfyui-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/artokun/comfyui-mcp/HEAD/README.md

## Documentation

- https://comfyui-mcp.artokun.io/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-comfyui-generation-workflows-through-comfyui-mcp/)
