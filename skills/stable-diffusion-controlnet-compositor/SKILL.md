---
title: Stable Diffusion ControlNet Compositor
description: The Stable Diffusion ControlNet Compositor automates guided image generation
  using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI
  workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge
  detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise
  compositional control. The skill handles prompt engineering with emphasis weighting
  syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic
  and artistic styles. It supports LoRA model loading with adjustable weights, textual
  inversion embeddings, and IP-Adapter for image-prompted generation. Batch processing
  capabilities include grid generation for prompt comparison, upscaling pipelines
  via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are
  exported as portable JSON for reproducibility, and the skill manages VRAM optimization
  through model offloading, attention slicing, and tiled VAE decoding for high-resolution
  outputs on consumer GPUs. Seed management ensures reproducible results across generation
  sessions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/
category:
- Image &amp; Creative Automation
framework:
- Gemini
---

# Stable Diffusion ControlNet Compositor

The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control. The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation. Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
