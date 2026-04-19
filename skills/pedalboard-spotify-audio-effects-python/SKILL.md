---
title: "Pedalboard Python Audio Effects Library by Spotify"
description: "Pedalboard is an open-source Python library created by Spotify&#8217;s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk. The library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines. A key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW). Pedalboard releases Python&#8217;s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines. Install via pip install pedalboard . Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard."
source: "https://github.com/spotify/pedalboard"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "spotify/pedalboard"
  github_stars: 6041
---

# Pedalboard Python Audio Effects Library by Spotify

Pedalboard is an open-source Python library created by Spotify&#8217;s Audio Intelligence Lab for processing audio programmatically. It provides a comprehensive set of tools for reading and writing audio files in multiple formats (AIFF, FLAC, MP3, OGG, WAV, AAC, and more), applying real-time audio effects, and rendering processed audio to disk. The library ships with a wide range of built-in audio effects including guitar-style effects (Chorus, Distortion, Phaser, Clipping), loudness and dynamic range processors (Compressor, Gain, Limiter), equalizers and filters (HighpassFilter, LadderFilter, LowpassFilter), spatial effects (Convolution, Delay, Reverb), pitch manipulation (PitchShift), and quality reduction tools (Resample, Bitcrush). Effects can be chained together using the Pedalboard class for complex processing pipelines. A key feature is the ability to load and use VST3 instrument and effect plugins on macOS, Windows, and Linux, as well as Audio Unit plugins on macOS. This means agents can leverage thousands of professional audio plugins directly from Python scripts without needing a Digital Audio Workstation (DAW). Pedalboard releases Python&#8217;s Global Interpreter Lock (GIL) during audio processing, enabling true multi-core parallelism. It also provides AudioStream for live real-time audio processing and on-the-fly resampling with O(1) memory usage. Internally at Spotify, pedalboard powers features like the AI DJ and AI Voice Translation, and is used for data augmentation in machine learning pipelines. Install via pip install pedalboard . Licensed under GPL-3.0 with over 6,000 GitHub stars and extensive documentation at spotify.github.io/pedalboard.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pedalboard-spotify-audio-effects-python/)
