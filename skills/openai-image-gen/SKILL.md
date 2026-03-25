---
name: "OpenAI Image Gen"
description: "Batch-generate images through the OpenAI Images API with a prompt sampler and gallery output."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openai-image-gen/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAI Image Gen

Batch-generate images through the OpenAI Images API with a prompt sampler and gallery output.

## Overview

OpenAI Image Gen gives OpenClaw a focused batch image-generation workflow built around the OpenAI Images API. It is designed for users who want to render multiple structured prompts, vary model settings, and review results in a simple gallery instead of generating one image at a time.

Best for

batch-generating images from structured prompts

testing model, size, and quality combinations

producing gallery-style output for review and iteration

Install notes

Requires Python 3 and a valid `OPENAI_API_KEY`. Install the skill, configure your API key, then run the bundled generation script with the model and output settings you want.

**Source:** OpenClaw official skill.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openai-image-gen
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openai-image-gen -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openai-image-gen -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openai-image-gen -a codex
```

### OpenClaw

```bash
clawhub install openai-image-gen
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openai-image-gen/
