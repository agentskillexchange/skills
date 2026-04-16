---
title: "Stable Diffusion ControlNet Compositor"
description: "Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
---

# Stable Diffusion ControlNet Compositor

The Stable Diffusion ControlNet Compositor automates guided image generation using SDXL and ControlNet adapters through both the Automatic1111 REST API and ComfyUI workflow engine. It manages multi-ControlNet conditioning by stacking Canny edge detection, MiDaS depth estimation, and OpenPose skeleton extraction for precise compositional control.

The skill handles prompt engineering with emphasis weighting syntax, CLIP skip configuration, and negative prompt templates optimized for photorealistic and artistic styles. It supports LoRA model loading with adjustable weights, textual inversion embeddings, and IP-Adapter for image-prompted generation.

Batch processing capabilities include grid generation for prompt comparison, upscaling pipelines via ESRGAN and SwinIR, and face restoration with CodeFormer. ComfyUI workflows are exported as portable JSON for reproducibility, and the skill manages VRAM optimization through model offloading, attention slicing, and tiled VAE decoding for high-resolution outputs on consumer GPUs. Seed management ensures reproducible results across generation sessions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
