---
name: Gemini Image Style Transfer Agent
description: Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic
  transformations to uploaded images, converting photos to watercolor, line art, or
  oil painting styles. Accepts base64-encoded input images and returns styled outputs
  with configurable style prompts.
verification: security_reviewed
source: https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/
category:
- Image &amp; Creative Automation
framework:
- Gemini
---
# Gemini Image Style Transfer Agent

Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts.
This skill handles image style transfer using Gemini Imagen 3's image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., &#8216;Convert to impressionist watercolor with soft edges and warm tones'), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters.
Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google's usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/)
