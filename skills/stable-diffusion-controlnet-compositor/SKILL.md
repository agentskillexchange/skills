---
name: "Stable Diffusion ControlNet Compositor"
description: "Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing."
category: "Image & Creative Automation"
framework: "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/"
tool_ecosystem:
  tool: stable.diffusion
---

# Stable Diffusion ControlNet Compositor

Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing.

## Overview

The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control.

The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation.

Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-compositor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-compositor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-compositor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-compositor -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-controlnet-compositor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/
