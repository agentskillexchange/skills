---
name: Stable Diffusion ComfyUI Workflow Runner
description: Executes ComfyUI workflow JSON files against a local or remote ComfyUI
  server via its REST API. Supports LoRA loading, ControlNet conditioning, and queue
  management with progress polling.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/
category:
- Image &amp; Creative Automation
framework:
- MCP
---
# Stable Diffusion ComfyUI Workflow Runner

This skill automates Stable Diffusion image generation by submitting and managing workflow JSON files through ComfyUI's HTTP API. It connects to ComfyUI instances running locally or on remote GPU servers, handling WebSocket connections for real-time progress updates and queue position tracking. Workflows are loaded from JSON templates with dynamic parameter injection for prompts, seeds, dimensions, CFG scale, and sampler settings. The skill supports advanced features including LoRA model stacking with per-LoRA weight control, ControlNet conditioning with preprocessor selection (Canny, Depth, OpenPose via ControlNet auxiliary models), IP-Adapter for style transfer, and upscaling via Ultimate SD Upscale or Tiled VAE. Batch generation processes multiple prompt variations with seed increments. Output images are automatically downloaded from ComfyUI's output directory, tagged with generation metadata in EXIF/PNG-info, and optionally uploaded to cloud storage. Queue management handles concurrent requests with priority levels and timeout handling for long-running hi-res workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/)
