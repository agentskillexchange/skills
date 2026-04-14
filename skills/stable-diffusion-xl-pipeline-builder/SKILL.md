---
title: "Stable Diffusion XL Pipeline Builder"
description: "Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
---

# Stable Diffusion XL Pipeline Builder

The Stable Diffusion XL Pipeline Builder creates sophisticated image generation workflows using the Hugging Face diffusers library and ComfyUI server API. It manages the full SDXL pipeline including base model inference, refiner pass, and VAE decoding stages.

The skill supports dynamic LoRA adapter loading with configurable weight merging, allowing multiple style and concept LoRAs to be combined in a single generation. ControlNet conditioning supports depth maps, canny edges, pose estimation, and segmentation masks for precise image composition control.

Batch prompt scheduling enables automated generation runs with parameter sweeps across guidance scale, sampling steps, and scheduler algorithms (DDIM, DPM++ 2M Karras, Euler Ancestral). The agent manages VRAM efficiently by offloading models to CPU when switching between pipeline configurations.

ComfyUI integration provides node-based workflow construction via the REST API, with support for custom nodes including IPAdapter, AnimateDiff, and InstantID. Generated images include full metadata embedding with generation parameters for reproducibility. The skill handles SDXL turbo and lightning variants for real-time generation use cases.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
