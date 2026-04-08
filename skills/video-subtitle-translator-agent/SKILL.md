---
title: "Video Subtitle Translator Agent"
slug: "video-subtitle-translator-agent"
description: "Extracts embedded subtitles from video containers using FFmpeg's subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages."
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg's subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
