---
title: "LiteLLM Unified LLM Gateway and Proxy Server"
description: "LiteLLM is an open-source Python SDK and proxy server that provides a unified OpenAI-compatible interface to call 100+ LLM APIs including OpenAI, Anthropic, Azure, Bedrock, and more. It includes cost tracking, guardrails, load balancing, and virtual key management for production deployments."
slug: "litellm-unified-llm-gateway-proxy"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/BerriAI/litellm"
tool_ecosystem:
  github_repo: "BerriAI/litellm"
  github_stars: 41815
listed: true
---

# LiteLLM Unified LLM Gateway and Proxy Server

LiteLLM is an open-source Python SDK and proxy server that provides a unified OpenAI-compatible interface to call 100+ LLM APIs including OpenAI, Anthropic, Azure, Bedrock, and more. It includes cost tracking, guardrails, load balancing, and virtual key management for production deployments.

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
clawhub install litellm-unified-llm-gateway-proxy
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

LiteLLM is a Python SDK and AI Gateway proxy server developed by BerriAI (YC-backed) that solves the multi-provider LLM integration problem. Available at github.com/BerriAI/litellm with 20,000+ GitHub stars, it lets developers call over 100 different LLM APIs through a single, unified OpenAI-compatible interface.
The fundamental value of LiteLLM is abstraction. Instead of writing separate integration code for OpenAI, Anthropic, Google VertexAI, AWS Bedrock, Azure, Cohere, HuggingFace, and dozens of other providers, developers write one completion call and swap the model string. LiteLLM handles the translation between provider-specific API formats, authentication methods, and response schemas automatically.
The proxy server component turns LiteLLM into a production-grade AI gateway. Teams deploy it as a centralized endpoint that all their applications call. It provides virtual API keys with per-key budget limits and rate limiting, automatic load balancing across multiple model deployments, cost tracking and spend analytics per key/user/team, guardrails and content filtering, and detailed request/response logging. This makes it practical for organizations running multiple AI-powered applications that need centralized control over LLM usage and spending.
A skill wrapping LiteLLM gives an AI agent the ability to route requests to the optimal model for each task. The agent could use cheaper models for simple tasks and premium models for complex reasoning, all through the same interface. The proxy supports /chat/completions, /embeddings, /images, /audio, /batches, /rerank, and the new /a2a agent-to-agent protocol.
Installation requires just pip install litellm for the SDK or pip install litellm[proxy] for the gateway server. LiteLLM is MIT-licensed with active daily releases and comprehensive documentation at docs.litellm.ai.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/litellm-unified-llm-gateway-proxy/)
