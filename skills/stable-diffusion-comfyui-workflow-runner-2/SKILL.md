---
title: "Stable Diffusion ComfyUI Workflow Runner"
description: "Executes ComfyUI workflow JSON files against a local or remote ComfyUI server via its REST API. Supports LoRA loading, ControlNet conditioning, and queue management with progress polling."
slug: "stable-diffusion-comfyui-workflow-runner-2"
category:
  - "Image &amp; Creative Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/"
---

# Stable Diffusion ComfyUI Workflow Runner

Executes ComfyUI workflow JSON files against a local or remote ComfyUI server via its REST API. Supports LoRA loading, ControlNet conditioning, and queue management with progress polling.

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
clawhub install stable-diffusion-comfyui-workflow-runner-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates Stable Diffusion image generation by submitting and managing workflow JSON files through ComfyUI’s HTTP API. It connects to ComfyUI instances running locally or on remote GPU servers, handling WebSocket connections for real-time progress updates and queue position tracking. Workflows are loaded from JSON templates with dynamic parameter injection for prompts, seeds, dimensions, CFG scale, and sampler settings. The skill supports advanced features including LoRA model stacking with per-LoRA weight control, ControlNet conditioning with preprocessor selection (Canny, Depth, OpenPose via ControlNet auxiliary models), IP-Adapter for style transfer, and upscaling via Ultimate SD Upscale or Tiled VAE. Batch generation processes multiple prompt variations with seed increments. Output images are automatically downloaded from ComfyUI’s output directory, tagged with generation metadata in EXIF/PNG-info, and optionally uploaded to cloud storage. Queue management handles concurrent requests with priority levels and timeout handling for long-running hi-res workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-comfyui-workflow-runner-2/)
