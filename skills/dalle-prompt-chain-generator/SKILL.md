---
title: "DALL-E Prompt Chain Generator"
description: "The DALL-E Prompt Chain Generator orchestrates iterative image creation workflows through the OpenAI Images API. It generates initial images via POST /v1/images/generations with model: &#8220;dall-e-3&#8221;, configurable size (1024&#215;1024, 1792&#215;1024, 1024&#215;1792), quality (&#8220;standard&#8221; or &#8220;hd&#8221;), and style (&#8220;vivid&#8221; or &#8220;natural&#8221;) parameters. The skill implements prompt engineering chains that analyze revised_prompt responses from DALL-E 3 to understand how the model interpreted instructions, then refines subsequent prompts for better alignment with creative intent. It manages image variation workflows through the /v1/images/variations endpoint for exploring creative directions from a base image. Advanced capabilities include mask-based inpainting via /v1/images/edits with PNG mask images for targeted region modification, automatic prompt expansion using structured templates for consistent brand imagery, and batch generation with response_format: &#8220;b64_json&#8221; for direct pipeline processing without URL downloads. The generator maintains a prompt history log for reproducible image generation and supports A/B comparison workflows across different style and quality combinations."
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

# DALL-E Prompt Chain Generator

The DALL-E Prompt Chain Generator orchestrates iterative image creation workflows through the OpenAI Images API. It generates initial images via POST /v1/images/generations with model: &#8220;dall-e-3&#8221;, configurable size (1024&#215;1024, 1792&#215;1024, 1024&#215;1792), quality (&#8220;standard&#8221; or &#8220;hd&#8221;), and style (&#8220;vivid&#8221; or &#8220;natural&#8221;) parameters. The skill implements prompt engineering chains that analyze revised_prompt responses from DALL-E 3 to understand how the model interpreted instructions, then refines subsequent prompts for better alignment with creative intent. It manages image variation workflows through the /v1/images/variations endpoint for exploring creative directions from a base image. Advanced capabilities include mask-based inpainting via /v1/images/edits with PNG mask images for targeted region modification, automatic prompt expansion using structured templates for consistent brand imagery, and batch generation with response_format: &#8220;b64_json&#8221; for direct pipeline processing without URL downloads. The generator maintains a prompt history log for reproducible image generation and supports A/B comparison workflows across different style and quality combinations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-prompt-chain-generator/)
