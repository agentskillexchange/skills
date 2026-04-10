---
title: "audiowaveform Audio Waveform Data Generator and Image Renderer"
description: "audiowaveform is a BBC open-source C++ CLI tool that generates waveform data from MP3, WAV, FLAC, Ogg Vorbis, and Opus audio files. It outputs binary or JSON waveform data and renders PNG waveform images at configurable zoom levels."
slug: "audiowaveform-bbc-waveform-generator"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/bbc/audiowaveform"
tool_ecosystem:
  github_repo: "bbc/audiowaveform"
  github_stars: 2130
---

# audiowaveform Audio Waveform Data Generator and Image Renderer

audiowaveform is a BBC open-source C++ CLI tool that generates waveform data from MP3, WAV, FLAC, Ogg Vorbis, and Opus audio files. It outputs binary or JSON waveform data and renders PNG waveform images at configurable zoom levels.

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
clawhub install audiowaveform-bbc-waveform-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

audiowaveform is a command-line application developed by BBC Research & Development that processes audio files to generate waveform data suitable for visual rendering. It accepts MP3, WAV, FLAC, Ogg Vorbis, and Opus input formats and produces output in binary (.dat), JSON (.json), or PNG image (.png) formats.
The tool works by first mixing multi-channel audio to mono, then computing minimum and maximum sample values over groups of N input samples (controlled by the --zoom parameter). Each group of N samples produces one min/max pair in the output, creating a compact representation of the audio waveform that can be rendered at various zoom levels.
A skill built around audiowaveform enables agents to generate audio visualizations for podcast episodes, music tracks, voice recordings, and any audio content. The JSON output format integrates directly with Peaks.js, BBC’s browser-based interactive audio waveform viewer, enabling rich web-based audio experiences.
Key CLI options include: --input-format (specify input type when piping from stdin), --output-format (dat, json, or png), --zoom (samples per pixel), --bits (8 or 16-bit output resolution), --start and --end (time range in seconds), --width and --height (image dimensions), --colors (waveform color scheme), and --split-channels (render each channel separately).
Integration workflows include: piping FFmpeg video output into audiowaveform for video soundtrack visualization, batch-processing podcast libraries to generate waveform thumbnails, creating audio previews for CMS platforms, and generating waveform data for interactive web audio players. The tool pairs with Peaks.js for browser-based waveform editing and with FFmpeg for format conversion pipelines. Available via apt on Ubuntu/Debian and as pre-built binaries for Linux, macOS, and Windows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audiowaveform-bbc-waveform-generator/)
