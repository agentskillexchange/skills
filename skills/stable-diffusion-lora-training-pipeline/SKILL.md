---
name: "Stable Diffusion LoRA Training Pipeline"
description: "Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Stable Diffusion LoRA Training Pipeline

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding.
This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/)
