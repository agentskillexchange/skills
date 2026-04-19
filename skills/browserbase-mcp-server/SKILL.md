---
title: "Browserbase MCP Server"
description: "Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment. The project exposes a focused set of browser tools including start , end , navigate , act , observe , and extract . Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY , BROWSERBASE_PROJECT_ID , and optionally GEMINI_API_KEY . This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools."
source: "https://github.com/browserbase/mcp-server-browserbase"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "browserbase/mcp-server-browserbase"
  github_stars: 3255
  npm_package: "@browserbasehq/mcp"
  npm_weekly_downloads: 907
---

# Browserbase MCP Server

Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment. The project exposes a focused set of browser tools including start , end , navigate , act , observe , and extract . Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY , BROWSERBASE_PROJECT_ID , and optionally GEMINI_API_KEY . This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-mcp-server/)
