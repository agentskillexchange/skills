---
title: "Stable Diffusion LoRA Training Pipeline"
description: "Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding. This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development."
source: "https://github.com/Stability-AI/stablediffusion"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Stable Diffusion LoRA Training Pipeline

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding. This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/)
