---
name: Stable Diffusion ControlNet Pose Pipeline
description: Orchestrates Stable Diffusion image generation with ControlNet pose conditioning
  via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img
  endpoints.
verification: security_reviewed
source: https://github.com/lllyasviel/ControlNet
category:
- Image &amp; Creative Automation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: lllyasviel/ControlNet
  github_stars: 33793
---
# Stable Diffusion ControlNet Pose Pipeline

The Stable Diffusion ControlNet Pose Pipeline automates pose-conditioned image generation by orchestrating the Automatic1111 Stable Diffusion Web UI API. It chains multiple API endpoints starting with the /sdapi/v1/detect endpoint for OpenPose skeleton extraction from reference images, then feeds the detected pose maps into the /sdapi/v1/txt2img or /sdapi/v1/img2img endpoints with ControlNet extension parameters. The skill manages ControlNet model selection across pose, depth, canny, and normal map preprocessors, configuring control_mode, resize_mode, and guidance_start/end parameters for each conditioning layer. It supports multi-ControlNet setups where pose and depth maps are combined for more precise spatial control. Batch processing handles multiple reference images with consistent seed management for reproducible outputs. The skill integrates with the Civitai API to discover and download ControlNet models, and supports LoRA weight injection via the prompt syntax for style transfer. Output images are post-processed with the /sdapi/v1/extra-single-image upscaling endpoint using Real-ESRGAN or SwinIR models.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pose-pipeline/)
