---
title: "DALL-E Variations Pipeline"
description: "The DALL-E Variations Pipeline skill orchestrates image generation and editing workflows through the OpenAI Images API, supporting both DALL-E 3 for generation and gpt-image-1 for advanced editing and variation tasks. For generation, the skill manages prompt construction with style modifiers, aspect ratio specifications, and quality presets (standard vs HD). It handles the revised_prompt field from DALL-E 3 responses to track how the model interpreted generation requests. Batch generation produces multiple variations from a single concept with controlled style consistency. Edit operations use mask-based inpainting — the skill generates mask images from natural language descriptions of regions to modify, then submits edit requests with the original image, mask, and modification prompt. This enables targeted changes like replacing backgrounds, adding objects, or modifying specific elements without regenerating the full image. The variation endpoint creates alternative interpretations of existing images while maintaining structural similarity. The skill chains generation, variation, and edit operations into pipelines for iterative refinement workflows. Output management handles multiple size formats (256&#215;256, 512&#215;512, 1024&#215;1024, 1792&#215;1024, 1024&#215;1792), response format selection (URL vs base64), and local file saving with metadata preservation. Rate limit handling with exponential backoff ensures reliable batch processing. Built for creative teams, marketing departments, and developers building image-generation features."
source: "https://github.com/openai/openai-node"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Variations Pipeline

The DALL-E Variations Pipeline skill orchestrates image generation and editing workflows through the OpenAI Images API, supporting both DALL-E 3 for generation and gpt-image-1 for advanced editing and variation tasks. For generation, the skill manages prompt construction with style modifiers, aspect ratio specifications, and quality presets (standard vs HD). It handles the revised_prompt field from DALL-E 3 responses to track how the model interpreted generation requests. Batch generation produces multiple variations from a single concept with controlled style consistency. Edit operations use mask-based inpainting — the skill generates mask images from natural language descriptions of regions to modify, then submits edit requests with the original image, mask, and modification prompt. This enables targeted changes like replacing backgrounds, adding objects, or modifying specific elements without regenerating the full image. The variation endpoint creates alternative interpretations of existing images while maintaining structural similarity. The skill chains generation, variation, and edit operations into pipelines for iterative refinement workflows. Output management handles multiple size formats (256&#215;256, 512&#215;512, 1024&#215;1024, 1792&#215;1024, 1024&#215;1792), response format selection (URL vs base64), and local file saving with metadata preservation. Rate limit handling with exponential backoff ensures reliable batch processing. Built for creative teams, marketing departments, and developers building image-generation features.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variations-pipeline/)
