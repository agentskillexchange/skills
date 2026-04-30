---
title: "Generate Slack-ready animated GIFs from custom frame sequences"
description: "Use Anthropic's slack-gif-creator skill to build animated GIFs that stay inside Slack's practical size, duration, and dimension constraints. It gives an agent a bounded GIF-production workflow, not a generic image library or chat sticker listing."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator"
author: "Anthropic"
publisher_type: "Public repository"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Generate Slack-ready animated GIFs from custom frame sequences

Use Anthropic's slack-gif-creator skill to build animated GIFs that stay inside Slack's practical size, duration, and dimension constraints. It gives an agent a bounded GIF-production workflow, not a generic image library or chat sticker listing.

## Prerequisites

Python, Pillow, imageio, imageio-ffmpeg, numpy, and optional uploaded source images

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone or install anthropics/skills, pip install -r skills/slack-gif-creator/requirements.txt, then generate frames with the skill's GIFBuilder workflow before exporting an optimized Slack-sized GIF.
```

## Documentation

- https://raw.githubusercontent.com/anthropics/skills/main/skills/slack-gif-creator/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slack-ready-animated-gifs-from-custom-frame-sequences/)
