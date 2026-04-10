---
title: "Stable Diffusion XL Pipeline"
description: "Orchestrates SDXL image generation via the Stability AI REST API with ControlNet conditioning, IP-Adapter style transfer, and automatic prompt enhancement using CLIP interrogation."
slug: "stable-diffusion-xl-pipeline"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/"
---

# Stable Diffusion XL Pipeline

Orchestrates SDXL image generation via the Stability AI REST API with ControlNet conditioning, IP-Adapter style transfer, and automatic prompt enhancement using CLIP interrogation.

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
clawhub install stable-diffusion-xl-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion XL Pipeline skill manages end-to-end image generation workflows using the Stability AI platform API. It handles text-to-image, image-to-image, and inpainting modes with full control over SDXL parameters including cfg_scale, steps, sampler selection, and seed management.
ControlNet integration supports Canny edge, depth map, and OpenPose conditioning for precise compositional control. The skill preprocesses input images using OpenCV for edge detection and MiDaS for depth estimation before sending to the API. IP-Adapter style transfer allows blending reference image aesthetics with text prompts.
The prompt engineering module uses CLIP interrogation to analyze reference images and generate optimized prompts. It includes a negative prompt library, automatic prompt weighting syntax, and A1111-compatible embedding triggers. Output images are post-processed with Real-ESRGAN upscaling and face restoration via GFPGAN, with metadata embedded as EXIF and PNG tEXt chunks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/)
