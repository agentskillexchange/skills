---
name: "DALL-E 3 Brand Asset Batch Generator"
description: "Batch-generates brand assets using the OpenAI Images API with DALL-E 3. Manages prompt engineering for consistent brand identity across icons, banners, and social media templates."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dall-e-3-brand-asset-batch-generator/"
tool_ecosystem:
  tool: openai
  github_stars: 10765
  npm_weekly_downloads: 16275389
  github_repo: openai/openai-node
  license: Apache-2.0
  maintained: true
---

# DALL-E 3 Brand Asset Batch Generator

Batch-generates brand assets using the OpenAI Images API with DALL-E 3. Manages prompt engineering for consistent brand identity across icons, banners, and social media templates.

## Overview

The DALL-E 3 Brand Asset Batch Generator leverages the OpenAI Images API to produce consistent brand assets at scale. It accepts a brand specification including color palette, typography style, logo description, and mood keywords, then constructs optimized prompts for the /v1/images/generations endpoint with model=dall-e-3. The skill generates coordinated asset sets including app icons at standard sizes (1024×1024), social media banners (1792×1024), and square social posts (1024×1024) while maintaining visual consistency through carefully engineered prompt prefixes that encode brand guidelines. It manages the quality and style parameters, switching between vivid and natural modes based on asset type. Rate limiting is handled with configurable concurrency and retry logic for the OpenAI API. The skill stores generation metadata including the revised_prompt returned by DALL-E 3 for audit purposes. Output images are organized into asset directories by type and can be post-processed with Sharp or Pillow for format conversion, resizing to platform-specific dimensions, and metadata embedding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dall-e-3-brand-asset-batch-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dall-e-3-brand-asset-batch-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dall-e-3-brand-asset-batch-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dall-e-3-brand-asset-batch-generator -a codex
```

### OpenClaw

```bash
clawhub install dall-e-3-brand-asset-batch-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dall-e-3-brand-asset-batch-generator/
