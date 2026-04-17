---
title: "DALL-E Variations Pipeline"
description: "Generates image variations and edits using the OpenAI Images API (DALL-E 3 and gpt-image-1). Manages prompt engineering for consistent style, handles mask-based inpainting, and outputs multiple sizes with quality presets."
verification: security_reviewed
source: "https://github.com/openai/openai-node"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
  license: "Apache-2.0"
---

# DALL-E Variations Pipeline

The DALL-E Variations Pipeline skill orchestrates image generation and editing workflows through the OpenAI Images API, supporting both DALL-E 3 for generation and gpt-image-1 for advanced editing and variation tasks.

For generation, the skill manages prompt construction with style modifiers, aspect ratio specifications, and quality presets (standard vs HD). It handles the revised_prompt field from DALL-E 3 responses to track how the model interpreted generation requests. Batch generation produces multiple variations from a single concept with controlled style consistency.

Edit operations use mask-based inpainting — the skill generates mask images from natural language descriptions of regions to modify, then submits edit requests with the original image, mask, and modification prompt. This enables targeted changes like replacing backgrounds, adding objects, or modifying specific elements without regenerating the full image.

The variation endpoint creates alternative interpretations of existing images while maintaining structural similarity. The skill chains generation, variation, and edit operations into pipelines for iterative refinement workflows. Output management handles multiple size formats (256×256, 512×512, 1024×1024, 1792×1024, 1024×1792), response format selection (URL vs base64), and local file saving with metadata preservation. Rate limit handling with exponential backoff ensures reliable batch processing. Built for creative teams, marketing departments, and developers building image-generation features.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dalle-variations-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dalle-variations-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variations-pipeline/)
