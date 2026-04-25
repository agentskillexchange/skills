---
title: "Stable Diffusion ControlNet Pipeline"
description: "Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
---

# Stable Diffusion ControlNet Pipeline

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance. The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows. Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stable-diffusion-controlnet-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stable-diffusion-controlnet-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
