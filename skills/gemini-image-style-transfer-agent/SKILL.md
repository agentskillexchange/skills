---
title: "Gemini Image Style Transfer Agent"
description: "Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts."
slug: "gemini-image-style-transfer-agent"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/"
---

# Gemini Image Style Transfer Agent

Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts.

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
clawhub install gemini-image-style-transfer-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill handles image style transfer using Gemini Imagen 3’s image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., ‘Convert to impressionist watercolor with soft edges and warm tones’), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters.
Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google’s usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/)
