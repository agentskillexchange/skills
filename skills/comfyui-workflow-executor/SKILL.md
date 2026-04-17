---
title: "ComfyUI Workflow Executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.\nThis skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/comfyui-workflow-executor/"
framework:
  - "Codex"
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.
This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/comfyui-workflow-executor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/comfyui-workflow-executor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/)
