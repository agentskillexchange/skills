---
title: "Video Subtitle Translator Agent"
description: "Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages."
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media & Transcription"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/video-subtitle-translator-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/video-subtitle-translator-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/video-subtitle-translator-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
