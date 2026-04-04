---
name: "Live Stream Audio Monitor"
category: "Media & Transcription"
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Live Stream Audio Monitor

Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install live-stream-audio-monitor

# OpenClaw CLI
openclaw skills install live-stream-audio-monitor

# Chat command
/skill install live-stream-audio-monitor

# Direct download
curl -L https://agentskillexchange.com/skills/live-stream-audio-monitor/download -o live-stream-audio-monitor.zip

# Git clone this repo and copy the skill folder
cp -r skills/live-stream-audio-monitor ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
