---
name: "Monitor and evaluate LLM agent traffic with Helicone"
slug: "monitor-and-evaluate-llm-agent-traffic-with-helicone"
description: "Route model calls through Helicone, inspect costs, latency, traces, prompts, and evaluations, then review changes before they ship."
github_stars: 5779
verification: "security_reviewed"
source: "https://github.com/Helicone/helicone"
author: "Helicone"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Helicone/helicone"
  github_stars: 5779
  npm_package: "helicone"
  npm_weekly_downloads: 49
---

# Monitor and evaluate LLM agent traffic with Helicone

Route model calls through Helicone, inspect costs, latency, traces, prompts, and evaluations, then review changes before they ship.

## Prerequisites

Helicone account or self-hosted Helicone deployment, LLM application or agent using an OpenAI-compatible client, configured HELICONE_API_KEY or self-hosted environment.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/Helicone/helicone.git
- Manual deployment is not recommended. Please use Docker or Helm. If you must, follow the instructions [here](https://docs.helicone.ai/getting-started/self-deploy).

Requirements and caveats from upstream:
- Helicone is simple to self-host and update. To get started locally, just use our [docker-compose](https://docs.helicone.ai/getting-started/self-deploy-docker) file.
- cd docker
- | AI Gateway | [JS/TS, Python, cURL](https://docs.helicone.ai/gateway/overview) | Unified API for 100+ providers with intelligent routing, automatic fallbacks, and unified observability

Basic usage or getting-started notes:
- Get your API key by signing up [here](https://helicone.ai/signup) and add credits at [helicone.ai/credits](https://us.helicone.ai/credits)
- Update the baseURL in your code and add your API key.
- typescript

- Source: https://github.com/Helicone/helicone
- Extracted from upstream docs: https://raw.githubusercontent.com/Helicone/helicone/HEAD/README.md

## Documentation

- https://docs.helicone.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-and-evaluate-llm-agent-traffic-with-helicone/)
