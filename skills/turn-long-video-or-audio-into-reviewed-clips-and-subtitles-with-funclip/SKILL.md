---
name: "Turn long video or audio into reviewed clips and subtitles with FunClip"
slug: "turn-long-video-or-audio-into-reviewed-clips-and-subtitles-with-funclip"
description: "Use FunClip when an agent needs a repeatable local workflow for transcribing media, proposing clip timestamps, and producing reviewable video segments with subtitle files."
github_stars: 5878
verification: "security_reviewed"
source: "https://github.com/modelscope/FunClip"
author: "ModelScope / FunASR"
publisher_type: "open-source"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "modelscope/FunClip"
  github_stars: 5878
---

# Turn long video or audio into reviewed clips and subtitles with FunClip

Use FunClip when an agent needs a repeatable local workflow for transcribing media, proposing clip timestamps, and producing reviewable video segments with subtitle files.

## Prerequisites

Python environment, FunClip source checkout, FunASR-supported models, local or server Gradio runtime, and media files to transcribe and clip.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/alibaba-damo-academy/FunClip.git
- pip install -r ./requirements.txt
- brew install imagemagick

Requirements and caveats from upstream:
- 2026/05/20 FunClip now supports Fun-ASR-Nano and SenseVoice models. Fun-ASR-Nano provides higher accuracy for 31 languages; SenseVoice adds emotion recognition and audio event detection. Run python funclip/launch.py -...
- 2024/06/12 FunClip supports recognize and clip English audio files now. Run python funclip/launch.py -l en to try.
- [x] FunClip will support Whisper model for English users, coming soon (ASR using Whisper with timestamp requires massive GPU memory, we support timestamp prediction for vanilla Paraformer in FunASR to achieving this).

Basic usage or getting-started notes:
- ｜<a href="#Usage"> Usage </a>
- 🔥2024/05/13 FunClip v2.0.0 now supports smart clipping with large language models, integrating models from the qwen series, GPT series, etc., providing default prompts. You can also explore and share tips for setting...
- cd FunClip

- Source: https://github.com/modelscope/FunClip
- Extracted from upstream docs: https://raw.githubusercontent.com/modelscope/FunClip/HEAD/README.md

## Documentation

- https://github.com/modelscope/FunClip

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-long-video-or-audio-into-reviewed-clips-and-subtitles-with-funclip/)
