---
title: "ComfyUI Workflow Executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint."
verification: "security_reviewed"
source: "https://github.com/Comfy-Org/ComfyUI"
category:
  - "Image & Creative Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "Comfy-Org/ComfyUI"
  github_stars: 109121
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/comfyui-workflow-executor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/comfyui-workflow-executor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/comfyui-workflow-executor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/)
