---
name: ComfyUI Workflow Executor
description: Executes ComfyUI image generation workflows via the /prompt REST API
  endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler
  scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval
  from the /view endpoint.
verification: security_reviewed
source: https://agentskillexchange.com/skills/comfyui-workflow-executor/
category:
- Image &amp; Creative Automation
framework:
- Codex
---
# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.
This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/)
