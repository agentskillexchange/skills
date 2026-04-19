---
title: "Stable Diffusion XL LoRA Trainer"
description: "Train custom LoRA (Low-Rank Adaptation) adapters for Stable Diffusion XL to generate images in specific styles or with specific subjects. This skill automates the full training pipeline from dataset curation through model export. Dataset preparation includes automatic image resizing, aspect ratio bucketing, and caption generation using BLIP-2 or WD14 tagger models. Training images are organized with text file captions following the Kohya-ss naming convention. Training configuration supports key hyperparameters including rank (4-128), alpha, learning rate scheduling (cosine, constant with warmup), optimizer selection (AdamW8bit, Prodigy, DAdaptation), and mixed precision (fp16/bf16). The training loop uses the diffusers library with xformers memory optimization and gradient checkpointing for reduced VRAM usage. Checkpoint management handles saving intermediate epochs, merging multiple LoRA weights with configurable merge ratios, and exporting to safetensors format. The skill can invoke the AUTOMATIC1111 or ComfyUI API to generate test images at configurable intervals during training for visual quality monitoring."
source: "https://github.com/Stability-AI/stablediffusion"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Stable Diffusion XL LoRA Trainer

Train custom LoRA (Low-Rank Adaptation) adapters for Stable Diffusion XL to generate images in specific styles or with specific subjects. This skill automates the full training pipeline from dataset curation through model export. Dataset preparation includes automatic image resizing, aspect ratio bucketing, and caption generation using BLIP-2 or WD14 tagger models. Training images are organized with text file captions following the Kohya-ss naming convention. Training configuration supports key hyperparameters including rank (4-128), alpha, learning rate scheduling (cosine, constant with warmup), optimizer selection (AdamW8bit, Prodigy, DAdaptation), and mixed precision (fp16/bf16). The training loop uses the diffusers library with xformers memory optimization and gradient checkpointing for reduced VRAM usage. Checkpoint management handles saving intermediate epochs, merging multiple LoRA weights with configurable merge ratios, and exporting to safetensors format. The skill can invoke the AUTOMATIC1111 or ComfyUI API to generate test images at configurable intervals during training for visual quality monitoring.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/)
