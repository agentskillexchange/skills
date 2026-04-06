---
name: "Pedalboard Python Audio Effects Library by Spotify"
description: "Pedalboard is a Python library built by Spotify for working with audio: reading, writing, rendering, and adding studio-quality effects. It supports VST3 and Audio Unit plugins and runs on macOS, Windows, and Linux with high performance."
category: "Media &amp; Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/spotify/pedalboard"
tool_ecosystem:
  github_repo: "https://github.com/spotify/pedalboard"
  github_stars: 6041
  license: "GPL-3.0"
---
# Pedalboard Python Audio Effects Library by Spotify

Pedalboard is a Python library built by Spotify for working with audio: reading, writing, rendering, and adding studio-quality effects. It supports VST3 and Audio Unit plugins and runs on macOS, Windows, and Linux with high performance.

Pedalboard is an open-source Python library created by Spotify’s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk.

The library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines.

A key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW).

Pedalboard releases Python’s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines.

Install via pip install pedalboard. Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pedalboard-spotify-audio-effects-python
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pedalboard-spotify-audio-effects-python -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pedalboard-spotify-audio-effects-python -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pedalboard-spotify-audio-effects-python -a codex
```

### OpenClaw

```bash
clawhub install pedalboard-spotify-audio-effects-python
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pedalboard-spotify-audio-effects-python/)
