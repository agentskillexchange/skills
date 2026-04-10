---
name: audiowaveform Audio Waveform Data Generator and Image Renderer
description: audiowaveform is a BBC open-source C++ CLI tool that generates waveform
  data from MP3, WAV, FLAC, Ogg Vorbis, and Opus audio files. It outputs binary or
  JSON waveform data and renders PNG waveform images at configurable zoom levels.
verification: security_reviewed
source: https://github.com/bbc/audiowaveform
category:
- Media &amp; Transcription
framework:
- Custom Agents
tool_ecosystem:
  github_repo: bbc/audiowaveform
  github_stars: 2130
  license: GPL-3.0
---
# audiowaveform Audio Waveform Data Generator and Image Renderer

audiowaveform is a command-line application developed by BBC Research & Development that processes audio files to generate waveform data suitable for visual rendering. It accepts MP3, WAV, FLAC, Ogg Vorbis, and Opus input formats and produces output in binary (.dat), JSON (.json), or PNG image (.png) formats.
The tool works by first mixing multi-channel audio to mono, then computing minimum and maximum sample values over groups of N input samples (controlled by the --zoom parameter). Each group of N samples produces one min/max pair in the output, creating a compact representation of the audio waveform that can be rendered at various zoom levels.
A skill built around audiowaveform enables agents to generate audio visualizations for podcast episodes, music tracks, voice recordings, and any audio content. The JSON output format integrates directly with Peaks.js, BBC's browser-based interactive audio waveform viewer, enabling rich web-based audio experiences.
Key CLI options include: --input-format (specify input type when piping from stdin), --output-format (dat, json, or png), --zoom (samples per pixel), --bits (8 or 16-bit output resolution), --start and --end (time range in seconds), --width and --height (image dimensions), --colors (waveform color scheme), and --split-channels (render each channel separately).
Integration workflows include: piping FFmpeg video output into audiowaveform for video soundtrack visualization, batch-processing podcast libraries to generate waveform thumbnails, creating audio previews for CMS platforms, and generating waveform data for interactive web audio players. The tool pairs with Peaks.js for browser-based waveform editing and with FFmpeg for format conversion pipelines. Available via apt on Ubuntu/Debian and as pre-built binaries for Linux, macOS, and Windows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audiowaveform-bbc-waveform-generator/)
