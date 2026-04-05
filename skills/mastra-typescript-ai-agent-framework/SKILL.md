---
name: "Mastra TypeScript AI Agent Framework"
description: "Mastra is an open-source TypeScript framework for building AI-powered applications and agents. Created by the team behind Gatsby, it provides model routing across 40+ providers, graph-based workflows, human-in-the-loop suspension, and MCP server authoring in a single cohesive package."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/mastra-ai/mastra"
tool_ecosystem:
  github_repo: "mastra-ai/mastra"
  github_stars: 22557
  npm_package: "mastra"
  npm_weekly_downloads: 276083
---
# Mastra TypeScript AI Agent Framework

Mastra is an open-source TypeScript framework for building AI-powered applications and agents. Created by the team behind Gatsby, it provides model routing across 40+ providers, graph-based workflows, human-in-the-loop suspension, and MCP server authoring in a single cohesive package.

What is Mastra? Mastra is a TypeScript-first framework for building production-ready AI applications and autonomous agents. Developed by the same team that created Gatsby, Mastra connects to over 40 LLM providers through a unified interface, including OpenAI, Anthropic, Google Gemini, and open-source models. It provides agents, workflows, memory management, RAG (retrieval-augmented generation), evaluation, and observability out of the box.

The framework is designed to go from prototype to production without switching tools. You can embed Mastra into existing React, Next.js, or Node.js applications, or deploy it as a standalone server. It also supports authoring MCP (Model Context Protocol) servers, exposing agents and tools to any MCP-compatible client.

Core Capabilities Mastra’s agent system lets you build autonomous units that use LLMs and tools to solve open-ended tasks. Agents reason about goals, decide which tools to use, and iterate until they produce a final answer. For deterministic control, the graph-based workflow engine uses an intuitive syntax with .then(), .branch(), and .parallel() operators for complex multi-step orchestration.

The human-in-the-loop feature suspends an agent or workflow mid-execution and awaits user input or approval before resuming. Execution state is persisted to storage, allowing indefinite pauses. Context management includes conversation history, semantic memory, working memory, and RAG retrieval from APIs, databases, and files.

Output and Integration Install with npm create mastra@latest and follow the CLI wizard to scaffold a project. Mastra integrates with Vercel’s AI SDK UI and CopilotKit for frontend experiences. Built-in evals measure agent quality, and observability hooks connect to your existing monitoring stack. The framework is Apache-2.0 licensed with over 22,000 GitHub stars, published on npm as @mastra/core, and backed by Y Combinator (W25 batch).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mastra-typescript-ai-agent-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mastra-typescript-ai-agent-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mastra-typescript-ai-agent-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mastra-typescript-ai-agent-framework -a codex
```

### OpenClaw

```bash
clawhub install mastra-typescript-ai-agent-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mastra-typescript-ai-agent-framework/)
