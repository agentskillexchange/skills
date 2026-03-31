---
name: "Podcast Transcription Pipeline"
description: "Transcribes podcast episodes using OpenAI Whisper API with speaker diarization via pyannote.audio. Exports formatted transcripts to SRT, VTT, and searchable JSON with timestamped segments."
category: "Media &amp; Transcription"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/"
---
# Podcast Transcription Pipeline

Transcribes podcast episodes using OpenAI Whisper API with speaker diarization via pyannote.audio. Exports formatted transcripts to SRT, VTT, and searchable JSON with timestamped segments.

## Overview

The Podcast Transcription Pipeline provides end-to-end audio transcription for podcast episodes and audio content. It uses the OpenAI Whisper API (whisper-1 model) for high-accuracy speech-to-text conversion with word-level timestamps. Speaker diarization is performed using the pyannote.audio pipeline with pretrained speaker segmentation models, identifying and labeling individual speakers throughout the episode. The agent handles audio preprocessing with FFmpeg for format conversion, noise reduction via SoX noisered, and silence trimming. It supports batch processing of RSS feeds using the podcast index API to automatically fetch new episodes. Output formats include SRT subtitles, WebVTT captions, plain text transcripts, and searchable JSON with segment-level timestamps and speaker labels. The pipeline integrates with Transistor.fm API and Podbean API for automatic transcript attachment to published episodes. It generates chapter markers from topic changes detected via semantic similarity scoring using sentence-transformers embeddings. Includes keyword extraction using spaCy NER and automatic show notes generation summarizing key topics, guest mentions, and referenced resources.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill podcast-transcription-pipeline-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill podcast-transcription-pipeline-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill podcast-transcription-pipeline-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill podcast-transcription-pipeline-agent -a codex
```

### OpenClaw

```bash
clawhub install podcast-transcription-pipeline-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/)
