---
title: Stable Diffusion XL Pipeline
description: The Stable Diffusion XL Pipeline skill manages end-to-end image generation
  workflows using the Stability AI platform API. It handles text-to-image, image-to-image,
  and inpainting modes with full control over SDXL parameters including cfg_scale,
  steps, sampler selection, and seed management. ControlNet integration supports Canny
  edge, depth map, and OpenPose conditioning for precise compositional control. The
  skill preprocesses input images using OpenCV for edge detection and MiDaS for depth
  estimation before sending to the API. IP-Adapter style transfer allows blending
  reference image aesthetics with text prompts. The prompt engineering module uses
  CLIP interrogation to analyze reference images and generate optimized prompts. It
  includes a negative prompt library, automatic prompt weighting syntax, and A1111-compatible
  embedding triggers. Output images are post-processed with Real-ESRGAN upscaling
  and face restoration via GFPGAN, with metadata embedded as EXIF and PNG tEXt chunks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/
category:
- Image &amp; Creative Automation
framework:
- Claude Agents
---

# Stable Diffusion XL Pipeline

The Stable Diffusion XL Pipeline skill manages end-to-end image generation workflows using the Stability AI platform API. It handles text-to-image, image-to-image, and inpainting modes with full control over SDXL parameters including cfg_scale, steps, sampler selection, and seed management. ControlNet integration supports Canny edge, depth map, and OpenPose conditioning for precise compositional control. The skill preprocesses input images using OpenCV for edge detection and MiDaS for depth estimation before sending to the API. IP-Adapter style transfer allows blending reference image aesthetics with text prompts. The prompt engineering module uses CLIP interrogation to analyze reference images and generate optimized prompts. It includes a negative prompt library, automatic prompt weighting syntax, and A1111-compatible embedding triggers. Output images are post-processed with Real-ESRGAN upscaling and face restoration via GFPGAN, with metadata embedded as EXIF and PNG tEXt chunks.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline/)
