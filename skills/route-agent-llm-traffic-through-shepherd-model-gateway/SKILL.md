---
title: "Route agent LLM traffic through Shepherd Model Gateway"
description: "Use Shepherd Model Gateway to route OpenAI, Anthropic, Responses API, embeddings, and MCP tool traffic across self-hosted and cloud model backends with cache-aware policies and observability."
verification: "security_reviewed"
source: "https://github.com/lightseekorg/smg"
author: "LightSeek contributors"
publisher_type: "open_source"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "lightseekorg/smg"
  github_stars: 380
---

# Route agent LLM traffic through Shepherd Model Gateway

Use Shepherd Model Gateway to route OpenAI, Anthropic, Responses API, embeddings, and MCP tool traffic across self-hosted and cloud model backends with cache-aware policies and observability.

## Prerequisites

SMG binary, Docker image, Python package, or Rust install; one or more model worker endpoints; agent runtime configured to call the gateway; optional Prometheus/OpenTelemetry stack

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with docker pull lightseekorg/smg:latest, pip install smg, or cargo install smg. Start with smg launch --worker-urls http://localhost:8000, add additional worker URLs or --policy cache_aware as needed, then point OpenAI-compatible agent clients at the gateway endpoint.
```

## Documentation

- https://lightseekorg.github.io/smg

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-agent-llm-traffic-through-shepherd-model-gateway/)
