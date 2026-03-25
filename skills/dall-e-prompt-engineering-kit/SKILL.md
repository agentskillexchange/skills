---
name: "DALL-E Prompt Engineering Kit"
description: "Structured prompt generation for OpenAI’s DALL-E 3 API (images/generations endpoint) with style modifiers, aspect ratio control, and batch variation generation. Includes negative prompt patterns and quality presets."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dall-e-prompt-engineering-kit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10765  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DALL-E Prompt Engineering Kit

Structured prompt generation for OpenAI’s DALL-E 3 API (images/generations endpoint) with style modifiers, aspect ratio control, and batch variation generation. Includes negative prompt patterns and quality presets.

## Overview

The DALL-E Prompt Engineering Kit provides systematic prompt construction for OpenAI’s image generation API. It interfaces with the /v1/images/generations endpoint using structured prompt templates that combine subject descriptions, style modifiers (photorealistic, digital art, watercolor, isometric), lighting directives, and composition guidelines.

The skill manages DALL-E 3 specific parameters including quality presets (standard vs hd), size options (1024×1024, 1792×1024, 1024×1792), and the revised_prompt response field for understanding how prompts are interpreted. It implements prompt chaining for iterative refinement, where generation results inform subsequent prompt adjustments.

Advanced features include negative prompt patterns (specifying what to exclude), style consistency tokens for maintaining visual coherence across series, batch variation generation using seed manipulation, and A/B prompt testing with visual similarity scoring. The kit includes prompt libraries for common use cases (product photography, character design, architectural visualization, icon generation) and integrates with the Images Edit endpoint for inpainting and outpainting workflows. Cost tracking per generation and rate limit management with queuing are built in.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dall-e-prompt-engineering-kit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dall-e-prompt-engineering-kit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dall-e-prompt-engineering-kit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dall-e-prompt-engineering-kit -a codex
```

### OpenClaw

```bash
clawhub install dall-e-prompt-engineering-kit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dall-e-prompt-engineering-kit/
