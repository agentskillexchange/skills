---
name: "DALL-E Variations Pipeline"
description: "Generates image variations and edits using the OpenAI Images API (DALL-E 3 and gpt-image-1). Manages prompt engineering for consistent style, handles mask-based inpainting, and outputs multiple sizes with quality presets."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-variations-pipeline/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
---

# DALL-E Variations Pipeline

The DALL-E Variations Pipeline skill orchestrates image generation and editing workflows through the OpenAI Images API, supporting both DALL-E 3 for generation and gpt-image-1 for advanced editing and variation tasks.
For generation, the skill manages prompt construction with style modifiers, aspect ratio specifications, and quality presets (standard vs HD). It handles the revised_prompt field from DALL-E 3 responses to track how the model interpreted generation requests. Batch generation produces multiple variations from a single concept with controlled style consistency.
Edit operations use mask-based inpainting — the skill generates mask images from natural language descriptions of regions to modify, then submits edit requests with the original image, mask, and modification prompt. This enables targeted changes like replacing backgrounds, adding objects, or modifying specific elements without regenerating the full image.
The variation endpoint creates alternative interpretations of existing images while maintaining structural similarity. The skill chains generation, variation, and edit operations into pipelines for iterative refinement workflows. Output management handles multiple size formats (256&#215;256, 512&#215;512, 1024&#215;1024, 1792&#215;1024, 1024&#215;1792), response format selection (URL vs base64), and local file saving with metadata preservation. Rate limit handling with exponential backoff ensures reliable batch processing. Built for creative teams, marketing departments, and developers building image-generation features.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variations-pipeline/)
