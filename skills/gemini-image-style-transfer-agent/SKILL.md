---
name: "Gemini Image Style Transfer Agent"
description: "Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts."
category: "Image &amp; Creative Automation"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/"
---
# Gemini Image Style Transfer Agent

Uses the Gemini Imagen 3 API (imagegeneration endpoint) to apply stylistic transformations to uploaded images, converting photos to watercolor, line art, or oil painting styles. Accepts base64-encoded input images and returns styled outputs with configurable style prompts.

This skill handles image style transfer using Gemini Imagen 3’s image editing capabilities. It takes an input image, encodes it as base64, constructs a style transfer prompt (e.g., ‘Convert to impressionist watercolor with soft edges and warm tones’), and calls the Gemini API with the image plus text prompt. Returns the styled image with metadata about generation parameters.

Use for product photography transformation, creative content pipelines, social media asset generation, and art direction workflows. Not for photorealistic face editing or content that violates Google’s usage policies. Requires a valid GEMINI_API_KEY and images under 10MB. Style accuracy varies — iterate on prompts for best results.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gemini-image-style-transfer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gemini-image-style-transfer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gemini-image-style-transfer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gemini-image-style-transfer-agent -a codex
```

### OpenClaw

```bash
clawhub install gemini-image-style-transfer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gemini-image-style-transfer-agent/)
