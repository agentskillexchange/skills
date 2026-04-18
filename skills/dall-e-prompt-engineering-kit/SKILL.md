---
title: "DALL-E Prompt Engineering Kit"
description: "Structured prompt generation for OpenAI’s DALL-E 3 API (images/generations endpoint) with style modifiers, aspect ratio control, and batch variation generation. Includes negative prompt patterns and quality presets."
verification: security_reviewed
source: "https://github.com/openai/openai-node"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  ase_npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Prompt Engineering Kit

The DALL-E Prompt Engineering Kit provides systematic prompt construction for OpenAI’s image generation API. It interfaces with the /v1/images/generations endpoint using structured prompt templates that combine subject descriptions, style modifiers (photorealistic, digital art, watercolor, isometric), lighting directives, and composition guidelines.

The skill manages DALL-E 3 specific parameters including quality presets (standard vs hd), size options (1024×1024, 1792×1024, 1024×1792), and the revised_prompt response field for understanding how prompts are interpreted. It implements prompt chaining for iterative refinement, where generation results inform subsequent prompt adjustments.

Advanced features include negative prompt patterns (specifying what to exclude), style consistency tokens for maintaining visual coherence across series, batch variation generation using seed manipulation, and A/B prompt testing with visual similarity scoring. The kit includes prompt libraries for common use cases (product photography, character design, architectural visualization, icon generation) and integrates with the Images Edit endpoint for inpainting and outpainting workflows. Cost tracking per generation and rate limit management with queuing are built in.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dall-e-prompt-engineering-kit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dall-e-prompt-engineering-kit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dall-e-prompt-engineering-kit/)
