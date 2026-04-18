---
title: "Browserbase MCP Server"
description: "Browserbase MCP Server gives agents cloud browser control through Browserbase and Stagehand, with both hosted HTTP and self-hosted stdio options. It suits teams that want MCP-based browser automation but prefer Browserbase sessions and Stagehand’s action model instead of running Playwright locally."
verification: security_reviewed
source: "https://github.com/browserbase/mcp-server-browserbase"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "browserbase/mcp-server-browserbase"
  github_stars: 3255
  ase_npm_package: "@browserbasehq/mcp"
  npm_weekly_downloads: 907
---

# Browserbase MCP Server

Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment.

The project exposes a focused set of browser tools including start, end, navigate, act, observe, and extract. Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, and optionally GEMINI_API_KEY.

This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/browserbase-mcp-server
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/browserbase-mcp-server` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-mcp-server/)
