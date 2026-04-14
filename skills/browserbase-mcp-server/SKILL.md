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
  npm_package: "@browserbasehq/mcp"
  npm_weekly_downloads: 907
---

# Browserbase MCP Server

Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment.

The project exposes a focused set of browser tools including start, end, navigate, act, observe, and extract. Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, and optionally GEMINI_API_KEY.

This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-mcp-server/)
