---
name: "audiowaveform Audio Waveform Data Generator and Image Renderer"
slug: "audiowaveform-bbc-waveform-generator"
description: "audiowaveform is a BBC open-source C++ CLI tool that generates waveform data from MP3, WAV, FLAC, Ogg Vorbis, and Opus audio files. It outputs binary or JSON waveform data and renders PNG waveform images at configurable zoom levels."
github_stars: 2130
verification: "security_reviewed"
source: "https://github.com/bbc/audiowaveform"
category: "Media & Transcription"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "bbc/audiowaveform"
  github_stars: 2130
---

# audiowaveform Audio Waveform Data Generator and Image Renderer

audiowaveform is a BBC open-source C++ CLI tool that generates waveform data from MP3, WAV, FLAC, Ogg Vorbis, and Opus audio files. It outputs binary or JSON waveform data and renders PNG waveform images at configurable zoom levels.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install audiowaveform
- docker pull realies/audiowaveform
- make
- make install

Requirements and caveats from upstream:
- ### Docker
- A Docker image based on Alpine Linux is available [here](https://hub.docker.com/r/realies/audiowaveform),
- alias awf='docker run --rm -v pwd:/tmp -w /tmp realies/audiowaveform'

Basic usage or getting-started notes:
- ![Example Waveform](/doc/example.png "Example Waveform")
- [Usage](#usage)
- ### Ubuntu

- Source: https://github.com/bbc/audiowaveform
- Extracted from upstream docs: https://raw.githubusercontent.com/bbc/audiowaveform/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audiowaveform-bbc-waveform-generator/)
