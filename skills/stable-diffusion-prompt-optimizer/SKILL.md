---
title: "Stable Diffusion Prompt Optimizer"
description: "Analyzes and enhances Stable Diffusion prompts using the Automatic1111 WebUI API /sdapi/v1/txt2img endpoint. Applies prompt weighting, negative prompt generation, and A1111-specific syntax like (keyword:weight)."
slug: "stable-diffusion-prompt-optimizer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/"
---

# Stable Diffusion Prompt Optimizer

Analyzes and enhances Stable Diffusion prompts using the Automatic1111 WebUI API /sdapi/v1/txt2img endpoint. Applies prompt weighting, negative prompt generation, and A1111-specific syntax like (keyword:weight).

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
clawhub install stable-diffusion-prompt-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stable Diffusion Prompt Optimizer skill enhances text-to-image prompts for Automatic1111’s Stable Diffusion WebUI. It connects to the /sdapi/v1/txt2img REST endpoint and analyzes prompt effectiveness by generating test batches with varied parameters. The skill applies A1111-specific syntax enhancements including attention weighting with (keyword:1.3) notation, BREAK tokens for 75-token chunk boundaries, and alternating prompt syntax [word1|word2] for creative blending. Negative prompts are auto-generated based on the positive prompt content using an embedded quality-tag database covering common artifacts like extra fingers, blurry backgrounds, and watermarks. The skill queries /sdapi/v1/sd-models to match prompts with appropriate checkpoint models and uses /sdapi/v1/samplers to recommend optimal sampler settings. Batch comparison mode generates A/B test grids using the /sdapi/v1/img2img endpoint with controlled seed variation. LoRA trigger words are automatically detected and inserted via /sdapi/v1/loras endpoint enumeration. CFG scale and step count optimization uses binary search to find the quality-performance sweet spot.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/)
