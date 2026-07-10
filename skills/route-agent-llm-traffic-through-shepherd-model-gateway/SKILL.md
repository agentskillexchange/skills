---
name: "Route agent LLM traffic through Shepherd Model Gateway"
slug: "route-agent-llm-traffic-through-shepherd-model-gateway"
description: "Use Shepherd Model Gateway to route OpenAI, Anthropic, Responses API, embeddings, and MCP tool traffic across self-hosted and cloud model backends with cache-aware policies and observability."
github_stars: 380
verification: "security_reviewed"
source: "https://github.com/lightseekorg/smg"
author: "LightSeek contributors"
publisher_type: "open_source"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "lightseekorg/smg"
  github_stars: 380
---

# Route agent LLM traffic through Shepherd Model Gateway

Use Shepherd Model Gateway to route OpenAI, Anthropic, Responses API, embeddings, and MCP tool traffic across self-hosted and cloud model backends with cache-aware policies and observability.

## Prerequisites

SMG binary, Docker image, Python package, or Rust install; one or more model worker endpoints; agent runtime configured to call the gateway; optional Prometheus/OpenTelemetry stack

## Installation

Use the upstream install or setup path that matches your environment:
- docker pull lightseekorg/smg:latest
- pip install smg
- cargo install smg

Requirements and caveats from upstream:
- <a href="https://github.com/orgs/lightseekorg/packages/container/package/smg"><img src="https://img.shields.io/badge/ghcr.io-lightseekorg%2Fsmg-blue?logo=docker" alt="Docker"></a>
- | **[High Availability](docs/concepts/architecture/high-availability.md)** | Mesh networking with SWIM protocol for multi-node deployments |

Basic usage or getting-started notes:
- **Install** — pick your preferred method:
- **Run** — point SMG at your inference workers:
- smg launch --worker-urls http://localhost:8000

- Source: https://github.com/lightseekorg/smg
- Extracted from upstream docs: https://raw.githubusercontent.com/lightseekorg/smg/HEAD/README.md

## Documentation

- https://lightseekorg.github.io/smg

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-agent-llm-traffic-through-shepherd-model-gateway/)
