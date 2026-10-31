---
name: "Agent Media Short Drama Series"
slug: "agent-media-ugc-video"
description: "Use Agent Media when an agent needs to make a short drama series (micro-drama, sitcom, K-drama style, any language) or another short vertical video through one hosted MCP connection, with the same cast every episode."
github_stars: 0
verification: "listed"
source: "https://github.com/agent-media-ai/agent-media"
author: "agent-media-ai"
category: "Image & Creative Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "agent-media-ai/agent-media"
  github_stars: 0
  npm_package: "@agentmedia/mcp-server"
  npm_weekly_downloads: 46
---

# Agent Media Short Drama Series

Use Agent Media when a Claude Code, Codex, Cursor, or other MCP-capable agent needs the video step of a UGC workflow rather than a generic asset prompt. The hosted Streamable HTTP MCP endpoint gives the agent tools to quote work before generation, create captioned vertical videos, generate or edit images, narrate b-roll, reuse saved characters, upload references, check account readiness, and poll asynchronous jobs until a final media URL is ready. The public repository also ships companion skills for full `make_ugc` flows, AI UGC test loops, and publish packets. It is useful for ad creative, product-in-hand demos, founder-style clips, b-roll narration, and iterative creative testing where the agent should reason about references, quote first, submit once approved, and return the finished result.

## Installation

Install or set up from the source-backed instructions:

npx skills add agent-media-ai/agent-media
claude mcp add --transport http --scope user agent-media https://api.agent-media.ai/mcp

- Source: https://github.com/agent-media-ai/agent-media

