---
name: "Langfuse Prompt Management MCP Server"
slug: "langfuse-prompt-management-mcp-server"
description: "Langfuse Prompt Management MCP Server connects MCP clients to Langfuse prompt libraries so agents can list, retrieve, and compile managed prompts at runtime. It is useful for teams that keep prompts in Langfuse and want assistants to consume production prompt definitions instead of copying templates by hand."
github_stars: 159
verification: "listed"
source: "https://github.com/langfuse/mcp-server-langfuse"
category: "Templates & Workflows"
framework: "MCP"
tool_ecosystem:
  github_repo: "langfuse/mcp-server-langfuse"
  github_stars: 159
---

# Langfuse Prompt Management MCP Server

Langfuse Prompt Management MCP Server connects MCP clients to Langfuse prompt libraries so agents can list, retrieve, and compile managed prompts at runtime. It is useful for teams that keep prompts in Langfuse and want assistants to consume production prompt definitions instead of copying templates by hand.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install
- npm run build
- npx @modelcontextprotocol/inspector node ./build/index.js
- Make sure to replace the environment variables with your actual Langfuse API keys. The server will now be available to use in Claude Desktop.

Requirements and caveats from upstream:
- "command": "node",
- LANGFUSE_PUBLIC_KEY="your-public-key" LANGFUSE_SECRET_KEY="your-secret-key" LANGFUSE_BASEURL="https://cloud.langfuse.com" node absolute-path/build/index.js
- List operations require fetching each prompt individually in the background to extract the arguments, this works but is not efficient

Basic usage or getting-started notes:
- ### Step 1: Build
- bash
- ### Step 2: Add the server to your MCP servers:

- Source: https://github.com/langfuse/mcp-server-langfuse
- Extracted from upstream docs: https://raw.githubusercontent.com/langfuse/mcp-server-langfuse/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langfuse-prompt-management-mcp-server/)
