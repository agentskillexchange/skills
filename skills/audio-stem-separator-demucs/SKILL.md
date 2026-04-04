---
name: "Audio Stem Separator with Demucs"
category: "Media & Transcription"
verification: "security_reviewed"
source: "https://github.com/adefossez/demucs"
tool_ecosystem:
  github_repo: "adefossez/demucs"
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Separates audio tracks into individual stems (vocals, drums, bass, other) using Meta’s Demucs neural network model via the demucs Python package. Supports batch processing of WAV and MP3 files, outputs isolated stems in FLAC or WAV format, and integrates with FFmpeg for format conversion and loudness matching post-separation.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install audio-stem-separator-demucs

# OpenClaw CLI
openclaw skills install audio-stem-separator-demucs

# Chat command
/skill install audio-stem-separator-demucs

# Direct download
curl -L https://agentskillexchange.com/skills/audio-stem-separator-demucs/download -o audio-stem-separator-demucs.zip

# Git clone this repo and copy the skill folder
cp -r skills/audio-stem-separator-demucs ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
