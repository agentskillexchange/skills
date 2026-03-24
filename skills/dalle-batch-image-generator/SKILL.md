---
name: "DALL-E Batch Image Generator"
description: "Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking."
category: "Image & Creative Automation"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dalle-batch-image-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DALL-E Batch Image Generator

Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking.

## Overview

The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=’dall-e-3′ and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024×1024, 1024×1792, 1792×1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-batch-image-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-batch-image-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-batch-image-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-batch-image-generator -a codex
```

### OpenClaw

```bash
clawhub install dalle-batch-image-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dalle-batch-image-generator/
