---
name: "Normalize loudness across podcast, lesson, or video batches before publishing"
slug: "normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing"
description: "Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery."
github_stars: 1500
verification: "security_reviewed"
source: "https://github.com/slhck/ffmpeg-normalize"
author: "slhck"
publisher_type: "Open Source Project"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "slhck/ffmpeg-normalize"
  github_stars: 1500
---

# Normalize loudness across podcast, lesson, or video batches before publishing

Uses ffmpeg-normalize to batch-normalize audio levels so an agent can hand off consistent output without opening a DAW or touching every file by hand. It fits pipelines that need EBU R128, RMS, or peak targets across mixed media before delivery.

## Prerequisites

ffmpeg plus a Python or uv environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip3 install ffmpeg-normalize
```

## Documentation

- https://slhck.info/ffmpeg-normalize/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-loudness-across-podcast-lesson-or-video-batches-before-publishing/)
