---
title: "DALL-E Batch Image Generator"
description: "The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=&#8217;dall-e-3&#8242; and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024&#215;1024, 1024&#215;1792, 1792&#215;1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation."
source: "https://github.com/openai/openai-node"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Batch Image Generator

The DALL-E Batch Image Generator skill orchestrates high-volume image generation through the OpenAI Images API. It sends requests to the /v1/images/generations endpoint with model=&#8217;dall-e-3&#8242; and manages concurrent generation within API rate limits using a token bucket algorithm. The skill supports all DALL-E 3 parameters including size (1024&#215;1024, 1024&#215;1792, 1792&#215;1024), quality (standard/hd), and style (vivid/natural). Each generation captures the revised_prompt field returned by the API to track how DALL-E interpreted the original prompt. Images are downloaded from the temporary OpenAI CDN URLs with configurable output formats and organized into batch-labeled directories. The skill implements retry logic with exponential backoff for 429 rate limit responses and 500 server errors. Variation generation uses the /v1/images/variations endpoint with source images for iterative refinement. Cost tracking calculates per-image pricing based on size and quality tier. A gallery HTML report is auto-generated with side-by-side original/revised prompt comparison and thumbnail navigation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-batch-image-generator/)
