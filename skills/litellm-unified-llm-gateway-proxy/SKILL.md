---
name: "LiteLLM Unified LLM Gateway and Proxy Server"
slug: "litellm-unified-llm-gateway-proxy"
description: "LiteLLM is an open-source Python SDK and proxy server that provides a unified OpenAI-compatible interface to call 100+ LLM APIs including OpenAI, Anthropic, Azure, Bedrock, and more. It includes cost tracking, guardrails, load balancing, and virtual key management for production deployments."
github_stars: 41815
verification: "security_reviewed"
source: "https://github.com/BerriAI/litellm"
category: "Integrations & Connectors"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "BerriAI/litellm"
  github_stars: 41815
---

# LiteLLM Unified LLM Gateway and Proxy Server

LiteLLM is an open-source Python SDK and proxy server that provides a unified OpenAI-compatible interface to call 100+ LLM APIs including OpenAI, Anthropic, Azure, Bedrock, and more. It includes cost tracking, guardrails, load balancing, and virtual key management for production deployments.

## Installation

Use the upstream install or setup path that matches your environment:
- **Stable Release:** Use docker images with the -stable tag. These have undergone 12 hour load tests, before being published. [More information about the release cycle here](https://docs.litellm.ai/docs/proxy/release_c...
- Run npm run dev to start the dashboard

Requirements and caveats from upstream:
- You can use LiteLLM through either the Proxy Server or Python SDK. Both give you a unified interface to access multiple LLMs (100+ LLMs). Choose the option that best fits your needs:
- <th style={{width: '43%'}}><strong><a href="https://docs.litellm.ai/docs/">LiteLLM Python SDK</a></strong></th>
- <td style={{width: '43%'}}>Use LiteLLM directly in your Python code</td>

Basic usage or getting-started notes:
- ### Run in Developer Mode
- uv run prisma generate

- Source: https://github.com/BerriAI/litellm
- Extracted from upstream docs: https://raw.githubusercontent.com/BerriAI/litellm/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/litellm-unified-llm-gateway-proxy/)
