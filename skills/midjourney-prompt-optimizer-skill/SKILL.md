---
name: "Midjourney Prompt Optimizer"
description: "Analyze and optimize Midjourney prompts using parameter tuning for –ar, –stylize, –chaos, and –weird flags. Generates prompt variations with style references (–sref) and character references (–cref) for consistent image output."
category: "Image & Creative Automation"
framework: "Gemini"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/midjourney-prompt-optimizer-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "midjourney"  # from ase_tool_match
---

# Midjourney Prompt Optimizer

Analyze and optimize Midjourney prompts using parameter tuning for –ar, –stylize, –chaos, and –weird flags. Generates prompt variations with style references (–sref) and character references (–cref) for consistent image output.

## Overview

Optimize image generation prompts for Midjourney with systematic parameter tuning and variation generation. This skill analyzes prompt structure and suggests improvements for better output quality and consistency.

The prompt analyzer breaks down input prompts into subject, style, lighting, composition, and technical parameter components. It evaluates prompt weight syntax (::weight), multi-prompt separators, and negative prompts (–no) for effectiveness.

Parameter optimization covers aspect ratio (–ar) selection based on intended use case, stylize values (–stylize 0-1000) for controlling artistic interpretation, chaos values (–chaos 0-100) for variation diversity, and weird values (–weird 0-3000) for unconventional aesthetics.

Advanced features include style reference URLs (–sref) for maintaining visual consistency across generations, character references (–cref) for preserving character identity, and seed locking (–seed) for reproducible results. The skill generates batch prompt sets with systematic parameter sweeps for A/B testing.

Version-specific optimization handles differences between Midjourney v5.2, v6, and v6.1 model capabilities, adjusting prompt strategies and available parameters for each version. Output includes formatted prompt text ready for Discord bot submission.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-optimizer-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-optimizer-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-optimizer-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-optimizer-skill -a codex
```

### OpenClaw

```bash
clawhub install midjourney-prompt-optimizer-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/midjourney-prompt-optimizer-skill/
