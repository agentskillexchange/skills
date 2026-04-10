---
title: "Stable Diffusion XL Pipeline Builder"
description: "Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling."
slug: "stable-diffusion-xl-pipeline-builder"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/"
---

# Stable Diffusion XL Pipeline Builder

Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling.

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
clawhub install stable-diffusion-xl-pipeline-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion XL Pipeline Builder creates sophisticated image generation workflows using the Hugging Face diffusers library and ComfyUI server API. It manages the full SDXL pipeline including base model inference, refiner pass, and VAE decoding stages.
The skill supports dynamic LoRA adapter loading with configurable weight merging, allowing multiple style and concept LoRAs to be combined in a single generation. ControlNet conditioning supports depth maps, canny edges, pose estimation, and segmentation masks for precise image composition control.
Batch prompt scheduling enables automated generation runs with parameter sweeps across guidance scale, sampling steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent manages VRAM efficiently by offloading models to CPU when switching between pipeline configurations.
ComfyUI integration provides node-based workflow construction via the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and InstantID. Generated images include full metadata embedding with generation parameters for reproducibility. The skill handles SDXL turbo and lightning variants for real-time generation use cases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
