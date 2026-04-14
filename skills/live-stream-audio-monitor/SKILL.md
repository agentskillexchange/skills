---
title: "Live Stream Audio Monitor"
description: "Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media &amp; Transcription"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-stream-audio-monitor/)
