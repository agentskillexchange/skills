---
name: "Hugging Face Model Deployer"
description: "Deploys models from Hugging Face Hub to Inference Endpoints using the huggingface_hub client and REST API. Monitors endpoint health and autoscaling status and streams logs to the terminal. Supports private repos with HF_TOKEN and custom Docker containers."
category: "CI/CD Integrations"
framework: "Codex"
verification: listed  # security_reviewed or listed
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

Deploys models from Hugging Face Hub to Inference Endpoints using the huggingface_hub client and REST API. Monitors endpoint health and autoscaling status and streams logs to the terminal. Supports private repos with HF_TOKEN and custom Docker containers.

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
