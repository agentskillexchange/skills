---
name: "FFmpeg Audio Transcoder"
description: "Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe."
category: "Media & Transcription"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# FFmpeg Audio Transcoder

Transcodes and processes audio files using the FFmpeg CLI and libavcodec library. Supports batch format conversion, loudness normalization via EBU R128, and metadata extraction with ffprobe.

## Overview

The FFmpeg Audio Transcoder skill provides professional-grade audio processing through the FFmpeg command-line toolkit and its underlying libavcodec/libavformat libraries. It handles format conversion, quality optimization, and batch processing for audio files across all major codecs.

Core transcoding capabilities include converting between formats like WAV, FLAC, MP3 (via LAME encoder), AAC (via libfdk_aac), OGG Vorbis, and Opus with precise bitrate and sample rate control. The skill implements EBU R128 loudness normalization using the loudnorm filter, ensuring consistent perceived volume across audio files — critical for podcast production and broadcast compliance. Two-pass loudness analysis provides accurate integrated loudness, loudness range, and true peak measurements.

The skill leverages ffprobe for detailed metadata extraction including codec parameters, channel layout, duration, and embedded artwork. Batch processing handles directory-level operations with parallel execution using GNU parallel or xargs. Audio manipulation features include silence detection/removal via the silencedetect filter, audio splitting at chapter markers, crossfade generation between tracks, and sample rate conversion using the soxr resampler for high-quality output. It also supports extracting audio streams from video containers with codec copy for lossless extraction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-transcoder -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-audio-transcoder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ffmpeg-audio-transcoder/
