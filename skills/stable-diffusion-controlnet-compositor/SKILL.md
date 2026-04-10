---
title: "Stable Diffusion ControlNet Compositor"
description: "Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing."
slug: "stable-diffusion-controlnet-compositor"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/"
---

# Stable Diffusion ControlNet Compositor

Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing.

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
clawhub install stable-diffusion-controlnet-compositor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control.
The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation.
Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
