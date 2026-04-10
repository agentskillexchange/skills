---
title: "Browserbase MCP Server"
description: "Browserbase MCP Server gives agents cloud browser control through Browserbase and Stagehand, with both hosted HTTP and self-hosted stdio options. It suits teams that want MCP-based browser automation but prefer Browserbase sessions and Stagehand’s action model instead of running Playwright locally."
slug: "browserbase-mcp-server"
category:
  - "Browser Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/browserbase/mcp-server-browserbase"
listed: true
---

# Browserbase MCP Server

Browserbase MCP Server gives agents cloud browser control through Browserbase and Stagehand, with both hosted HTTP and self-hosted stdio options. It suits teams that want MCP-based browser automation but prefer Browserbase sessions and Stagehand’s action model instead of running Playwright locally.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install browserbase-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment.
The project exposes a focused set of browser tools including start, end, navigate, act, observe, and extract. Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, and optionally GEMINI_API_KEY.
This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-mcp-server/)
