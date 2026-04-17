---
title: "Chrome DevTools MCP Browser Debugging and Performance Analysis"
description: "Chrome DevTools MCP is an official ChromeDevTools project that turns Google Chrome into an MCP-accessible debugging and automation surface for coding agents. Instead of treating the browser like a black box, this server gives agents structured access to core DevTools workflows: page inspection, console analysis, network debugging, screenshots, trace capture, and browser automation. The project uses Puppeteer for reliable actions while also surfacing deeper debugging and performance capabilities that are hard to get from generic browser-control layers alone.\nFor teams building browser-heavy products, the job-to-be-done is clear: let an agent reproduce issues in a real browser, inspect what happened, and report back with evidence. Chrome DevTools MCP is especially useful when an agent needs to debug failed page loads, investigate JavaScript errors, profile runtime behavior, or collect performance insights from traces. Because it is packaged as an MCP server, the same tool can be plugged into clients such as Claude Code, Codex, Cursor, Copilot, or Gemini-compatible workflows.\nIntegration is straightforward. The README documents a standard MCP configuration using npx -y chrome-devtools-mcp@latest, with optional flags such as --slim and --headless for lighter browser-task modes. Upstream documentation also includes tool references, troubleshooting notes, and client-specific setup examples. This makes Chrome DevTools MCP a strong fit for Browser Automation skills that need real debugging depth, not just clicks and screenshots."
verification: security_reviewed
source: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/chrome-devtools-mcp-browser-debugging-performance-analysis
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/chrome-devtools-mcp-browser-debugging-performance-analysis` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-devtools-mcp-browser-debugging-performance-analysis/)
