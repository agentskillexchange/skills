---
name: "DALL-E Variation Generator"
description: "Generates image variations and edits using OpenAI’s DALL-E 3 API with mask-based inpainting, style consistency scoring via CLIP embeddings, and automatic prompt refinement loops."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-variation-generator/"
---
# DALL-E Variation Generator

Generates image variations and edits using OpenAI’s DALL-E 3 API with mask-based inpainting, style consistency scoring via CLIP embeddings, and automatic prompt refinement loops.

The DALL-E Variation Generator skill uses the OpenAI Images API to create variations of existing images and perform mask-based edits with DALL-E 3. It handles image preprocessing including resize to supported dimensions, PNG conversion, and RGBA mask generation for inpainting regions.



Style consistency is measured using CLIP embeddings from the OpenAI CLIP model. The skill computes cosine similarity between generated variations and reference images, automatically rejecting outputs below a configurable similarity threshold and regenerating with adjusted prompts. This creates a feedback loop that converges on stylistically consistent outputs.



The prompt refinement module uses GPT-4o to analyze failed generations and suggest improved prompts based on DALL-E’s known strengths and limitations. The skill supports batch generation with concurrent API calls respecting rate limits, stores generation history with full prompt and parameter metadata in SQLite, and exports image grids for visual comparison using Sharp for Node.js or Pillow for Python environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-variation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-variation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-variation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-variation-generator -a codex
```

### OpenClaw

```bash
clawhub install dalle-variation-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-variation-generator/)
