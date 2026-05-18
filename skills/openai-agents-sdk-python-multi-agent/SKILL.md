---
name: "OpenAI Agents SDK Multi-Agent Workflow Framework for Python"
slug: "openai-agents-sdk-python-multi-agent"
description: "The OpenAI Agents SDK is a lightweight Python framework for building multi-agent workflows. It supports 100+ LLMs, provides built-in guardrails, handoffs between agents, MCP tool integration, tracing, sessions, and real-time voice capabilities."
github_stars: 20576
verification: "security_reviewed"
source: "https://github.com/openai/openai-agents-python"
category: "Developer Tools"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-agents-python"
  github_stars: 20576
---

# OpenAI Agents SDK Multi-Agent Workflow Framework for Python

The OpenAI Agents SDK is a lightweight Python framework for building multi-agent workflows. It supports 100+ LLMs, provides built-in guardrails, handoffs between agents, MCP tool integration, tracing, sessions, and real-time voice capabilities.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install openai-agents
- uv init
- uv add openai-agents

Requirements and caveats from upstream:
- [**Agents**](https://openai.github.io/openai-agents-python/agents): LLMs configured with instructions, tools, guardrails, and handoffs
- [**Sandbox Agents**](https://openai.github.io/openai-agents-python/sandbox_agents): Agents preconfigured to work with a container to perform work over long time horizons.
- **[Agents as tools](https://openai.github.io/openai-agents-python/tools/#agents-as-tools) / [Handoffs](https://openai.github.io/openai-agents-python/handoffs/)**: Delegating to other agents for specific tasks

Basic usage or getting-started notes:
- ## Run your first Sandbox Agent
- from agents.run import RunConfig
- # Run this agent on the local filesystem

- Source: https://github.com/openai/openai-agents-python
- Extracted from upstream docs: https://raw.githubusercontent.com/openai/openai-agents-python/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-agents-sdk-python-multi-agent/)
