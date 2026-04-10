---
name: "pydub Python Audio Manipulation Library"
description: "pydub is a Python library that provides a simple, high-level interface for manipulating audio files. It supports slicing, concatenation, volume adjustment, crossfading, format conversion, and effects processing across all formats supported by FFmpeg."
verification: security_reviewed
source: "https://github.com/jiaaro/pydub"
category:
  - "Media &amp; Transcription"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pydub-python-audio-manipulation-library/)
