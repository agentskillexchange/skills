---
title: "Force-align narration and transcript text into subtitle or SMIL timing maps"
description: "Use aeneas when an agent already has audio and text, but still needs timing. The workflow aligns spoken narration against fragments of plain text or XML and emits sync maps that can be turned into subtitles, EPUB 3 media overlays, JSON timing data, or other downstream caption assets."
verification: "security_reviewed"
source: "https://github.com/readbeyond/aeneas"
author: "Alberto Pettarin"
publisher_type: "Open Source Project"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "readbeyond/aeneas"
  github_stars: 2820
---

# Force-align narration and transcript text into subtitle or SMIL timing maps

Use aeneas when an agent already has audio and text, but still needs timing. The workflow aligns spoken narration against fragments of plain text or XML and emits sync maps that can be turned into subtitles, EPUB 3 media overlays, JSON timing data, or other downstream caption assets.

## Prerequisites

Python, pip, FFmpeg, and eSpeak

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install FFmpeg and eSpeak, then run: pip install numpy && pip install aeneas
```

## Documentation

- https://readbeyond.it/aeneas/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/force-align-narration-and-transcript-text-into-subtitle-or-smil-timing-maps/)
