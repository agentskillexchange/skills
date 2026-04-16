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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/)
