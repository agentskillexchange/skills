---
title: "Pedalboard Python Audio Effects Library by Spotify"
description: "Pedalboard is a Python library built by Spotify for working with audio: reading, writing, rendering, and adding studio-quality effects. It supports VST3 and Audio Unit plugins and runs on macOS, Windows, and Linux with high performance."
slug: "pedalboard-spotify-audio-effects-python"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/spotify/pedalboard"
tool_ecosystem:
  github_repo: "spotify/pedalboard"
  github_stars: 6041
---

# Pedalboard Python Audio Effects Library by Spotify

Pedalboard is a Python library built by Spotify for working with audio: reading, writing, rendering, and adding studio-quality effects. It supports VST3 and Audio Unit plugins and runs on macOS, Windows, and Linux with high performance.

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
clawhub install pedalboard-spotify-audio-effects-python
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Pedalboard is an open-source Python library created by Spotify’s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk.
The library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines.
A key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW).
Pedalboard releases Python’s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines.
Install via pip install pedalboard. Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pedalboard-spotify-audio-effects-python/)
