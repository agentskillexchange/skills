---
name: DALL-E 3 Brand Asset Batch Generator
description: Batch-generates brand assets using the OpenAI Images API with DALL-E
  3. Manages prompt engineering for consistent brand identity across icons, banners,
  and social media templates.
verification: security_reviewed
source: https://platform.openai.com/docs/guides/images
category:
- Image &amp; Creative Automation
framework:
- OpenClaw
---
# DALL-E 3 Brand Asset Batch Generator

The DALL-E 3 Brand Asset Batch Generator leverages the OpenAI Images API to produce consistent brand assets at scale. It accepts a brand specification including color palette, typography style, logo description, and mood keywords, then constructs optimized prompts for the /v1/images/generations endpoint with model=dall-e-3. The skill generates coordinated asset sets including app icons at standard sizes (1024&#215;1024), social media banners (1792&#215;1024), and square social posts (1024&#215;1024) while maintaining visual consistency through carefully engineered prompt prefixes that encode brand guidelines. It manages the quality and style parameters, switching between vivid and natural modes based on asset type. Rate limiting is handled with configurable concurrency and retry logic for the OpenAI API. The skill stores generation metadata including the revised_prompt returned by DALL-E 3 for audit purposes. Output images are organized into asset directories by type and can be post-processed with Sharp or Pillow for format conversion, resizing to platform-specific dimensions, and metadata embedding.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dall-e-3-brand-asset-batch-generator/)
