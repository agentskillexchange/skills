---
name: "Stable Diffusion XL Pipeline Builder"
description: "Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling."
category: "Image &amp; Creative Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/"
---
# Stable Diffusion XL Pipeline Builder

Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling.

## Overview

The Stable Diffusion XL Pipeline Builder creates sophisticated image generation workflows using the Hugging Face diffusers library and ComfyUI server API. It manages the full SDXL pipeline including base model inference, refiner pass, and VAE decoding stages.

The skill supports dynamic LoRA adapter loading with configurable weight merging, allowing multiple style and concept LoRAs to be combined in a single generation. ControlNet conditioning supports depth maps, canny edges, pose estimation, and segmentation masks for precise image composition control.

Batch prompt scheduling enables automated generation runs with parameter sweeps across guidance scale, sampling steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent manages VRAM efficiently by offloading models to CPU when switching between pipeline configurations.

ComfyUI integration provides node-based workflow construction via the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and InstantID. Generated images include full metadata embedding with generation parameters for reproducibility. The skill handles SDXL turbo and lightning variants for real-time generation use cases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline-builder -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-xl-pipeline-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
