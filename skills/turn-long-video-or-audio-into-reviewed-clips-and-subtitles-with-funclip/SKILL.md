---
title: "Turn long video or audio into reviewed clips and subtitles with FunClip"
description: "Use FunClip when an agent needs a repeatable local workflow for transcribing media, proposing clip timestamps, and producing reviewable video segments with subtitle files."
verification: "security_reviewed"
source: "https://github.com/modelscope/FunClip"
author: "ModelScope / FunASR"
publisher_type: "open-source"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "modelscope/FunClip"
  github_stars: 5878
---

# Turn long video or audio into reviewed clips and subtitles with FunClip

Use FunClip when an agent needs a repeatable local workflow for transcribing media, proposing clip timestamps, and producing reviewable video segments with subtitle files.

## Prerequisites

Python environment, FunClip source checkout, FunASR-supported models, local or server Gradio runtime, and media files to transcribe and clip.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the upstream FunClip repository, install its Python dependencies as documented, launch the local Gradio app with the documented python funclip/launch.py command, then load media files for transcription, subtitle generation, LLM-assisted timestamp selection, and reviewed clipping.
```

## Documentation

- https://github.com/modelscope/FunClip

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-long-video-or-audio-into-reviewed-clips-and-subtitles-with-funclip/)
