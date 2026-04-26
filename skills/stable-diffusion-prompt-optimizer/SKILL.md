---
title: "Stable Diffusion Prompt Optimizer"
description: "Analyzes and enhances Stable Diffusion prompts using the Automatic1111 WebUI API /sdapi/v1/txt2img endpoint. Applies prompt weighting, negative prompt generation, and A1111-specific syntax like (keyword:weight)."
verification: "security_reviewed"
source: "https://github.com/Stability-AI/stablediffusion"
category:
  - "Image & Creative Automation"
framework:
  - "Gemini"
---

# Stable Diffusion Prompt Optimizer

The Stable Diffusion Prompt Optimizer skill enhances text-to-image prompts for Automatic1111’s Stable Diffusion WebUI. It connects to the /sdapi/v1/txt2img REST endpoint and analyzes prompt effectiveness by generating test batches with varied parameters. The skill applies A1111-specific syntax enhancements including attention weighting with (keyword:1.3) notation, BREAK tokens for 75-token chunk boundaries, and alternating prompt syntax [word1|word2] for creative blending. Negative prompts are auto-generated based on the positive prompt content using an embedded quality-tag database covering common artifacts like extra fingers, blurry backgrounds, and watermarks. The skill queries /sdapi/v1/sd-models to match prompts with appropriate checkpoint models and uses /sdapi/v1/samplers to recommend optimal sampler settings. Batch comparison mode generates A/B test grids using the /sdapi/v1/img2img endpoint with controlled seed variation. LoRA trigger words are automatically detected and inserted via /sdapi/v1/loras endpoint enumeration. CFG scale and step count optimization uses binary search to find the quality-performance sweet spot.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stable-diffusion-prompt-optimizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stable-diffusion-prompt-optimizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/)
