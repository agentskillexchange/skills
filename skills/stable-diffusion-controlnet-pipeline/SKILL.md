---
title: "Stable Diffusion ControlNet Pipeline"
description: "Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement."
slug: "stable-diffusion-controlnet-pipeline"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/"
---

# Stable Diffusion ControlNet Pipeline

Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement.

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
clawhub install stable-diffusion-controlnet-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance.
The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows.
Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
