---
title: "Stable Diffusion XL LoRA Trainer"
description: "Fine-tune Stable Diffusion XL models with LoRA adapters using the diffusers library and Kohya-ss training scripts. Manages dataset preparation, training configuration, and checkpoint merging for custom image generation."
slug: "stable-diffusion-xl-lora-trainer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/"
---

# Stable Diffusion XL LoRA Trainer

Fine-tune Stable Diffusion XL models with LoRA adapters using the diffusers library and Kohya-ss training scripts. Manages dataset preparation, training configuration, and checkpoint merging for custom image generation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install stable-diffusion-xl-lora-trainer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Train custom LoRA (Low-Rank Adaptation) adapters for Stable Diffusion XL to generate images in specific styles or with specific subjects. This skill automates the full training pipeline from dataset curation through model export.
Dataset preparation includes automatic image resizing, aspect ratio bucketing, and caption generation using BLIP-2 or WD14 tagger models. Training images are organized with text file captions following the Kohya-ss naming convention.
Training configuration supports key hyperparameters including rank (4-128), alpha, learning rate scheduling (cosine, constant with warmup), optimizer selection (AdamW8bit, Prodigy, DAdaptation), and mixed precision (fp16/bf16). The training loop uses the diffusers library with xformers memory optimization and gradient checkpointing for reduced VRAM usage.
Checkpoint management handles saving intermediate epochs, merging multiple LoRA weights with configurable merge ratios, and exporting to safetensors format. The skill can invoke the AUTOMATIC1111 or ComfyUI API to generate test images at configurable intervals during training for visual quality monitoring.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/)
