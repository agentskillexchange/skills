---
title: "Stable Diffusion ControlNet Pipeline"
description: "The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance.\nThe skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows.\nKey capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation."
verification: security_reviewed
source: "https://github.com/Stability-AI/stablediffusion"
framework:
  - "Cursor"
---

# Stable Diffusion ControlNet Pipeline

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance.
The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows.
Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stable-diffusion-controlnet-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stable-diffusion-controlnet-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
