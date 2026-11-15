---
name: "Deploy a private local agent stack with Self-Hosted AI Stack"
slug: "deploy-private-local-agent-stack-with-self-hosted-ai-stack"
description: "Stand up a local-first Docker Compose backend for agent work: LLM routing, chat, document parsing, embeddings, speech, and MCP tools."
github_stars: 163
verification: "security_reviewed"
source: "https://github.com/hwdsl2/self-hosted-ai-stack"
author: "hwdsl2"
publisher_type: "GitHub repository"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hwdsl2/self-hosted-ai-stack"
  github_stars: 163
---

# Deploy a private local agent stack with Self-Hosted AI Stack

Stand up a local-first Docker Compose backend for agent work: LLM routing, chat, document parsing, embeddings, speech, and MCP tools.

## Prerequisites

Docker, Docker Compose, Ollama/InferCrate, GatewayCrate/LiteLLM, ToolUplink/MCPHub, AnythingLLM

## Installation

Install or set up from the source-backed instructions:

git clone https://github.com/hwdsl2/self-hosted-ai-stack && cd self-hosted-ai-stack && docker compose up -d && docker exec ollama ollama_manage --pull llama3.2:3b && ./stack-check.sh

- Source: https://github.com/hwdsl2/self-hosted-ai-stack

## Documentation

- https://selfhostedaistack.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-private-local-agent-stack-with-self-hosted-ai-stack/)
