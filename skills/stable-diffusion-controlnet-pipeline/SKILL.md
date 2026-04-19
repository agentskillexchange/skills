---
title: "Stable Diffusion ControlNet Pipeline"
description: "The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance. The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows. Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation."
source: "https://github.com/Stability-AI/stablediffusion"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
---

# Stable Diffusion ControlNet Pipeline

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance. The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows. Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
