---
title: "Live Stream Audio Monitor"
description: "Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm."
slug: "live-stream-audio-monitor"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Live Stream Audio Monitor

Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install live-stream-audio-monitor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Live Stream Audio Monitor provides real-time quality monitoring and transcription for live audio broadcasts. It connects to RTMP, HLS, and Icecast streams using FFmpeg’s input protocols, capturing audio chunks for parallel processing through both quality analysis and speech-to-text pipelines.
Audio quality analysis runs through pyloudnorm for EBU R128 integrated loudness measurement, detecting deviations from the target -14 LUFS for streaming or -24 LUFS for broadcast. The monitor identifies silence gaps longer than configurable thresholds using FFmpeg’s silencedetect filter, flags audio clipping via astats peak level analysis, and tracks loudness range to catch dynamic compression issues.
Real-time transcription connects to Deepgram’s streaming WebSocket API for low-latency speech-to-text, with fallback to local Whisper.cpp processing for offline or cost-sensitive deployments. Transcripts are streamed to a WebSocket endpoint for live captioning display. Alert notifications fire through webhook callbacks when quality metrics breach thresholds — silence lasting over 5 seconds, loudness swings exceeding 6 LU, or sustained clipping. All metrics log to a time-series database for post-stream quality reports.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
