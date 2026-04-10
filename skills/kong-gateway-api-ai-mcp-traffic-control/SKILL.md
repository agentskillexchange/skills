---
name: "Kong Gateway API AI and MCP Traffic Control"
description: "Kong Gateway is an open-source API gateway that handles routing, authentication, load balancing, observability, and newer AI and MCP traffic patterns. It fits teams that need one control layer in front of services, model providers, or mixed API estates."
verification: security_reviewed
source: "https://github.com/Kong/kong"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
---

# Kong Gateway API AI and MCP Traffic Control

Kong Gateway is an open-source gateway for API, AI, and MCP traffic. Its practical job-to-be-done is to sit in front of services and centralize the hard parts: routing, authentication, authorization, rate limiting, load balancing, health checking, request and response transformation, and operational visibility. Instead of rebuilding those controls inside every service, teams can standardize them at the gateway layer and manage policies from one place.
The upstream project positions Kong as both an API gateway and an AI gateway, with support for RESTful admin APIs, declarative configuration, Kubernetes ingress, and a large plugin ecosystem. The current README also calls out LLM routing across providers such as OpenAI, Anthropic, Gemini, Bedrock, Azure AI, Databricks, Mistral, and Hugging Face, plus MCP governance and observability features. That makes Kong especially relevant for agentic systems that need one enforcement point across conventional APIs and newer model-serving traffic.
Installation paths are documented through Kong's official install pages, and the quick start in the README uses the KONG_DATABASE=postgres docker-compose --profile database up command after cloning the docker-kong repository. Documentation is published at docs.konghq.com, and plugin-development references show how to extend the platform in Lua, Go, or JavaScript. The repository is actively maintained by Kong Inc., has a long release history, and carries an Apache 2.0 license, so it clears ASE's verified-metadata intake gate.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kong-gateway-api-ai-mcp-traffic-control/)
