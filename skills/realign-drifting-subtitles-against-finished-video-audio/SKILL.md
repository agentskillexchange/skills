---
title: "Realign drifting subtitles against finished video audio"
description: "Uses Subaligner to retime an existing subtitle file against the final audio track, then outputs a corrected subtitle asset. This is for subtitle drift, forced alignment, or batch retiming, not for full video editing or general media management."
verification: "security_reviewed"
source: "https://github.com/baxtree/subaligner"
author: "baxtree"
publisher_type: "open_source_project"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "baxtree/subaligner"
  github_stars: 504
---

# Realign drifting subtitles against finished video audio

Uses Subaligner to retime an existing subtitle file against the final audio track, then outputs a corrected subtitle asset. This is for subtitle drift, forced alignment, or batch retiming, not for full video editing or general media management.

## Prerequisites

FFmpeg

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install subaligner; install FFmpeg first as required by upstream docs.
```

## Documentation

- https://subaligner.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/realign-drifting-subtitles-against-finished-video-audio/)
