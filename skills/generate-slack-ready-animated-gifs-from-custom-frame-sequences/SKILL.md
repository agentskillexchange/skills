---
title: "Generate Slack-ready animated GIFs from custom frame sequences"
description: "Use Anthropic’s slack-gif-creator skill to build animated GIFs that stay inside Slack’s practical size, duration, and dimension constraints. It gives an agent a bounded GIF-production workflow, not a generic image library or chat sticker listing."
verification: security_reviewed
source: "https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116154
---

# Generate Slack-ready animated GIFs from custom frame sequences

Tool name: Anthropic’s slack-gif-creator skill from the public anthropics/skills repository. The upstream source defines a very specific job: create animated GIFs optimized for Slack, with explicit dimensions, frame-rate guidance, color limits, and a code path built around GIFBuilder, Pillow, and image encoding helpers. That specificity is exactly why this passes the skill-shaped gate.

What the agent does: decide whether the output is an emoji-sized GIF or a larger message GIF, build or transform the frame sequence, draw graphics with Pillow primitives or use uploaded images as direct source material, optimize the palette and frame count, and export a GIF that is small enough and short enough to work well in Slack. The skill is valuable because it translates vague requests like “make me a Slack GIF of this mascot waving” into a repeatable rendering and optimization workflow with concrete technical constraints.

When to use it: invoke this skill when the user wants a custom Slack reaction GIF, a lightweight animated status graphic, or a short looping visual for internal chat. It is the right choice when a normal image generator is not enough because the final output must actually behave well inside Slack and not balloon in file size or playback length.

Scope boundary: this is not a generic design tool, not a broad video editor, and not a catalog card for Pillow or imageio. Its scope is narrowly bounded to Slack-oriented GIF creation and optimization. Integration points: Python, Pillow, imageio, imageio-ffmpeg, numpy, uploaded PNG or JPG source images, and downstream Slack usage for emoji or message attachments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-slack-ready-animated-gifs-from-custom-frame-sequences
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-slack-ready-animated-gifs-from-custom-frame-sequences` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slack-ready-animated-gifs-from-custom-frame-sequences/)
