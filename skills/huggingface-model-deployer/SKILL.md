---
name: "Hugging Face Model Deployer"
description: "Deploys models from Hugging Face Hub to Inference Endpoints using the huggingface_hub client and REST API. Monitors endpoint health and autoscaling status and streams logs to the terminal. Supports private repos with HF_TOKEN and custom Docker containers."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/huggingface-model-deployer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Hugging Face Model Deployer

Deploys models from Hugging Face Hub to Inference Endpoints using the huggingface_hub client and REST API. Monitors endpoint health and autoscaling status and streams logs to the terminal. Supports private repos with HF_TOKEN and custom Docker containers.

## Overview

**Hugging Face Model Deployer** is built around Docker container platform. The underlying ecosystem is represented by `moby/moby` (71,560+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Docker Engine API, Dockerfiles, docker compose, image builds, registries and preserving the operational context that matters for real tasks.

In deployment workflows, the skill acts as a control layer around docker operations so an agent can inspect current state, compute a diff, surface rollout risk, and only then trigger the change path. The original use case is clear: Deploys models from Hugging Face Hub to Inference Endpoints using the huggingface_hub client and REST API. Monitors endpoint health and autoscaling status and streams logs to the terminal. Supports private repos with HF_TOKEN and custom Docker containers. The implementation typically relies on Docker Engine API, Dockerfiles, docker compose, image builds, registries, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses Docker Engine API, Dockerfiles, docker compose, image builds, registries instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as local dev, packaging, runtime isolation, and deployment pipelines.

Key integration points include local dev, packaging, runtime isolation, and deployment pipelines. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill huggingface-model-deployer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill huggingface-model-deployer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill huggingface-model-deployer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill huggingface-model-deployer -a codex
```

### OpenClaw

```bash
clawhub install huggingface-model-deployer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/huggingface-model-deployer/
