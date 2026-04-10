---
name: Browserbase MCP Server
description: Browserbase MCP Server gives agents cloud browser control through Browserbase
  and Stagehand, with both hosted HTTP and self-hosted stdio options. It suits teams
  that want MCP-based browser automation but prefer Browserbase sessions and Stagehand’s
  action model instead of running Playwright locally.
verification: security_reviewed
source: https://github.com/browserbase/mcp-server-browserbase
category:
- Browser Automation
framework:
- MCP
---
# Browserbase MCP Server

Browserbase MCP Server is Browserbase’s MCP implementation for cloud browser automation. It connects an MCP client to Browserbase sessions and Stagehand so an agent can start a browser session, navigate pages, observe actionable elements, execute actions, and extract information from live sites. The upstream README documents both a hosted MCP endpoint and a self-hosted npm package, which makes it flexible for teams that want a quick managed setup or tighter control over deployment.
The project exposes a focused set of browser tools including start, end, navigate, act, observe, and extract. Browserbase positions this as a standardized MCP bridge for LLM applications, while Stagehand provides the browser interaction layer and default model-backed action engine. For self-hosted operation, the maintainer documents an npx @browserbasehq/mcp flow with environment variables for BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID, and optionally GEMINI_API_KEY.
This belongs in Browser Automation because the real job-to-be-done is running web actions in a browser session from an MCP client, not just scraping static HTML. It also clearly maps to the MCP framework and has strong external verification signals: an official GitHub repository, npm package, published documentation, open-source license, and healthy adoption. For users already invested in Browserbase or Stagehand, this is one of the most direct ways to expose those capabilities to agentic tools.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-mcp-server/)
