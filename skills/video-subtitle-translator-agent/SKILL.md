---
title: "Video Subtitle Translator Agent"
slug: "video-subtitle-translator-agent"
description: "Extracts embedded subtitles from video containers using FFmpeg&#8217;s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages."
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
category: "Media &amp; Transcription"
framework: "Gemini"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---
# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg&#8217;s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

## Installation

Choose the installation path that fits your setup:

1. Install from Agent Skill Exchange in the OpenClaw UI.
2. Copy the skill folder into your local skills directory.
3. Add it to your shared workspace skills collection.
4. Install it through a compatible agent skill manager.
5. Clone or download the upstream source and wire it into your agent runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
