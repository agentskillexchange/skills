---
name: "Stable Diffusion ControlNet Pose Pipeline"
description: "Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints."
category: "42"
framework: "38"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-pose-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stable.diffusion"  # from ase_tool_match
---

# Stable Diffusion ControlNet Pose Pipeline

Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints.

## Overview

The Stable Diffusion ControlNet Pose Pipeline automates pose-conditioned image generation by orchestrating the Automatic1111 Stable Diffusion Web UI API. It chains multiple API endpoints starting with the /sdapi/v1/detect endpoint for OpenPose skeleton extraction from reference images, then feeds the detected pose maps into the /sdapi/v1/txt2img or /sdapi/v1/img2img endpoints with ControlNet extension parameters. The skill manages ControlNet model selection across pose, depth, canny, and normal map preprocessors, configuring control_mode, resize_mode, and guidance_start/end parameters for each conditioning layer. It supports multi-ControlNet setups where pose and depth maps are combined for more precise spatial control. Batch processing handles multiple reference images with consistent seed management for reproducible outputs. The skill integrates with the Civitai API to discover and download ControlNet models, and supports LoRA weight injection via the prompt syntax for style transfer. Output images are post-processed with the /sdapi/v1/extra-single-image upscaling endpoint using Real-ESRGAN or SwinIR models.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pose-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pose-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pose-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pose-pipeline -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-controlnet-pose-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stable-diffusion-controlnet-pose-pipeline/
