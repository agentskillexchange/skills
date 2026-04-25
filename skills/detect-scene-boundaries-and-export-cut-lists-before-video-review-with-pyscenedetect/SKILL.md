---
title: "Detect Scene Boundaries And Export Cut Lists Before Video Review With Pyscenedetect"
description: "Detect scene changes in a video, emit cut boundaries, and hand back machine-usable scene lists before manual review, splitting, or clip assembly."
verification: "security_reviewed"
source: "https://github.com/Breakthrough/PySceneDetect"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Breakthrough/PySceneDetect"
  github_stars: 4711
---

# Detect Scene Boundaries And Export Cut Lists Before Video Review With Pyscenedetect

PySceneDetect is a narrow, operator-facing skill for finding scene boundaries in video files and turning them into cut lists, saved images, or split-ready segments. An agent should invoke it when a downstream workflow needs reliable scene timestamps before someone starts reviewing footage by hand, extracting clips, or chunking media for transcription. Use this instead of a full video editor when the real job is scene detection and cut-list generation, not timeline editing. The scope boundary is explicit: detect scene transitions, export scene metadata, and optionally hand off to ffmpeg or another step for splitting. It is not a general media-production or video-generation listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/detect-scene-boundaries-and-export-cut-lists-before-video-review-with-pyscenedetect/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/detect-scene-boundaries-and-export-cut-lists-before-video-review-with-pyscenedetect
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/detect-scene-boundaries-and-export-cut-lists-before-video-review-with-pyscenedetect`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-scene-boundaries-and-export-cut-lists-before-video-review-with-pyscenedetect/)
