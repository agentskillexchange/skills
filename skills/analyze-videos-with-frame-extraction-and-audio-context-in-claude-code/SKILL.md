---
title: "Analyze videos with frame extraction and audio context in Claude Code"
description: "Give Claude Code a video perception layer that extracts frames, transcribes audio, and lets Claude answer questions about local videos or YouTube URLs."
verification: "security_reviewed"
source: "https://github.com/jordanrendric/claude-video-vision"
author: "Jordan Rendric"
publisher_type: "individual"
category:
  - "Media & Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jordanrendric/claude-video-vision"
  github_stars: 698
  npm_package: "claude-video-vision"
  npm_weekly_downloads: 802
---

# Analyze videos with frame extraction and audio context in Claude Code

Give Claude Code a video perception layer that extracts frames, transcribes audio, and lets Claude answer questions about local videos or YouTube URLs.

## Prerequisites

Claude Code, Node.js 20+, ffmpeg, optional yt-dlp, Gemini API or Whisper/OpenAI audio backend

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
In Claude Code, run /plugin marketplace add https://github.com/jordanrendric/claude-video-vision, then /plugin install claude-video-vision. Run /setup-video-vision to configure ffmpeg, audio backend, and optional YouTube support.
```

## Documentation

- https://github.com/jordanrendric/claude-video-vision

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/analyze-videos-with-frame-extraction-and-audio-context-in-claude-code/)
