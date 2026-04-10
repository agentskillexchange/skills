---
title: "Stable Diffusion ControlNet Pose Pipeline"
description: "Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints."
slug: "stable-diffusion-controlnet-pose-pipeline"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/lllyasviel/ControlNet"
tool_ecosystem:
  github_repo: "lllyasviel/ControlNet"
  github_stars: 33793
listed: true
---

# Stable Diffusion ControlNet Pose Pipeline

Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints.

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
clawhub install stable-diffusion-controlnet-pose-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion ControlNet Pose Pipeline automates pose-conditioned image generation by orchestrating the Automatic1111 Stable Diffusion Web UI API. It chains multiple API endpoints starting with the /sdapi/v1/detect endpoint for OpenPose skeleton extraction from reference images, then feeds the detected pose maps into the /sdapi/v1/txt2img or /sdapi/v1/img2img endpoints with ControlNet extension parameters. The skill manages ControlNet model selection across pose, depth, canny, and normal map preprocessors, configuring control_mode, resize_mode, and guidance_start/end parameters for each conditioning layer. It supports multi-ControlNet setups where pose and depth maps are combined for more precise spatial control. Batch processing handles multiple reference images with consistent seed management for reproducible outputs. The skill integrates with the Civitai API to discover and download ControlNet models, and supports LoRA weight injection via the prompt syntax for style transfer. Output images are post-processed with the /sdapi/v1/extra-single-image upscaling endpoint using Real-ESRGAN or SwinIR models.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pose-pipeline/)
