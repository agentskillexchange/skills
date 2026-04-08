---
title: FFmpeg Audio Normalization Pipeline
description: 'This skill implements professional audio loudness normalization using
  FFmpeg’s loudnorm filter conforming to the EBU R128 broadcast standard. It performs
  a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json
  -f null /dev/null to measure the source audio’s integrated loudness (LUFS), true
  peak (dBTP), and loudness range (LU). The second pass applies correction using the
  measured values as input parameters to the loudnorm filter for precise linear normalization.
  The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify,
  Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts.
  It handles batch processing of multiple files using shell globbing and parallel
  execution via GNU parallel. Audio format conversion is handled through FFmpeg’s
  codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for
  Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports
  sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format
  -show_streams to verify output specifications.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/
category:
- Media &amp; Transcription
framework:
- OpenClaw
---

# FFmpeg Audio Normalization Pipeline

This skill implements professional audio loudness normalization using FFmpeg’s loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio’s integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg’s codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
