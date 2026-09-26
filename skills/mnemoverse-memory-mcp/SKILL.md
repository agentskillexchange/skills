---
name: "Mnemoverse Memory MCP"
slug: "mnemoverse-memory-mcp"
description: "Give Claude Code, Cursor, VS Code and ChatGPT agents hosted persistent memory over MCP that learns from outcomes: the agent calls memory_feedback to report whether a recalled memory helped or misled, and later memory_read results are re-ranked. Use it when memory has to follow an agent across sessions and clients, or when several agents share one memory through a room."
category: "Integrations & Connectors"
framework: "MCP"
verification: listed
source: "https://github.com/mnemoverse/mcp-memory-server"
tool_ecosystem:
  tool: "mnemoverse"
  github_repo: "mnemoverse/mcp-memory-server"
  npm_package: "@mnemoverse/mcp-memory-server"
  license: "MIT"
  maintained: true
---

# Mnemoverse Memory MCP

Mnemoverse is hosted persistent memory for AI agents, reached over the Model Context Protocol. The agent stores durable facts, decisions and corrections with `memory_write` and recalls them by natural-language query with `memory_read`. After using a recalled memory it calls `memory_feedback` to say whether that memory helped or misled, and what comes back next is re-ranked by that report. Shared rooms (`memory_create_room`, `memory_invite_to_room`, `memory_join_room`, `memory_list_rooms`) let several agents or accounts read and write one memory. `memory_list_recent` lists the newest memories, `memory_stats` shows counts and domains, and `vault_list` names stored secrets by alias without returning their values. Those are the server's ten tools.

The MCP server is the MIT-licensed npm package `@mnemoverse/mcp-memory-server` ([source](https://github.com/mnemoverse/mcp-memory-server)). The memory engine behind it is a proprietary hosted service; Enterprise customers can self-host it by agreement. The same account works from Claude Code, Cursor, VS Code and ChatGPT, with an API key or with OAuth sign-in.

## When to use it

- An agent relearns the same project facts, conventions or past decisions at the start of every session.
- The same memory should be available in more than one client, for example Claude Code at the desk and ChatGPT elsewhere.
- Several agents work on one task and need a common memory: create a room, invite the others, and pass the room address as the `domain` argument.
- You want recall order to respond to whether earlier recalls actually helped, instead of staying fixed.

## When not to use it

- The data has to stay on the local machine: memories are stored by the hosted service.
- The information only matters inside the current conversation.

## Working pattern

1. Before a task, call `memory_read` with a query that names the task, and use what comes back.
2. After the task, call `memory_feedback` on each recalled memory you relied on, marking it as helped or misled.
3. Save new durable decisions, corrections and failures with `memory_write` as short self-contained statements.
4. For shared work, call `memory_list_rooms` to find the room address and use it as the `domain` on reads and writes.

## Installation

### Claude Code: remote server with OAuth sign-in

```bash
claude mcp add --transport http mnemoverse https://mcp.mnemoverse.com/mcp
```

Run `/mcp` in Claude Code and complete the browser sign-in. No API key is needed on this path.

### Any MCP client: local stdio server with an API key

```bash
npx -y @mnemoverse/mcp-memory-server@latest
```

The server starts and lists its tools without a key; every tool call needs `MNEMOVERSE_API_KEY`, a free key from https://console.mnemoverse.com. Client configuration:

```json
{
  "mcpServers": {
    "mnemoverse": {
      "command": "npx",
      "args": ["-y", "@mnemoverse/mcp-memory-server@latest"],
      "env": { "MNEMOVERSE_API_KEY": "<your-api-key>" }
    }
  }
}
```

### This skill file

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/mnemoverse-memory-mcp ~/.agent-skills/mnemoverse-memory-mcp
```

## Documentation

- Docs: https://mnemoverse.com/docs
- Remote MCP server: https://mnemoverse.com/docs/api/remote-mcp-server
- Pricing, including the free tier: https://mnemoverse.com/pricing
