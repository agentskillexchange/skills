---
title: "Operate multi-provider AI gateway traffic with Bifrost"
description: "Run Bifrost as an OpenAI-compatible gateway so agents can route model calls across providers with failover, load balancing, caching, and governance."
verification: "security_reviewed"
source: "https://github.com/maximhq/bifrost"
author: "Maxim AI"
publisher_type: "company"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "maximhq/bifrost"
  github_stars: 5969
  npm_package: "@maximhq/bifrost"
  npm_weekly_downloads: 6524
---

# Operate multi-provider AI gateway traffic with Bifrost

Run Bifrost as an OpenAI-compatible gateway so agents can route model calls across providers with failover, load balancing, caching, and governance.

## Prerequisites

Bifrost gateway, provider API keys, and an agent or application stack that can call an OpenAI-compatible chat completions endpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run Bifrost with npx -y @maximhq/bifrost or docker run -p 8080:8080 maximhq/bifrost, open http://localhost:8080 to configure providers and keys, then point the agent runtime at the Bifrost OpenAI-compatible endpoint.
```

## Documentation

- https://docs.getbifrost.ai/quickstart/gateway/setting-up

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-multi-provider-ai-gateway-traffic-with-bifrost/)
