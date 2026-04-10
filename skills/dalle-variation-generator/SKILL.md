---
title: "DALL-E Variation Generator"
description: "Generates image variations and edits using OpenAI’s DALL-E 3 API with mask-based inpainting, style consistency scoring via CLIP embeddings, and automatic prompt refinement loops."
slug: "dalle-variation-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dalle-variation-generator/"
---

# DALL-E Variation Generator

Generates image variations and edits using OpenAI’s DALL-E 3 API with mask-based inpainting, style consistency scoring via CLIP embeddings, and automatic prompt refinement loops.

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
clawhub install dalle-variation-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The DALL-E Variation Generator skill uses the OpenAI Images API to create variations of existing images and perform mask-based edits with DALL-E 3. It handles image preprocessing including resize to supported dimensions, PNG conversion, and RGBA mask generation for inpainting regions.
Style consistency is measured using CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity between generated variations and reference images, automatically rejecting outputs below a configurable similarity threshold and regenerating with adjusted prompts. This creates a feedback loop that converges on stylistically consistent outputs.
The prompt refinement module uses GPT-4o to analyze failed generations and suggest improved prompts based on DALL-E’s known strengths and limitations. The skill supports batch generation with concurrent API calls respecting rate limits, stores generation history with full prompt and parameter metadata in SQLite, and exports image grids for visual comparison using Sharp for Node.js or Pillow for Python environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variation-generator/)
