---
title: "DALL-E Batch Image Generator"
description: "Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-batch-image-generator/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
---

# DALL-E Batch Image Generator

The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=’dall-e-3′ and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024×1024, 1024×1792, 1792×1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-batch-image-generator/)
