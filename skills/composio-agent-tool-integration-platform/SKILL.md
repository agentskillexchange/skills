---
name: "Composio Agent Tool Integration Platform"
description: "Composio provides 1000+ pre-built toolkits with managed authentication, context management, and sandboxed execution to connect AI agents to external apps like Gmail, Slack, GitHub, and Notion. Available as Python and TypeScript SDKs with support for major agent frameworks."
category: "Integrations & Connectors"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/ComposioHQ/composio"
---
# Composio Agent Tool Integration Platform

Composio provides 1000+ pre-built toolkits with managed authentication, context management, and sandboxed execution to connect AI agents to external apps like Gmail, Slack, GitHub, and Notion. Available as Python and TypeScript SDKs with support for major agent frameworks.

## Overview

What is Composio?

Composio is an open-source platform with over 27,000 GitHub stars that powers tool integration for AI agents. It provides SDKs in Python and TypeScript that connect agents built with OpenAI, Anthropic, LangChain, CrewAI, Vercel AI SDK, Google Gemini, and other frameworks to over 500 external applications through managed authentication and pre-built toolkits.

How the Skill Works

A Composio integration skill enables agents to call external APIs without writing custom integration code. The skill initializes the Composio client, authenticates users via OAuth or API keys managed by Composio’s auth infrastructure, and exposes toolkit functions as callable tools. When an agent needs to send a Slack message, create a GitHub issue, or query a database, Composio handles the API call, authentication refresh, error handling, and response formatting.

The platform includes a sandboxed workbench for safe tool execution, preventing agents from making unintended side effects. Tool search capabilities let agents discover relevant tools at runtime based on natural language descriptions, and context management ensures agents receive only the most relevant tool definitions for their current task.

Integration Points

Composio supports direct integration with OpenAI Agents SDK, Anthropic Claude, LangChain, LlamaIndex, CrewAI, AutoGen, Vercel AI SDK, Google ADK, Mastra, and Cloudflare Workers AI. The npm package @composio/core and PyPI package composio provide the core SDK, with framework-specific packages like @composio/openai-agents for seamless integration. Custom providers can be built for any AI framework not yet supported.

What It Outputs

The skill outputs structured tool call results from external APIs, formatted for consumption by the calling agent framework. It provides authentication status, tool execution logs, and error diagnostics. The platform also outputs tool discovery results when agents search for capabilities dynamically.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill composio-agent-tool-integration-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill composio-agent-tool-integration-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill composio-agent-tool-integration-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill composio-agent-tool-integration-platform -a codex
```

### OpenClaw

```bash
clawhub install composio-agent-tool-integration-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/composio-agent-tool-integration-platform/)
