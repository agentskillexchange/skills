---
title: "Monitor and evaluate LLM agent traffic with Helicone"
description: "Route model calls through Helicone, inspect costs, latency, traces, prompts, and evaluations, then review changes before they ship."
verification: "security_reviewed"
source: "https://github.com/Helicone/helicone"
author: "Helicone"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For the hosted gateway, create a Helicone API key, set the OpenAI client baseURL to https://ai-gateway.helicone.ai, and use HELICONE_API_KEY for authentication. For self-hosting, clone https://github.com/Helicone/helicone, enter the docker directory, copy .env.example to .env, and start services with ./helicone-compose.sh helicone up.
```

## Documentation

- https://docs.helicone.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-and-evaluate-llm-agent-traffic-with-helicone/)
