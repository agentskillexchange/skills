---
name: "Podcast Transcription Pipeline"
description: "Transcribes podcast episodes using OpenAI Whisper API with speaker diarization via pyannote.audio. Exports formatted transcripts to SRT, VTT, and searchable JSON with timestamped segments."
category: "Media & Transcription"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96570  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/podcast-transcription-pipeline-agent/
