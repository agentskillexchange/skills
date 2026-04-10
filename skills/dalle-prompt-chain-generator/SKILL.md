---
name: DALL-E Prompt Chain Generator
description: Generates and iterates DALL-E 3 image prompts using the OpenAI Images
  API with size, quality, and style parameters. Chains edits via the images/edits
  endpoint with mask-based inpainting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dalle-prompt-chain-generator/
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
---
# DALL-E Prompt Chain Generator

The DALL-E Prompt Chain Generator orchestrates iterative image creation workflows through the OpenAI Images API. It generates initial images via POST /v1/images/generations with model: &#8220;dall-e-3&#8221;, configurable size (1024&#215;1024, 1792&#215;1024, 1024&#215;1792), quality (&#8220;standard&#8221; or &#8220;hd&#8221;), and style (&#8220;vivid&#8221; or &#8220;natural&#8221;) parameters.
The skill implements prompt engineering chains that analyze revised_prompt responses from DALL-E 3 to understand how the model interpreted instructions, then refines subsequent prompts for better alignment with creative intent. It manages image variation workflows through the /v1/images/variations endpoint for exploring creative directions from a base image.
Advanced capabilities include mask-based inpainting via /v1/images/edits with PNG mask images for targeted region modification, automatic prompt expansion using structured templates for consistent brand imagery, and batch generation with response_format: &#8220;b64_json&#8221; for direct pipeline processing without URL downloads. The generator maintains a prompt history log for reproducible image generation and supports A/B comparison workflows across different style and quality combinations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-prompt-chain-generator/)
