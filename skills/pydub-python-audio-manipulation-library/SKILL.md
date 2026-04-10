---
title: "pydub Python Audio Manipulation Library"
description: "pydub is a Python library that provides a simple, high-level interface for manipulating audio files. It supports slicing, concatenation, volume adjustment, crossfading, format conversion, and effects processing across all formats supported by FFmpeg."
slug: "pydub-python-audio-manipulation-library"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/jiaaro/pydub"
tool_ecosystem:
  github_repo: "jiaaro/pydub"
  github_stars: 9746
listed: true
---

# pydub Python Audio Manipulation Library

pydub is a Python library that provides a simple, high-level interface for manipulating audio files. It supports slicing, concatenation, volume adjustment, crossfading, format conversion, and effects processing across all formats supported by FFmpeg.

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
clawhub install pydub-python-audio-manipulation-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

pydub is an open-source Python library created by James Robert (jiaaro) that makes audio manipulation straightforward and intuitive. It wraps FFmpeg/libav to provide a clean, Pythonic API for working with audio files in any format that FFmpeg supports, including WAV, MP3, OGG, FLAC, AAC, WMA, and dozens more.
The core abstraction is the AudioSegment class, which represents an audio clip and supports operator overloading for natural audio manipulation. You can slice audio with Python slice syntax (song[:10000] for the first 10 seconds), adjust volume with addition/subtraction operators (clip + 6 to boost by 6dB), concatenate clips with the + operator, and chain operations fluently since every operation returns a new AudioSegment.
Key capabilities include: loading audio from any FFmpeg-supported format, slicing and splicing by millisecond precision, volume normalization and adjustment, fade in/out effects, crossfading between clips, audio concatenation and overlay/mixing, sample rate and channel conversion, silence detection and splitting, and exporting to any supported format with configurable bitrate, tags, and cover art metadata.
pydub is installed via pip install pydub and requires FFmpeg as its backend audio processing engine. It has an extensive API documented at github.com/jiaaro/pydub/blob/master/API.markdown. With 9,700+ GitHub stars, 1,100+ forks, and over 10 million PyPI downloads, pydub is one of the most widely-used Python audio libraries. AI agents can use pydub to automate audio processing workflows like podcast editing, audio file format conversion, silence trimming, volume normalization, and creating audio montages programmatically.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pydub-python-audio-manipulation-library/)
