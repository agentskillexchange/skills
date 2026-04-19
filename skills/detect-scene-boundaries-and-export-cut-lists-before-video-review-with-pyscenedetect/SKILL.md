---
title: "Detect Scene Boundaries And Export Cut Lists Before Video Review With Pyscenedetect"
description: "PySceneDetect is a narrow, operator-facing skill for finding scene boundaries in video files and turning them into cut lists, saved images, or split-ready segments. An agent should invoke it when a downstream workflow needs reliable scene timestamps before someone starts reviewing footage by hand, extracting clips, or chunking media for transcription. Use this instead of a full video editor when the real job is scene detection and cut-list generation, not timeline editing. The scope boundary is explicit: detect scene transitions, export scene metadata, and optionally hand off to ffmpeg or another step for splitting. It is not a general media-production or video-generation listing."
source: "https://github.com/Breakthrough/PySceneDetect"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Breakthrough/PySceneDetect"
  github_stars: 4711
---

# Detect Scene Boundaries And Export Cut Lists Before Video Review With Pyscenedetect

PySceneDetect is a narrow, operator-facing skill for finding scene boundaries in video files and turning them into cut lists, saved images, or split-ready segments. An agent should invoke it when a downstream workflow needs reliable scene timestamps before someone starts reviewing footage by hand, extracting clips, or chunking media for transcription. Use this instead of a full video editor when the real job is scene detection and cut-list generation, not timeline editing. The scope boundary is explicit: detect scene transitions, export scene metadata, and optionally hand off to ffmpeg or another step for splitting. It is not a general media-production or video-generation listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-scene-boundaries-and-export-cut-lists-before-video-review-with-pyscenedetect/)
