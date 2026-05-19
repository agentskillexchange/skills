---
name: "WhisperX Speech Recognition with Word-Level Timestamps and Diarization"
slug: "whisperx-speech-recognition-timestamps-diarization"
description: "WhisperX extends OpenAI Whisper with batched inference for 70x realtime transcription, phoneme-based word-level timestamp alignment via wav2vec2, voice activity detection, and speaker diarization. It produces accurate per-word timestamps and speaker labels from audio files."
github_stars: 21036
verification: "security_reviewed"
source: "https://github.com/m-bain/whisperX"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "m-bain/whisperX"
  github_stars: 21036
---

# WhisperX Speech Recognition with Word-Level Timestamps and Diarization

WhisperX extends OpenAI Whisper with batched inference for 70x realtime transcription, phoneme-based word-level timestamp alignment via wav2vec2, voice activity detection, and speaker diarization. It produces accurate per-word timestamps and speaker labels from audio files.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install whisperx
- git clone https://github.com/m-bain/whisperX.git
- uv sync --all-extras --dev

Requirements and caveats from upstream:
- 🪶 [faster-whisper](https://github.com/guillaumekln/faster-whisper) backend, requires <8GB gpu memory for large-v2 with beam_size=5
- ## Python usage 🐍
- python

Basic usage or getting-started notes:
- **Phoneme-Based ASR** A suite of models finetuned to recognise the smallest unit of speech distinguishing one word from another, e.g. the element p in "tap". A popular example model is [wav2vec2.0](https://huggingface...
- You may also need to install ffmpeg, rust etc. Follow openAI instructions here https://github.com/openai/whisper#setup.
- <h2 align="left" id="example">Usage 💬 (command line)</h2>

- Source: https://github.com/m-bain/whisperX
- Extracted from upstream docs: https://raw.githubusercontent.com/m-bain/whisperX/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisperx-speech-recognition-timestamps-diarization/)
