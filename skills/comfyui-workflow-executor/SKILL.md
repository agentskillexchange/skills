---
name: "ComfyUI Workflow Executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint."
category: "Image & Creative Automation"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/comfyui-workflow-executor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "vault"  # from ase_tool_match
  github_stars: 35266  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/vault"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

## Overview

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a codex
```

### OpenClaw

```bash
clawhub install comfyui-workflow-executor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/comfyui-workflow-executor/
