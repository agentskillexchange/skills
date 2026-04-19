---
title: "Gemini Image Style Transfer Agent"
description: "Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts. This skill handles image style transfer using Gemini Imagen 3&#8217;s image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., &#8216;Convert to impressionist watercolor with soft edges and warm tones&#8217;), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters. Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google&#8217;s usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results."
source: "https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
---

# Gemini Image Style Transfer Agent

Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts. This skill handles image style transfer using Gemini Imagen 3&#8217;s image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., &#8216;Convert to impressionist watercolor with soft edges and warm tones&#8217;), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters. Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google&#8217;s usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/)
