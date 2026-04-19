---
title: "Live Stream Audio Monitor"
description: "Live Stream Audio Monitor provides real-time quality monitoring and transcription for live audio broadcasts. It connects to RTMP, HLS, and Icecast streams using FFmpeg&#8217;s input protocols, capturing audio chunks for parallel processing through both quality analysis and speech-to-text pipelines. Audio quality analysis runs through pyloudnorm for EBU R128 integrated loudness measurement, detecting deviations from the target -14 LUFS for streaming or -24 LUFS for broadcast. The monitor identifies silence gaps longer than configurable thresholds using FFmpeg&#8217;s silencedetect filter, flags audio clipping via astats peak level analysis, and tracks loudness range to catch dynamic compression issues. Real-time transcription connects to Deepgram&#8217;s streaming WebSocket API for low-latency speech-to-text, with fallback to local Whisper.cpp processing for offline or cost-sensitive deployments. Transcripts are streamed to a WebSocket endpoint for live captioning display. Alert notifications fire through webhook callbacks when quality metrics breach thresholds — silence lasting over 5 seconds, loudness swings exceeding 6 LU, or sustained clipping. All metrics log to a time-series database for post-stream quality reports."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "FFmpeg/FFmpeg"
  github_stars: 58548
---

# Live Stream Audio Monitor

Live Stream Audio Monitor provides real-time quality monitoring and transcription for live audio broadcasts. It connects to RTMP, HLS, and Icecast streams using FFmpeg&#8217;s input protocols, capturing audio chunks for parallel processing through both quality analysis and speech-to-text pipelines. Audio quality analysis runs through pyloudnorm for EBU R128 integrated loudness measurement, detecting deviations from the target -14 LUFS for streaming or -24 LUFS for broadcast. The monitor identifies silence gaps longer than configurable thresholds using FFmpeg&#8217;s silencedetect filter, flags audio clipping via astats peak level analysis, and tracks loudness range to catch dynamic compression issues. Real-time transcription connects to Deepgram&#8217;s streaming WebSocket API for low-latency speech-to-text, with fallback to local Whisper.cpp processing for offline or cost-sensitive deployments. Transcripts are streamed to a WebSocket endpoint for live captioning display. Alert notifications fire through webhook callbacks when quality metrics breach thresholds — silence lasting over 5 seconds, loudness swings exceeding 6 LU, or sustained clipping. All metrics log to a time-series database for post-stream quality reports.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
