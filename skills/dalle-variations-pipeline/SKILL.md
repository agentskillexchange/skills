---
name: DALL-E Variations Pipeline
description: Generates image variations and edits using the OpenAI Images API (DALL-E
  3 and gpt-image-1). Manages prompt engineering for consistent style, handles mask-based
  inpainting, and outputs multiple sizes with quality presets.
category: "Image &amp; Creative Automation"
framework: ChatGPT Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-variations-pipeline/"
---
# DALL-E Variations Pipeline

Generates image variations and edits using the OpenAI Images API (DALL-E 3 and gpt-image-1). Manages prompt engineering for consistent style, handles mask-based inpainting, and outputs multiple sizes with quality presets.

The DALL-E Variations Pipeline skill orchestrates image generation and editing workflows through the OpenAI Images API, supporting both DALL-E 3 for generation and gpt-image-1 for advanced editing and variation tasks.

For generation, the skill manages prompt construction with style modifiers, aspect ratio specifications, and quality presets (standard vs HD). It handles the revised_prompt field from DALL-E 3 responses to track how the model interpreted generation requests. Batch generation produces multiple variations from a single concept with controlled style consistency.

Edit operations use mask-based inpainting — the skill generates mask images from natural language descriptions of regions to modify, then submits edit requests with the original image, mask, and modification prompt. This enables targeted changes like replacing backgrounds, adding objects, or modifying specific elements without regenerating the full image.

The variation endpoint creates alternative interpretations of existing images while maintaining structural similarity. The skill chains generation, variation, and edit operations into pipelines for iterative refinement workflows. Output management handles multiple size formats (256×256, 512×512, 1024×1024, 1792×1024, 1024×1792), response format selection (URL vs base64), and local file saving with metadata preservation. Rate limit handling with exponential backoff ensures reliable batch processing. Built for creative teams, marketing departments, and developers building image-generation features.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-variations-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-variations-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-variations-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-variations-pipeline -a codex
```

### OpenClaw

```bash
clawhub install dalle-variations-pipeline
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variations-pipeline/)
