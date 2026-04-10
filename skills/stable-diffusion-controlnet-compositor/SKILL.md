---
name: "Stable Diffusion ControlNet Compositor"
description: "Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
