---
title: "DALL-E Batch Image Generator"
description: "Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking."
slug: "dalle-batch-image-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dalle-batch-image-generator/"
---

# DALL-E Batch Image Generator

Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking.

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
clawhub install dalle-batch-image-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=’dall-e-3′ and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024×1024, 1024×1792, 1792×1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-batch-image-generator/)
