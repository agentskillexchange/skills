---
name: LobeHub Multi-Agent Chat Platform with MCP Plugin Ecosystem
description: LobeHub is an open-source multi-agent chat platform supporting 50+ LLM
  providers, MCP plugin marketplace, knowledge base management, and multi-agent collaboration.
  It serves as a self-hosted alternative to ChatGPT with extensible function calling
  and voice capabilities.
category: Developer Tools
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/lobehub/lobehub"
tool_ecosystem:
  github_repo: "https://github.com/lobehub/lobehub"
  github_stars: 74751
---
# LobeHub Multi-Agent Chat Platform with MCP Plugin Ecosystem

LobeHub is an open-source multi-agent chat platform supporting 50+ LLM providers, MCP plugin marketplace, knowledge base management, and multi-agent collaboration. It serves as a self-hosted alternative to ChatGPT with extensible function calling and voice capabilities.

Overview

LobeHub (formerly Lobe Chat) is an open-source, high-performance multi-agent chat platform built with TypeScript and Next.js. With over 74,000 GitHub stars, it is one of the most popular open-source AI chat interfaces available. LobeHub supports 50+ LLM providers including OpenAI, Claude, Gemini, DeepSeek, and local models via Ollama, and introduces a multi-agent collaboration framework where agents work as teammates rather than isolated tools.

Multi-Agent Collaboration

LobeHub treats agents as the fundamental unit of work interaction. Users can build personalized AI teams through the Agent Builder, where each agent has its own system prompt, model configuration, tools, and knowledge base. Agents can collaborate on tasks, share context, and hand off work to specialized teammates. The platform includes an Agent Market (similar to GPTs) where users can discover and install pre-built agents.

MCP Plugin Ecosystem

LobeHub features a built-in MCP (Model Context Protocol) marketplace with one-click plugin installation. This allows agents to connect to external tools and data sources including file systems, databases, web browsers, and third-party APIs. The plugin system uses OpenAI-compatible function calling, making it straightforward to extend agent capabilities with custom tools.

Agent Integration Points

AI coding agents can use LobeHub as a front-end interface for interacting with multiple LLM providers through a unified API. The platform supports chain-of-thought reasoning visualization, branching conversations for exploring alternative approaches, and Artifacts support for rendering interactive components. Developers can extend LobeHub with custom plugins and integrate it into existing workflows via its API.

Key Features

- Support for 50+ LLM providers (OpenAI, Claude, Gemini, DeepSeek, Ollama, etc.)

- Multi-agent collaboration with agent teams and handoffs

- MCP plugin marketplace with one-click installation

- Knowledge base with file upload and RAG pipeline

- Vision, TTS, and STT multimodal capabilities

- Text-to-image generation integration

- Branching conversations and chain-of-thought display

- Desktop application support

- Progressive Web App (PWA) with mobile adaptation

- Local and remote database support with multi-user management

- Custom themes and extensive personalization

Deployment

LobeHub can be deployed via Vercel, Docker, or Zeabur. For Docker deployment:

docker run -d -p 3210:3210 lobehub/lobehub

The platform supports both client-side database mode (zero-config, data stored in browser) and server-side database mode (PostgreSQL, for multi-device sync and team use).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lobehub-multi-agent-chat-platform-mcp-plugins
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lobehub-multi-agent-chat-platform-mcp-plugins -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lobehub-multi-agent-chat-platform-mcp-plugins -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lobehub-multi-agent-chat-platform-mcp-plugins -a codex
```

### OpenClaw

```bash
clawhub install lobehub-multi-agent-chat-platform-mcp-plugins
```


## Source

- [GitHub](https://github.com/lobehub/lobehub)
