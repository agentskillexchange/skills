---
title: "OpenAI Agents SDK Multi-Agent Workflow Framework for Python"
description: "The OpenAI Agents SDK is a lightweight Python framework for building multi-agent workflows. It supports 100+ LLMs, provides built-in guardrails, handoffs between agents, MCP tool integration, tracing, sessions, and real-time voice capabilities."
slug: "openai-agents-sdk-python-multi-agent"
category:
  - "Developer Tools"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://github.com/openai/openai-agents-python"
tool_ecosystem:
  github_repo: "openai/openai-agents-python"
  github_stars: 20576
---

# OpenAI Agents SDK Multi-Agent Workflow Framework for Python

The OpenAI Agents SDK is a lightweight Python framework for building multi-agent workflows. It supports 100+ LLMs, provides built-in guardrails, handoffs between agents, MCP tool integration, tracing, sessions, and real-time voice capabilities.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install openai-agents-sdk-python-multi-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The OpenAI Agents SDK (openai-agents) is a lightweight yet powerful framework for building multi-agent workflows in Python. Despite the name, it is provider-agnostic and supports the OpenAI Responses and Chat Completions APIs as well as 100+ other LLMs. It provides a structured, production-ready approach to orchestrating multiple AI agents that collaborate on complex tasks.
Core Concepts
The SDK is built around several key primitives: Agents are LLMs configured with instructions, tools, guardrails, and handoffs. Handoffs enable delegation between agents for specialized tasks. Tools let agents take actions through functions, MCP servers, or hosted tools. Guardrails provide configurable safety checks for input and output validation. Sessions automatically manage conversation history across agent runs.
Key Features
Built-in tracing tracks agent runs for debugging and optimization, viewable in the OpenAI dashboard or exported to external systems. Human-in-the-loop mechanisms allow agents to pause and request human approval. The Agents-as-tools pattern lets agents be invoked as tools by other agents without full handoff. Realtime Agents support enables building voice agents with gpt-realtime models and full agent features including tool calls and handoffs.
MCP Integration
The SDK provides first-class support for Model Context Protocol (MCP) servers. Agents can connect to any MCP server to access tools, making it easy to integrate with databases, APIs, file systems, and other services through the standardized MCP interface. Both stdio and SSE transport modes are supported.
Agent Integration
For agent developers, the SDK provides the most direct path to building multi-agent systems on top of OpenAI models. It integrates naturally with existing Python codebases and supports structured outputs via Pydantic models. The Runner class orchestrates agent execution with synchronous and asynchronous interfaces, streaming support, and automatic context management.
Installation
pip install openai-agents
For voice support: pip install openai-agents[voice]. For Redis sessions: pip install openai-agents[redis]. Requires Python 3.10+ and an OPENAI_API_KEY environment variable.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-agents-sdk-python-multi-agent/)
