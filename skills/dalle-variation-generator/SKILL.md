---
title: DALL-E Variation Generator
description: The DALL-E Variation Generator skill uses the OpenAI Images API to create
  variations of existing images and perform mask-based edits with DALL-E 3. It handles
  image preprocessing including resize to supported dimensions, PNG conversion, and
  RGBA mask generation for inpainting regions. Style consistency is measured using
  CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity
  between generated variations and reference images, automatically rejecting outputs
  below a configurable similarity threshold and regenerating with adjusted prompts.
  This creates a feedback loop that converges on stylistically consistent outputs.
  The prompt refinement module uses GPT-4o to analyze failed generations and suggest
  improved prompts based on DALL-E’s known strengths and limitations. The skill supports
  batch generation with concurrent API calls respecting rate limits, stores generation
  history with full prompt and parameter metadata in SQLite, and exports image grids
  for visual comparison using Sharp for Node.js or Pillow for Python environments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dalle-variation-generator/
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
---

# DALL-E Variation Generator

The DALL-E Variation Generator skill uses the OpenAI Images API to create variations of existing images and perform mask-based edits with DALL-E 3. It handles image preprocessing including resize to supported dimensions, PNG conversion, and RGBA mask generation for inpainting regions. Style consistency is measured using CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity between generated variations and reference images, automatically rejecting outputs below a configurable similarity threshold and regenerating with adjusted prompts. This creates a feedback loop that converges on stylistically consistent outputs. The prompt refinement module uses GPT-4o to analyze failed generations and suggest improved prompts based on DALL-E’s known strengths and limitations. The skill supports batch generation with concurrent API calls respecting rate limits, stores generation history with full prompt and parameter metadata in SQLite, and exports image grids for visual comparison using Sharp for Node.js or Pillow for Python environments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variation-generator/)
