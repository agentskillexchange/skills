---
title: DALL-E Batch Image Generator
description: The DALL-E Batch Image Generator skill orchestrates high-volume image
  generation through the OpenAI Images API. It sends requests to the /v1/images/generations
  endpoint with model=’dall-e-3′ and manages concurrent generation within API rate
  limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters
  including size (1024×1024, 1024×1792, 1792×1024), quality (standard/hd), and style
  (vivid/natural). Each generation captures the revised_prompt field returned by the
  API to track how DALL-E interpreted the original prompt. Images are downloaded from
  the temporary OpenAI CDN URLs with configurable output formats and organized into
  batch-labeled directories. The skill implements retry logic with exponential backoff
  for 429 rate limit responses and 500 server errors. Variation generation uses the
  /v1/images/variations endpoint with source images for iterative refinement. Cost
  tracking calculates per-image pricing based on size and quality tier. A gallery
  HTML report is auto-generated with side-by-side original/revised prompt comparison
  and thumbnail navigation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dalle-batch-image-generator/
category:
- Image &amp; Creative Automation
framework:
- Claude Agents
---

# DALL-E Batch Image Generator

The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=’dall-e-3′ and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024×1024, 1024×1792, 1792×1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-batch-image-generator/)
