---
title: "Video Subtitle Translator Agent"
description: "Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages."
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
