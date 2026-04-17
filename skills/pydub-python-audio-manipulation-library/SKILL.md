---
title: "pydub Python Audio Manipulation Library"
description: "pydub is an open-source Python library created by James Robert (jiaaro) that makes audio manipulation straightforward and intuitive. It wraps FFmpeg/libav to provide a clean, Pythonic API for working with audio files in any format that FFmpeg supports, including WAV, MP3, OGG, FLAC, AAC, WMA, and dozens more.\nThe core abstraction is the AudioSegment class, which represents an audio clip and supports operator overloading for natural audio manipulation. You can slice audio with Python slice syntax (song[:10000] for the first 10 seconds), adjust volume with addition/subtraction operators (clip + 6 to boost by 6dB), concatenate clips with the + operator, and chain operations fluently since every operation returns a new AudioSegment.\nKey capabilities include: loading audio from any FFmpeg-supported format, slicing and splicing by millisecond precision, volume normalization and adjustment, fade in/out effects, crossfading between clips, audio concatenation and overlay/mixing, sample rate and channel conversion, silence detection and splitting, and exporting to any supported format with configurable bitrate, tags, and cover art metadata.\npydub is installed via pip install pydub and requires FFmpeg as its backend audio processing engine. It has an extensive API documented at github.com/jiaaro/pydub/blob/master/API.markdown. With 9,700+ GitHub stars, 1,100+ forks, and over 10 million PyPI downloads, pydub is one of the most widely-used Python audio libraries. AI agents can use pydub to automate audio processing workflows like podcast editing, audio file format conversion, silence trimming, volume normalization, and creating audio montages programmatically."
verification: security_reviewed
source: "https://github.com/jiaaro/pydub"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jiaaro/pydub"
  github_stars: 9746
---

# pydub Python Audio Manipulation Library

pydub is an open-source Python library created by James Robert (jiaaro) that makes audio manipulation straightforward and intuitive. It wraps FFmpeg/libav to provide a clean, Pythonic API for working with audio files in any format that FFmpeg supports, including WAV, MP3, OGG, FLAC, AAC, WMA, and dozens more.
The core abstraction is the AudioSegment class, which represents an audio clip and supports operator overloading for natural audio manipulation. You can slice audio with Python slice syntax (song[:10000] for the first 10 seconds), adjust volume with addition/subtraction operators (clip + 6 to boost by 6dB), concatenate clips with the + operator, and chain operations fluently since every operation returns a new AudioSegment.
Key capabilities include: loading audio from any FFmpeg-supported format, slicing and splicing by millisecond precision, volume normalization and adjustment, fade in/out effects, crossfading between clips, audio concatenation and overlay/mixing, sample rate and channel conversion, silence detection and splitting, and exporting to any supported format with configurable bitrate, tags, and cover art metadata.
pydub is installed via pip install pydub and requires FFmpeg as its backend audio processing engine. It has an extensive API documented at github.com/jiaaro/pydub/blob/master/API.markdown. With 9,700+ GitHub stars, 1,100+ forks, and over 10 million PyPI downloads, pydub is one of the most widely-used Python audio libraries. AI agents can use pydub to automate audio processing workflows like podcast editing, audio file format conversion, silence trimming, volume normalization, and creating audio montages programmatically.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pydub-python-audio-manipulation-library
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pydub-python-audio-manipulation-library` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pydub-python-audio-manipulation-library/)
