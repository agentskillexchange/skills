---
name: "Stable Diffusion LoRA Training Pipeline"
description: "Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/"
---
# Stable Diffusion LoRA Training Pipeline

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding.

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding.



This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-lora-training-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-lora-training-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-lora-training-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-lora-training-pipeline -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-lora-training-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/)
