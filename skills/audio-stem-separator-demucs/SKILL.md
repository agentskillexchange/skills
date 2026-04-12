---
title: "Audio Stem Separator with Demucs"
slug: "audio-stem-separator-demucs"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
source: "https://github.com/adefossez/demucs"
tool_ecosystem:
  github_repo: "adefossez/demucs"
  github_stars: 2507
---

# Audio Stem Separator with Demucs

Separates audio tracks into individual stems (vocals, drums, bass, other) using Meta’s Demucs neural network model via the demucs Python package. Supports batch processing of WAV and MP3 files, outputs isolated stems in FLAC or WAV format, and integrates with FFmpeg for format conversion and loudness matching post-separation.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-stem-separator-demucs/)
