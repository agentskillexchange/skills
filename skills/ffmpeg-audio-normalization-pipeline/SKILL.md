---
title: "FFmpeg Audio Normalization Pipeline"
description: "This skill implements professional audio loudness normalization using FFmpeg&#8217;s loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio&#8217;s integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg&#8217;s codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Audio Normalization Pipeline

This skill implements professional audio loudness normalization using FFmpeg&#8217;s loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio&#8217;s integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg&#8217;s codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
