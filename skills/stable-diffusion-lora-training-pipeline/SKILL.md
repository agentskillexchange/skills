---
title: "Stable Diffusion LoRA Training Pipeline"
description: "Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# Stable Diffusion LoRA Training Pipeline

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding.


This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/)
