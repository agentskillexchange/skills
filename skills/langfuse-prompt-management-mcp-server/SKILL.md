---
name: "Langfuse Prompt Management MCP Server"
slug: "langfuse-prompt-management-mcp-server"
description: "Langfuse Prompt Management MCP Server connects MCP clients to Langfuse prompt libraries so agents can list, retrieve, and compile managed prompts at runtime. It is useful for teams that keep prompts in Langfuse and want assistants to consume production prompt definitions instead of copying templates by hand."
github_stars: 159
verification: "security_reviewed"
source: "https://github.com/langfuse/mcp-server-langfuse"
author: "langfuse"
category: "Templates & Workflows"
framework: "MCP"
tool_ecosystem:
  github_repo: "langfuse/mcp-server-langfuse"
  github_stars: 159
---

# Langfuse Prompt Management MCP Server

Langfuse Prompt Management MCP Server connects MCP clients to Langfuse prompt libraries so agents can list, retrieve, and compile managed prompts at runtime. It is useful for teams that keep prompts in Langfuse and want assistants to consume production prompt definitions instead of copying templates by hand.

## Installation

Install or set up from the source-backed instructions:

From a checkout of langfuse/mcp-server-langfuse:
npm install
npm run build
Configure your MCP client to run node <absolute-path>/build/index.js with LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY and LANGFUSE_BASEURL.

- Source: https://github.com/langfuse/mcp-server-langfuse

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langfuse-prompt-management-mcp-server/)
