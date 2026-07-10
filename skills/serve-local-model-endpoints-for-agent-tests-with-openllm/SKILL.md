---
title: "Serve local model endpoints for agent tests with OpenLLM"
description: "Launch an OpenAI-compatible OpenLLM server for a chosen open model, point an agent runtime at it, and compare behavior before production use."
verification: "security_reviewed"
source: "https://github.com/bentoml/OpenLLM"
author: "BentoML"
publisher_type: "open-source organization"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bentoml/OpenLLM"
  github_stars: 12346
  npm_package: "openllm"
  npm_weekly_downloads: 6
---

# Serve local model endpoints for agent tests with OpenLLM

Launch an OpenAI-compatible OpenLLM server for a chosen open model, point an agent runtime at it, and compare behavior before production use.

## Prerequisites

OpenLLM, Python environment, supported open model, required GPU/CPU resources, Hugging Face token for gated models, agent runtime or SDK that can call an OpenAI-compatible endpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install openllm`, run `openllm hello` to verify the CLI, then start a server such as `openllm serve llama3.2:1b`. The server exposes OpenAI-compatible APIs at `http://localhost:3000`; point compatible clients at `http://localhost:3000/v1` with a placeholder local API key.
```

## Documentation

- https://github.com/bentoml/OpenLLM

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serve-local-model-endpoints-for-agent-tests-with-openllm/)
