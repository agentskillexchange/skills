---
title: "Gemini Image Style Transfer Agent"
description: "Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
---

# Gemini Image Style Transfer Agent

Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts.

This skill handles image style transfer using Gemini Imagen 3’s image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., ‘Convert to impressionist watercolor with soft edges and warm tones’), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters.

Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google’s usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/)
