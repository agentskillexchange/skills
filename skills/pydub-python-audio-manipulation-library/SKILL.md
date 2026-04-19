---
title: "pydub Python Audio Manipulation Library"
description: "pydub is an open-source Python library created by James Robert (jiaaro) that makes audio manipulation straightforward and intuitive. It wraps FFmpeg/libav to provide a clean, Pythonic API for working with audio files in any format that FFmpeg supports, including WAV, MP3, OGG, FLAC, AAC, WMA, and dozens more. The core abstraction is the AudioSegment class, which represents an audio clip and supports operator overloading for natural audio manipulation. You can slice audio with Python slice syntax ( song[:10000] for the first 10 seconds), adjust volume with addition/subtraction operators ( clip + 6 to boost by 6dB), concatenate clips with the + operator, and chain operations fluently since every operation returns a new AudioSegment. Key capabilities include: loading audio from any FFmpeg-supported format, slicing and splicing by millisecond precision, volume normalization and adjustment, fade in/out effects, crossfading between clips, audio concatenation and overlay/mixing, sample rate and channel conversion, silence detection and splitting, and exporting to any supported format with configurable bitrate, tags, and cover art metadata. pydub is installed via pip install pydub and requires FFmpeg as its backend audio processing engine. It has an extensive API documented at github.com/jiaaro/pydub/blob/master/API.markdown. With 9,700+ GitHub stars, 1,100+ forks, and over 10 million PyPI downloads, pydub is one of the most widely-used Python audio libraries. AI agents can use pydub to automate audio processing workflows like podcast editing, audio file format conversion, silence trimming, volume normalization, and creating audio montages programmatically."
source: "https://github.com/jiaaro/pydub"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jiaaro/pydub"
  github_stars: 9746
---

# pydub Python Audio Manipulation Library

pydub is an open-source Python library created by James Robert (jiaaro) that makes audio manipulation straightforward and intuitive. It wraps FFmpeg/libav to provide a clean, Pythonic API for working with audio files in any format that FFmpeg supports, including WAV, MP3, OGG, FLAC, AAC, WMA, and dozens more. The core abstraction is the AudioSegment class, which represents an audio clip and supports operator overloading for natural audio manipulation. You can slice audio with Python slice syntax ( song[:10000] for the first 10 seconds), adjust volume with addition/subtraction operators ( clip + 6 to boost by 6dB), concatenate clips with the + operator, and chain operations fluently since every operation returns a new AudioSegment. Key capabilities include: loading audio from any FFmpeg-supported format, slicing and splicing by millisecond precision, volume normalization and adjustment, fade in/out effects, crossfading between clips, audio concatenation and overlay/mixing, sample rate and channel conversion, silence detection and splitting, and exporting to any supported format with configurable bitrate, tags, and cover art metadata. pydub is installed via pip install pydub and requires FFmpeg as its backend audio processing engine. It has an extensive API documented at github.com/jiaaro/pydub/blob/master/API.markdown. With 9,700+ GitHub stars, 1,100+ forks, and over 10 million PyPI downloads, pydub is one of the most widely-used Python audio libraries. AI agents can use pydub to automate audio processing workflows like podcast editing, audio file format conversion, silence trimming, volume normalization, and creating audio montages programmatically.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pydub-python-audio-manipulation-library/)
