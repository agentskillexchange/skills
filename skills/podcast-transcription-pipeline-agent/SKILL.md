---
title: "Podcast Transcription Pipeline"
description: "The Podcast Transcription Pipeline provides end-to-end audio transcription for podcast episodes and audio content. It uses the OpenAI Whisper API (whisper-1 model) for high-accuracy speech-to-text conversion with word-level timestamps. Speaker diarization is performed using the pyannote.audio pipeline with pretrained speaker segmentation models, identifying and labeling individual speakers throughout the episode. The agent handles audio preprocessing with FFmpeg for format conversion, noise reduction via SoX noisered, and silence trimming. It supports batch processing of RSS feeds using the podcast index API to automatically fetch new episodes. Output formats include SRT subtitles, WebVTT captions, plain text transcripts, and searchable JSON with segment-level timestamps and speaker labels. The pipeline integrates with Transistor.fm API and Podbean API for automatic transcript attachment to published episodes. It generates chapter markers from topic changes detected via semantic similarity scoring using sentence-transformers embeddings. Includes keyword extraction using spaCy NER and automatic show notes generation summarizing key topics, guest mentions, and referenced resources."
source: "https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Codex"
---

# Podcast Transcription Pipeline

The Podcast Transcription Pipeline provides end-to-end audio transcription for podcast episodes and audio content. It uses the OpenAI Whisper API (whisper-1 model) for high-accuracy speech-to-text conversion with word-level timestamps. Speaker diarization is performed using the pyannote.audio pipeline with pretrained speaker segmentation models, identifying and labeling individual speakers throughout the episode. The agent handles audio preprocessing with FFmpeg for format conversion, noise reduction via SoX noisered, and silence trimming. It supports batch processing of RSS feeds using the podcast index API to automatically fetch new episodes. Output formats include SRT subtitles, WebVTT captions, plain text transcripts, and searchable JSON with segment-level timestamps and speaker labels. The pipeline integrates with Transistor.fm API and Podbean API for automatic transcript attachment to published episodes. It generates chapter markers from topic changes detected via semantic similarity scoring using sentence-transformers embeddings. Includes keyword extraction using spaCy NER and automatic show notes generation summarizing key topics, guest mentions, and referenced resources.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/)
