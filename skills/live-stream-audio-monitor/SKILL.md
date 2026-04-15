---
title: "Live Stream Audio Monitor"
description: "Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media & Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Live Stream Audio Monitor

Live Stream Audio Monitor provides real-time quality monitoring and transcription for live audio broadcasts. It connects to RTMP, HLS, and Icecast streams using FFmpeg’s input protocols, capturing audio chunks for parallel processing through both quality analysis and speech-to-text pipelines.

Audio quality analysis runs through pyloudnorm for EBU R128 integrated loudness measurement, detecting deviations from the target -14 LUFS for streaming or -24 LUFS for broadcast. The monitor identifies silence gaps longer than configurable thresholds using FFmpeg’s silencedetect filter, flags audio clipping via astats peak level analysis, and tracks loudness range to catch dynamic compression issues.

Real-time transcription connects to Deepgram’s streaming WebSocket API for low-latency speech-to-text, with fallback to local Whisper.cpp processing for offline or cost-sensitive deployments. Transcripts are streamed to a WebSocket endpoint for live captioning display. Alert notifications fire through webhook callbacks when quality metrics breach thresholds — silence lasting over 5 seconds, loudness swings exceeding 6 LU, or sustained clipping. All metrics log to a time-series database for post-stream quality reports.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/live-stream-audio-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/live-stream-audio-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
