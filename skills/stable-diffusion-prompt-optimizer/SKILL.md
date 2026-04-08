---
title: Stable Diffusion Prompt Optimizer
description: The Stable Diffusion Prompt Optimizer skill enhances text-to-image prompts
  for Automatic1111’s Stable Diffusion WebUI. It connects to the /sdapi/v1/txt2img
  REST endpoint and analyzes prompt effectiveness by generating test batches with
  varied parameters. The skill applies A1111-specific syntax enhancements including
  attention weighting with (keyword:1.3) notation, BREAK tokens for 75-token chunk
  boundaries, and alternating prompt syntax [word1|word2] for creative blending. Negative
  prompts are auto-generated based on the positive prompt content using an embedded
  quality-tag database covering common artifacts like extra fingers, blurry backgrounds,
  and watermarks. The skill queries /sdapi/v1/sd-models to match prompts with appropriate
  checkpoint models and uses /sdapi/v1/samplers to recommend optimal sampler settings.
  Batch comparison mode generates A/B test grids using the /sdapi/v1/img2img endpoint
  with controlled seed variation. LoRA trigger words are automatically detected and
  inserted via /sdapi/v1/loras endpoint enumeration. CFG scale and step count optimization
  uses binary search to find the quality-performance sweet spot.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/
category:
- Image &amp; Creative Automation
framework:
- Gemini
---

# Stable Diffusion Prompt Optimizer

The Stable Diffusion Prompt Optimizer skill enhances text-to-image prompts for Automatic1111’s Stable Diffusion WebUI. It connects to the /sdapi/v1/txt2img REST endpoint and analyzes prompt effectiveness by generating test batches with varied parameters. The skill applies A1111-specific syntax enhancements including attention weighting with (keyword:1.3) notation, BREAK tokens for 75-token chunk boundaries, and alternating prompt syntax [word1|word2] for creative blending. Negative prompts are auto-generated based on the positive prompt content using an embedded quality-tag database covering common artifacts like extra fingers, blurry backgrounds, and watermarks. The skill queries /sdapi/v1/sd-models to match prompts with appropriate checkpoint models and uses /sdapi/v1/samplers to recommend optimal sampler settings. Batch comparison mode generates A/B test grids using the /sdapi/v1/img2img endpoint with controlled seed variation. LoRA trigger words are automatically detected and inserted via /sdapi/v1/loras endpoint enumeration. CFG scale and step count optimization uses binary search to find the quality-performance sweet spot.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/)
