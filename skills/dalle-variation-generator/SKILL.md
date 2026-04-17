---
title: "DALL-E Variation Generator"
description: "The DALL-E Variation Generator skill uses the OpenAI Images API to create variations of existing images and perform mask-based edits with DALL-E 3. It handles image preprocessing including resize to supported dimensions, PNG conversion, and RGBA mask generation for inpainting regions.\nStyle consistency is measured using CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity between generated variations and reference images, automatically rejecting outputs below a configurable similarity threshold and regenerating with adjusted prompts. This creates a feedback loop that converges on stylistically consistent outputs.\nThe prompt refinement module uses GPT-4o to analyze failed generations and suggest improved prompts based on DALL-E’s known strengths and limitations. The skill supports batch generation with concurrent API calls respecting rate limits, stores generation history with full prompt and parameter metadata in SQLite, and exports image grids for visual comparison using Sharp for Node.js or Pillow for Python environments."
verification: security_reviewed
source: "https://github.com/openai/openai-node"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  ase_npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Variation Generator

The DALL-E Variation Generator skill uses the OpenAI Images API to create variations of existing images and perform mask-based edits with DALL-E 3. It handles image preprocessing including resize to supported dimensions, PNG conversion, and RGBA mask generation for inpainting regions.
Style consistency is measured using CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity between generated variations and reference images, automatically rejecting outputs below a configurable similarity threshold and regenerating with adjusted prompts. This creates a feedback loop that converges on stylistically consistent outputs.
The prompt refinement module uses GPT-4o to analyze failed generations and suggest improved prompts based on DALL-E’s known strengths and limitations. The skill supports batch generation with concurrent API calls respecting rate limits, stores generation history with full prompt and parameter metadata in SQLite, and exports image grids for visual comparison using Sharp for Node.js or Pillow for Python environments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dalle-variation-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dalle-variation-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variation-generator/)
