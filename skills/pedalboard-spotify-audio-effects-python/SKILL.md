---
title: "Pedalboard Python Audio Effects Library by Spotify"
description: "Pedalboard is an open-source Python library created by Spotify’s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk.\nThe library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines.\nA key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW).\nPedalboard releases Python’s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines.\nInstall via pip install pedalboard. Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard."
verification: security_reviewed
source: "https://github.com/spotify/pedalboard"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "spotify/pedalboard"
  github_stars: 6041
---

# Pedalboard Python Audio Effects Library by Spotify

Pedalboard is an open-source Python library created by Spotify’s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk.
The library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines.
A key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW).
Pedalboard releases Python’s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines.
Install via pip install pedalboard. Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pedalboard-spotify-audio-effects-python
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pedalboard-spotify-audio-effects-python` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pedalboard-spotify-audio-effects-python/)
