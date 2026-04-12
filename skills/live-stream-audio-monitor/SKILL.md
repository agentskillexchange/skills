---
title: "Live Stream Audio Monitor"
slug: "live-stream-audio-monitor"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Live Stream Audio Monitor

Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
