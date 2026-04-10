---
name: Stable Diffusion XL LoRA Trainer
description: Fine-tune Stable Diffusion XL models with LoRA adapters using the diffusers
  library and Kohya-ss training scripts. Manages dataset preparation, training configuration,
  and checkpoint merging for custom image generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/
category:
- Image &amp; Creative Automation
framework:
- Custom Agents
---
# Stable Diffusion XL LoRA Trainer

Train custom LoRA (Low-Rank Adaptation) adapters for Stable Diffusion XL to generate images in specific styles or with specific subjects. This skill automates the full training pipeline from dataset curation through model export.
Dataset preparation includes automatic image resizing, aspect ratio bucketing, and caption generation using BLIP-2 or WD14 tagger models. Training images are organized with text file captions following the Kohya-ss naming convention.
Training configuration supports key hyperparameters including rank (4-128), alpha, learning rate scheduling (cosine, constant with warmup), optimizer selection (AdamW8bit, Prodigy, DAdaptation), and mixed precision (fp16/bf16). The training loop uses the diffusers library with xformers memory optimization and gradient checkpointing for reduced VRAM usage.
Checkpoint management handles saving intermediate epochs, merging multiple LoRA weights with configurable merge ratios, and exporting to safetensors format. The skill can invoke the AUTOMATIC1111 or ComfyUI API to generate test images at configurable intervals during training for visual quality monitoring.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-lora-trainer/)
