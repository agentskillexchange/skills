---
name: "Stable Diffusion XL Pipeline"
description: "Orchestrates SDXL image generation via the Stability AI REST API with ControlNet conditioning, IP-Adapter style transfer, and automatic prompt enhancement using CLIP interrogation."
category: "Image &amp; Creative Automation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/"
---
# Stable Diffusion XL Pipeline

Orchestrates SDXL image generation via the Stability AI REST API with ControlNet conditioning, IP-Adapter style transfer, and automatic prompt enhancement using CLIP interrogation.

## Overview

The Stable Diffusion XL Pipeline skill manages end-to-end image generation workflows using the Stability AI platform API. It handles text-to-image, image-to-image, and inpainting modes with full control over SDXL parameters including cfg_scale, steps, sampler selection, and seed management.

ControlNet integration supports Canny edge, depth map, and OpenPose conditioning for precise compositional control. The skill preprocesses input images using OpenCV for edge detection and MiDaS for depth estimation before sending to the API. IP-Adapter style transfer allows blending reference image aesthetics with text prompts.

The prompt engineering module uses CLIP interrogation to analyze reference images and generate optimized prompts. It includes a negative prompt library, automatic prompt weighting syntax, and A1111-compatible embedding triggers. Output images are post-processed with Real-ESRGAN upscaling and face restoration via GFPGAN, with metadata embedded as EXIF and PNG tEXt chunks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-xl-pipeline -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-xl-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/)
