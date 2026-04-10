---
name: Langfuse Prompt Management MCP Server
description: Langfuse Prompt Management MCP Server connects MCP clients to Langfuse
  prompt libraries so agents can list, retrieve, and compile managed prompts at runtime.
  It is useful for teams that keep prompts in Langfuse and want assistants to consume
  production prompt definitions instead of copying templates by hand.
verification: security_reviewed
source: https://github.com/langfuse/mcp-server-langfuse
category:
- Templates &amp; Workflows
framework:
- MCP
tool_ecosystem:
  github_repo: langfuse/mcp-server-langfuse
  github_stars: 159
---
# Langfuse Prompt Management MCP Server

Langfuse Prompt Management MCP Server is an official Langfuse project that bridges Langfuse prompt management with MCP-compatible clients. The repository focuses on one clear workflow: expose managed prompts from Langfuse so an assistant can discover prompt names, fetch a prompt, and compile it with runtime variables. That makes it valuable for teams using Langfuse as a source of truth for production prompts and prompt templates.
According to the upstream README, the server implements the MCP Prompts specification and also exports tool-based equivalents for clients that do not yet support the prompt capability directly. The documented features include prompts/list, prompts/get, get-prompts, and get-prompt. In practice, that means an agent can query available prompts, inspect required arguments, and render a concrete prompt with variables before handing it off to a model or workflow.
The setup is straightforward but intentionally explicit: you build the Node project, run the compiled server, and provide LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, and LANGFUSE_BASEURL. The README includes configuration examples for Claude Desktop and Cursor. Langfuse also notes current limitations, such as only returning prompts labeled production and assuming prompt variables are optional. This skill is best suited to prompt operations teams and workflow builders who want reusable, centrally managed prompt assets available inside MCP clients instead of duplicating prompt text across multiple agent environments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langfuse-prompt-management-mcp-server/)
