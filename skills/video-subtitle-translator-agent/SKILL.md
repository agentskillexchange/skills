---
name: "Video Subtitle Translator Agent"
category: "Media & Transcription"
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Video Subtitle Translator Agent

Extracts embedded subtitles from video containers using FFmpeg’s subtitle stream extraction, translates SRT/VTT files through DeepL API or Google Cloud Translation v3, and re-embeds localized subtitle tracks. Supports batch processing with language detection via langdetect and proper bidirectional text handling for RTL languages.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install video-subtitle-translator-agent

# OpenClaw CLI
openclaw skills install video-subtitle-translator-agent

# Chat command
/skill install video-subtitle-translator-agent

# Direct download
curl -L https://agentskillexchange.com/skills/video-subtitle-translator-agent/download -o video-subtitle-translator-agent.zip

# Git clone this repo and copy the skill folder
cp -r skills/video-subtitle-translator-agent ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/video-subtitle-translator-agent/)
