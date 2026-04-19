---
title: "Stable Diffusion ControlNet Compositor"
description: "The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control. The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation. Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions."
source: "https://github.com/Stability-AI/stablediffusion"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
---

# Stable Diffusion ControlNet Compositor

The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control. The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation. Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
