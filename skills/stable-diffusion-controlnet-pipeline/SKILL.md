---
title: Stable Diffusion ControlNet Pipeline
description: The Stable Diffusion ControlNet Pipeline skill provides a comprehensive
  image generation framework that leverages ControlNet conditioning models through
  the Stability AI API. It supports multiple control modes including depth mapping
  via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation
  for precise human figure guidance. The skill integrates directly with the Hugging
  Face diffusers library to manage model downloads, LoRA weight loading, and scheduler
  configuration. It includes CLIP interrogator functionality to reverse-engineer prompts
  from reference images, enabling style transfer workflows. Key capabilities include
  batch processing with configurable seed management, automatic EXIF metadata embedding,
  and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI
  backends and cloud Stability AI endpoints, with automatic fallback between providers.
  Output images are validated against NSFW classifiers and can be automatically uploaded
  to S3-compatible storage with CDN invalidation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/
category:
- Image &amp; Creative Automation
framework:
- Cursor
---

# Stable Diffusion ControlNet Pipeline

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance. The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows. Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
