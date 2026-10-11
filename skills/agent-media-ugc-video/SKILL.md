---
name: "Agent Media UGC Video"
slug: "agent-media-ugc-video"
description: "Use Agent Media when an agent needs to create captioned vertical UGC videos, narrated b-roll overlays, reusable characters, images, and voice through a hosted MCP server and companion skills."
verification: "listed"
source: "https://github.com/agent-media-ai/agent-media"
category: "Image & Creative Automation"
framework: "MCP"
---

# Agent Media UGC Video

Use Agent Media when a Claude Code, Codex, Cursor, or other MCP-capable agent needs the video step of a UGC workflow rather than a generic asset prompt. The hosted Streamable HTTP MCP endpoint gives the agent tools to quote work before generation, create captioned vertical videos, generate or edit images, narrate b-roll, reuse saved characters, upload references, check account readiness, and poll asynchronous jobs until a final media URL is ready. The public repository also ships companion skills for full `make_ugc` flows, AI UGC test loops, and publish packets. It is useful for ad creative, product-in-hand demos, founder-style clips, b-roll narration, and iterative creative testing where the agent should reason about references, quote first, submit once approved, and return the finished result.

## Installation

### Hosted MCP connector

Add the remote Streamable HTTP MCP server to an MCP-capable client:

```json
{
  "mcpServers": {
    "agent-media": {
      "type": "http",
      "url": "https://api.agent-media.ai/mcp"
    }
  }
}
```

Authenticate through the browser OAuth flow opened by the client. For Claude Code, use:

```bash
claude mcp add --transport http --scope user agent-media https://api.agent-media.ai/mcp
```

For Codex, use:

```bash
codex mcp add agent-media --url https://api.agent-media.ai/mcp
codex mcp login agent-media
```

### Companion skills

Install the upstream Agent Media skill pack when the agent runtime supports GitHub-hosted skills:

```bash
npx skills add agent-media-ai/agent-media
```

### Direct Agent Skill Exchange install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/agent-media-ugc-video ~/.agent-skills/agent-media-ugc-video
```
