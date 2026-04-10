---
name: Chrome DevTools MCP Browser Debugging and Performance Analysis
description: Chrome DevTools MCP connects an MCP-compatible agent to a live Chrome
  browser for debugging, automation, and performance work. It exposes Chrome DevTools
  capabilities through MCP, so agents can inspect network traffic, collect traces,
  capture screenshots, and automate browser actions from the same server.
verification: security_reviewed
source: https://github.com/ChromeDevTools/chrome-devtools-mcp
category:
- Browser Automation
framework:
- MCP
tool_ecosystem:
  github_repo: ChromeDevTools/chrome-devtools-mcp
  github_stars: 33906
---
# Chrome DevTools MCP Browser Debugging and Performance Analysis

Chrome DevTools MCP is an official ChromeDevTools project that turns Google Chrome into an MCP-accessible debugging and automation surface for coding agents. Instead of treating the browser like a black box, this server gives agents structured access to core DevTools workflows: page inspection, console analysis, network debugging, screenshots, trace capture, and browser automation. The project uses Puppeteer for reliable actions while also surfacing deeper debugging and performance capabilities that are hard to get from generic browser-control layers alone.
For teams building browser-heavy products, the job-to-be-done is clear: let an agent reproduce issues in a real browser, inspect what happened, and report back with evidence. Chrome DevTools MCP is especially useful when an agent needs to debug failed page loads, investigate JavaScript errors, profile runtime behavior, or collect performance insights from traces. Because it is packaged as an MCP server, the same tool can be plugged into clients such as Claude Code, Codex, Cursor, Copilot, or Gemini-compatible workflows.
Integration is straightforward. The README documents a standard MCP configuration using npx -y chrome-devtools-mcp@latest, with optional flags such as --slim and --headless for lighter browser-task modes. Upstream documentation also includes tool references, troubleshooting notes, and client-specific setup examples. This makes Chrome DevTools MCP a strong fit for Browser Automation skills that need real debugging depth, not just clicks and screenshots.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-devtools-mcp-browser-debugging-performance-analysis/)
