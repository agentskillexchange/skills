---
title: "Route and observe production agent traffic with Plano"
description: "Use Plano when an agent application needs an out-of-process data plane for multi-agent routing, model agility, guardrails, traces, and OpenAI-compatible traffic instead of custom glue in every service."
verification: "security_reviewed"
source: "https://github.com/katanemo/plano"
author: "Katanemo"
publisher_type: "open_source_project"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "katanemo/plano"
  github_stars: 6604
---

# Route and observe production agent traffic with Plano

Use Plano when an agent application needs an out-of-process data plane for multi-agent routing, model agility, guardrails, traces, and OpenAI-compatible traffic instead of custom glue in every service.

## Prerequisites

Python 3.10+, uv or pip, provider API keys, optional Docker and Docker Compose

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Recommended: uv tool install planoai==0.4.26. Alternative: create a Python virtual environment and run pip install planoai==0.4.26. Then create a Plano config and run planoai up plano_config.yaml.
```

## Documentation

- https://docs.planoai.dev/get_started/quickstart.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-and-observe-production-agent-traffic-with-plano/)
