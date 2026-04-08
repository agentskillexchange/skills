---
title: Stable Diffusion XL Pipeline Builder
description: The Stable Diffusion XL Pipeline Builder creates sophisticated image
  generation workflows using the Hugging Face diffusers library and ComfyUI server
  API. It manages the full SDXL pipeline including base model inference, refiner pass,
  and VAE decoding stages. The skill supports dynamic LoRA adapter loading with configurable
  weight merging, allowing multiple style and concept LoRAs to be combined in a single
  generation. ControlNet conditioning supports depth maps, canny edges, pose estimation,
  and segmentation masks for precise image composition control. Batch prompt scheduling
  enables automated generation runs with parameter sweeps across guidance scale, sampling
  steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent
  manages VRAM efficiently by offloading models to CPU when switching between pipeline
  configurations. ComfyUI integration provides node-based workflow construction via
  the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and
  InstantID. Generated images include full metadata embedding with generation parameters
  for reproducibility. The skill handles SDXL turbo and lightning variants for real-time
  generation use cases.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/
category:
- Image &amp; Creative Automation
framework:
- Cursor
---

# Stable Diffusion XL Pipeline Builder

The Stable Diffusion XL Pipeline Builder creates sophisticated image generation workflows using the Hugging Face diffusers library and ComfyUI server API. It manages the full SDXL pipeline including base model inference, refiner pass, and VAE decoding stages. The skill supports dynamic LoRA adapter loading with configurable weight merging, allowing multiple style and concept LoRAs to be combined in a single generation. ControlNet conditioning supports depth maps, canny edges, pose estimation, and segmentation masks for precise image composition control. Batch prompt scheduling enables automated generation runs with parameter sweeps across guidance scale, sampling steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent manages VRAM efficiently by offloading models to CPU when switching between pipeline configurations. ComfyUI integration provides node-based workflow construction via the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and InstantID. Generated images include full metadata embedding with generation parameters for reproducibility. The skill handles SDXL turbo and lightning variants for real-time generation use cases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
