---
name: Agent Browser Operator
description: Interactive browser skill for logged-in flows, dynamic pages, and session-aware
  site operations.
verification: security_reviewed
source: https://github.com/microsoft/playwright
category:
- Browser Automation
framework:
- Custom Agents
- OpenClaw
tool_ecosystem:
  github_repo: microsoft/playwright
  github_stars: 85658
---
# Agent Browser Operator

Agent Browser Operator handles interactive, session-aware browser tasks where simple scraping is not enough. It is built for logged-in flows, dynamic page interactions, form filling, and multi-step site navigation that requires a real browser context.
Best for

logged-in admin workflows (WordPress, dashboards, internal tools)
multi-step form submission and interactive page flows
extracting data from JavaScript-rendered or authentication-gated pages

How it differs from MCP browser tools
Unlike MCP-based browser connectors (Playwright MCP, Browser MCP, Browserbase), Agent Browser Operator works through OpenClaw's native browser tool with direct session context. It is best for tasks that need the agent's own authenticated session rather than a standalone browser-as-a-service.
Install notes
Enable the browser tool in OpenClaw. For managed mode, install Chrome or Chromium on the host. For relay mode, use the OpenClaw Browser Relay Chrome extension.
Source: OpenClaw browser tool documentation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agent-browser-operator/)
