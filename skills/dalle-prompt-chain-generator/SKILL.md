---
name: "DALL-E Prompt Chain Generator"
description: "Generates and iterates DALL-E 3 image prompts using the OpenAI Images API with size, quality, and style parameters. Chains edits via the images/edits endpoint with mask-based inpainting."
category: "Image &amp; Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-prompt-chain-generator/"
---
# DALL-E Prompt Chain Generator

Generates and iterates DALL-E 3 image prompts using the OpenAI Images API with size, quality, and style parameters. Chains edits via the images/edits endpoint with mask-based inpainting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-prompt-chain-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-prompt-chain-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-prompt-chain-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-prompt-chain-generator -a codex
```

### OpenClaw

```bash
clawhub install dalle-prompt-chain-generator
```

## Details

The DALL-E Prompt Chain Generator orchestrates iterative image creation workflows through the OpenAI Images API. It generates initial images via POST /v1/images/generations with model: “dall-e-3”, configurable size (1024×1024, 1792×1024, 1024×1792), quality (“standard” or “hd”), and style (“vivid” or “natural”) parameters.

The skill implements prompt engineering chains that analyze revised_prompt responses from DALL-E 3 to understand how the model interpreted instructions, then refines subsequent prompts for better alignment with creative intent. It manages image variation workflows through the /v1/images/variations endpoint for exploring creative directions from a base image.

Advanced capabilities include mask-based inpainting via /v1/images/edits with PNG mask images for targeted region modification, automatic prompt expansion using structured templates for consistent brand imagery, and batch generation with response_format: “b64_json” for direct pipeline processing without URL downloads. The generator maintains a prompt history log for reproducible image generation and supports A/B comparison workflows across different style and quality combinations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-prompt-chain-generator/)
