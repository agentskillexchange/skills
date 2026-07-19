---
name: "Monitor Claude Code sessions and tool activity with Claude Code Agent Monitor"
slug: "monitor-claude-code-sessions-and-tool-activity-with-claude-code-agent-monitor"
description: "Install Claude Code hooks that stream session, tool, subagent, and workflow events into a local dashboard for live observability and review."
github_stars: 815
verification: "security_reviewed"
source: "https://github.com/hoangsonww/Claude-Code-Agent-Monitor"
author: "hoangsonww"
publisher_type: "individual"
category: "Monitoring & Alerts"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "hoangsonww/Claude-Code-Agent-Monitor"
  github_stars: 815
---

# Monitor Claude Code sessions and tool activity with Claude Code Agent Monitor

Install Claude Code hooks that stream session, tool, subagent, and workflow events into a local dashboard for live observability and review.

## Prerequisites

Claude Code, Node.js 20+, npm, local dashboard server; optional MCP host integration

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/hoangsonww/Claude-Code-Agent-Monitor.git
- npm run setup
- npm run install-hooks
- npm run dev

Requirements and caveats from upstream:
- A professional dashboard to track and visualize your Claude Code agent sessions, tool usage, and subagent orchestration in real-time. Built with Node.js, Express, React, and SQLite, it integrates directly with Claude...
- ![Node.js](https://img.shields.io/badge/Node.js-%3E%3D20-339933?style=flat-square&logo=node.js&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-%3E%3D3.6-3776AB?style=flat-square&logo=python&logoColor=white)

Basic usage or getting-started notes:
- Track sessions, monitor agents in real-time, visualize tool usage, and observe subagent orchestration through a professional dark-themed web interface. Integrates directly with Claude Code via its native hook system.
- <em>🤖 <strong>Session Detail · Agents</strong> — real-time overview tiles (events, tool calls, subagents, compactions, errors, duration), top-tool usage bars, subagent type breakdown, token flow, and the agent hierarc...
- <em>📊 <strong>Analytics</strong> — token usage by model, tool frequency, activity heatmap, and session trends with live / offline indicator</em>

- Source: https://github.com/hoangsonww/Claude-Code-Agent-Monitor
- Extracted from upstream docs: https://raw.githubusercontent.com/hoangsonww/Claude-Code-Agent-Monitor/HEAD/README.md

## Documentation

- https://github.com/hoangsonww/Claude-Code-Agent-Monitor

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-claude-code-sessions-and-tool-activity-with-claude-code-agent-monitor/)
