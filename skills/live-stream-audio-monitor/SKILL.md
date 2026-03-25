---
name: "Live Stream Audio Monitor"
description: "Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm."
category: "Media & Transcription"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/live-stream-audio-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58283  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Live Stream Audio Monitor

Monitors live audio streams from RTMP, HLS, or Icecast sources using FFmpeg stream capture and real-time chunked transcription via Deepgram’s streaming API or Whisper.cpp. Detects silence gaps, audio clipping, and loudness deviations from EBU R128 targets using pyloudnorm.

## Overview

Live Stream Audio Monitor provides real-time quality monitoring and transcription for live audio broadcasts. It connects to RTMP, HLS, and Icecast streams using FFmpeg’s input protocols, capturing audio chunks for parallel processing through both quality analysis and speech-to-text pipelines.

Audio quality analysis runs through pyloudnorm for EBU R128 integrated loudness measurement, detecting deviations from the target -14 LUFS for streaming or -24 LUFS for broadcast. The monitor identifies silence gaps longer than configurable thresholds using FFmpeg’s silencedetect filter, flags audio clipping via astats peak level analysis, and tracks loudness range to catch dynamic compression issues.

Real-time transcription connects to Deepgram’s streaming WebSocket API for low-latency speech-to-text, with fallback to local Whisper.cpp processing for offline or cost-sensitive deployments. Transcripts are streamed to a WebSocket endpoint for live captioning display. Alert notifications fire through webhook callbacks when quality metrics breach thresholds — silence lasting over 5 seconds, loudness swings exceeding 6 LU, or sustained clipping. All metrics log to a time-series database for post-stream quality reports.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill live-stream-audio-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill live-stream-audio-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill live-stream-audio-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill live-stream-audio-monitor -a codex
```

### OpenClaw

```bash
clawhub install live-stream-audio-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/live-stream-audio-monitor/
