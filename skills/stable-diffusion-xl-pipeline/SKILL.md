---
title: "Stable Diffusion XL Pipeline"
description: "Orchestrates SDXL image generation via the Stability AI REST API with ControlNet conditioning, IP-Adapter style transfer, and automatic prompt enhancement using CLIP interrogation."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
---

# Stable Diffusion XL Pipeline

The Stable Diffusion XL Pipeline skill manages end-to-end image generation workflows using the Stability AI platform API. It handles text-to-image, image-to-image, and inpainting modes with full control over SDXL parameters including cfg_scale, steps, sampler selection, and seed management. ControlNet integration supports Canny edge, depth map, and OpenPose conditioning for precise compositional control. The skill preprocesses input images using OpenCV for edge detection and MiDaS for depth estimation before sending to the API. IP-Adapter style transfer allows blending reference image aesthetics with text prompts. The prompt engineering module uses CLIP interrogation to analyze reference images and generate optimized prompts. It includes a negative prompt library, automatic prompt weighting syntax, and A1111-compatible embedding triggers. Output images are post-processed with Real-ESRGAN upscaling and face restoration via GFPGAN, with metadata embedded as EXIF and PNG tEXt chunks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stable-diffusion-xl-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stable-diffusion-xl-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/)
