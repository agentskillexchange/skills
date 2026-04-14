---
title: "Chrome DevTools MCP Browser Debugging and Performance Analysis"
description: "Chrome DevTools MCP connects an MCP-compatible agent to a live Chrome browser for debugging, automation, and performance work. It exposes Chrome DevTools capabilities through MCP, so agents can inspect network traffic, collect traces, capture screenshots, and automate browser actions from the same server."
verification: security_reviewed
source: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "ChromeDevTools/chrome-devtools-mcp"
  github_stars: 34239
---

# Chrome DevTools MCP Browser Debugging and Performance Analysis

Chrome DevTools MCP is an official ChromeDevTools project that turns Google Chrome into an MCP-accessible debugging and automation surface for coding agents. Instead of treating the browser like a black box, this server gives agents structured access to core DevTools workflows: page inspection, console analysis, network debugging, screenshots, trace capture, and browser automation. The project uses Puppeteer for reliable actions while also surfacing deeper debugging and performance capabilities that are hard to get from generic browser-control layers alone.

For teams building browser-heavy products, the job-to-be-done is clear: let an agent reproduce issues in a real browser, inspect what happened, and report back with evidence. Chrome DevTools MCP is especially useful when an agent needs to debug failed page loads, investigate JavaScript errors, profile runtime behavior, or collect performance insights from traces. Because it is packaged as an MCP server, the same tool can be plugged into clients such as Claude Code, Codex, Cursor, Copilot, or Gemini-compatible workflows.

Integration is straightforward. The README documents a standard MCP configuration using npx -y chrome-devtools-mcp@latest, with optional flags such as --slim and --headless for lighter browser-task modes. Upstream documentation also includes tool references, troubleshooting notes, and client-specific setup examples. This makes Chrome DevTools MCP a strong fit for Browser Automation skills that need real debugging depth, not just clicks and screenshots.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-devtools-mcp-browser-debugging-performance-analysis/)
