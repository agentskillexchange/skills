---
title: Stable Diffusion ComfyUI Workflow Runner
description: This skill automates Stable Diffusion image generation by submitting
  and managing workflow JSON files through ComfyUI’s HTTP API. It connects to ComfyUI
  instances running locally or on remote GPU servers, handling WebSocket connections
  for real-time progress updates and queue position tracking. Workflows are loaded
  from JSON templates with dynamic parameter injection for prompts, seeds, dimensions,
  CFG scale, and sampler settings. The skill supports advanced features including
  LoRA model stacking with per-LoRA weight control, ControlNet conditioning with preprocessor
  selection (Canny, Depth, OpenPose via ControlNet auxiliary models), IP-Adapter for
  style transfer, and upscaling via Ultimate SD Upscale or Tiled VAE. Batch generation
  processes multiple prompt variations with seed increments. Output images are automatically
  downloaded from ComfyUI’s output directory, tagged with generation metadata in EXIF/PNG-info,
  and optionally uploaded to cloud storage. Queue management handles concurrent requests
  with priority levels and timeout handling for long-running hi-res workflows.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/
category:
- Image &amp; Creative Automation
framework:
- MCP
---

# Stable Diffusion ComfyUI Workflow Runner

This skill automates Stable Diffusion image generation by submitting and managing workflow JSON files through ComfyUI’s HTTP API. It connects to ComfyUI instances running locally or on remote GPU servers, handling WebSocket connections for real-time progress updates and queue position tracking. Workflows are loaded from JSON templates with dynamic parameter injection for prompts, seeds, dimensions, CFG scale, and sampler settings. The skill supports advanced features including LoRA model stacking with per-LoRA weight control, ControlNet conditioning with preprocessor selection (Canny, Depth, OpenPose via ControlNet auxiliary models), IP-Adapter for style transfer, and upscaling via Ultimate SD Upscale or Tiled VAE. Batch generation processes multiple prompt variations with seed increments. Output images are automatically downloaded from ComfyUI’s output directory, tagged with generation metadata in EXIF/PNG-info, and optionally uploaded to cloud storage. Queue management handles concurrent requests with priority levels and timeout handling for long-running hi-res workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/)
