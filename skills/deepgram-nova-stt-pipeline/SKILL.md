---
name: "Deepgram Nova STT Pipeline"
description: "Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows."
category: "Media & Transcription"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58283  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Deepgram Nova STT Pipeline

Real-time speech-to-text using Deepgram Nova-2 API with streaming WebSocket connections. Supports diarization, punctuation, and language detection via the Deepgram Python SDK for podcast and meeting transcription workflows.

## Overview

Automate speech-to-text transcription using the Deepgram Nova-2 model via their streaming WebSocket API. This skill connects to the Deepgram Python SDK (deepgram-sdk) to process audio files and live audio streams into accurate text transcripts.

Key capabilities include multi-speaker diarization for meeting recordings, automatic punctuation restoration, and real-time interim results for live captioning. The skill supports over 30 languages with automatic language detection.

Configuration options include model selection (nova-2, nova, enhanced, base), sample rate settings, encoding formats (linear16, flac, opus), and callback URLs for async processing. The pipeline handles chunked audio uploads for large files, with automatic retry logic and rate limit management against the Deepgram REST API.

Output formats include plain text, SRT subtitles, VTT captions, and structured JSON with word-level timestamps. Integrates with FFmpeg for audio preprocessing and format conversion before submission to the Deepgram endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-stt-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-stt-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-stt-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill deepgram-nova-stt-pipeline -a codex
```

### OpenClaw

```bash
clawhub install deepgram-nova-stt-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/deepgram-nova-stt-pipeline/
