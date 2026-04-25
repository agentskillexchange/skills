---
title: "Stable Diffusion XL Pipeline Builder"
description: "Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
---

# Stable Diffusion XL Pipeline Builder

The Stable Diffusion XL Pipeline Builder creates sophisticated image generation workflows using the Hugging Face diffusers library and ComfyUI server API. It manages the full SDXL pipeline including base model inference, refiner pass, and VAE decoding stages. The skill supports dynamic LoRA adapter loading with configurable weight merging, allowing multiple style and concept LoRAs to be combined in a single generation. ControlNet conditioning supports depth maps, canny edges, pose estimation, and segmentation masks for precise image composition control. Batch prompt scheduling enables automated generation runs with parameter sweeps across guidance scale, sampling steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent manages VRAM efficiently by offloading models to CPU when switching between pipeline configurations. ComfyUI integration provides node-based workflow construction via the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and InstantID. Generated images include full metadata embedding with generation parameters for reproducibility. The skill handles SDXL turbo and lightning variants for real-time generation use cases.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stable-diffusion-xl-pipeline-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stable-diffusion-xl-pipeline-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
