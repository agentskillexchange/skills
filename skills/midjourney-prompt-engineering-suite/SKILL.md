---
name: "Midjourney Prompt Engineering Suite"
description: "Generates and optimizes Midjourney prompts using the Midjourney API with automatic parameter tuning for aspect ratios, stylize values, and chaos settings. Includes A/B testing workflows via Replicate prediction API."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/midjourney-prompt-engineering-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "midjourney"  # from ase_tool_match
---

# Midjourney Prompt Engineering Suite

Generates and optimizes Midjourney prompts using the Midjourney API with automatic parameter tuning for aspect ratios, stylize values, and chaos settings. Includes A/B testing workflows via Replicate prediction API.

## Overview

The Midjourney Prompt Engineering Suite provides intelligent prompt construction and optimization for Midjourney image generation. It analyzes input descriptions and automatically selects optimal parameters including aspect ratio, stylize value, chaos level, and quality settings based on the intended output use case.

The skill maintains a prompt template library organized by genre (photorealistic, illustration, 3D render, abstract) with tested parameter combinations. It supports multi-prompt weighting syntax and negative prompting to exclude unwanted elements. Style reference images can be provided via URLs with configurable style weight blending.

A/B testing functionality leverages the Replicate prediction API to generate variant images with systematic parameter sweeps, scoring outputs using CLIP similarity against the target description. Results are compiled into comparison grids with metadata annotations. The suite includes prompt history tracking, favorite management, and export to JSON for team sharing. Batch generation queues handle rate limiting gracefully with exponential backoff.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-engineering-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-engineering-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-engineering-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-engineering-suite -a codex
```

### OpenClaw

```bash
clawhub install midjourney-prompt-engineering-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/midjourney-prompt-engineering-suite/
