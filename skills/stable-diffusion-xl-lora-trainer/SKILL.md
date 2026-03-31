---
name: "Stable Diffusion XL LoRA Trainer"
description: "Fine-tune Stable Diffusion XL models with LoRA adapters using the diffusers library and Kohya-ss training scripts. Manages dataset preparation, training configuration, and checkpoint merging for custom image generation."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/"
---
# Stable Diffusion XL LoRA Trainer

Fine-tune Stable Diffusion XL models with LoRA adapters using the diffusers library and Kohya-ss training scripts. Manages dataset preparation, training configuration, and checkpoint merging for custom image generation.

## Overview

Train custom LoRA (Low-Rank Adaptation) adapters for Stable Diffusion XL to generate images in specific styles or with specific subjects. This skill automates the full training pipeline from dataset curation through model export.

Dataset preparation includes automatic image resizing, aspect ratio bucketing, and caption generation using BLIP-2 or WD14 tagger models. Training images are organized with text file captions following the Kohya-ss naming convention.

Training configuration supports key hyperparameters including rank (4-128), alpha, learning rate scheduling (cosine, constant with warmup), optimizer selection (AdamW8bit, Prodigy, DAdaptation), and mixed precision (fp16/bf16). The training loop uses the diffusers library with xformers memory optimization and gradient checkpointing for reduced VRAM usage.

Checkpoint management handles saving intermediate epochs, merging multiple LoRA weights with configurable merge ratios, and exporting to safetensors format. The skill can invoke the AUTOMATIC1111 or ComfyUI API to generate test images at configurable intervals during training for visual quality monitoring.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-lora-trainer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-lora-trainer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-lora-trainer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-lora-trainer -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-xl-lora-trainer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/)
