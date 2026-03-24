---
name: "AssemblyAI Audio Intelligence Agent"
description: "Extract structured intelligence from audio using the AssemblyAI API with sentiment analysis, entity detection, topic modeling, and auto-chapter generation. Uses the assemblyai Python SDK for transcript processing pipelines."
category: "Media & Transcription"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/"
---

# AssemblyAI Audio Intelligence Agent

Extract structured intelligence from audio using the AssemblyAI API with sentiment analysis, entity detection, topic modeling, and auto-chapter generation. Uses the assemblyai Python SDK for transcript processing pipelines.

## Overview

Analyze audio content using AssemblyAI’s Audio Intelligence models to extract structured data beyond basic transcription. This skill leverages the AssemblyAI API v2 for advanced audio analysis workflows.

The transcription pipeline uploads audio via POST /v2/upload, creates transcript jobs with audio_intelligence features enabled, and polls for completion. Supported intelligence models include sentiment analysis per utterance, entity detection (PII, names, locations, monetary amounts), topic detection using the IAB taxonomy, and auto-chapter generation with summary headlines.

Speaker diarization identifies individual speakers and labels utterances for meeting transcript formatting. Content safety detection flags sensitive topics across configurable severity thresholds. PII redaction can be applied to both text output and audio files with configurable entity types.

The assemblyai Python SDK (v0.20+) provides high-level wrappers for the REST API with automatic polling and webhook support. Real-time transcription uses WebSocket streaming for live audio feeds with interim result callbacks.

Batch processing handles multiple files with parallel job submission and result aggregation into structured JSON or SRT output formats. Rate limit management includes automatic throttling and retry logic for the 200 concurrent transcript limit.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill assemblyai-audio-intelligence-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill assemblyai-audio-intelligence-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill assemblyai-audio-intelligence-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill assemblyai-audio-intelligence-agent -a codex
```

### OpenClaw

```bash
clawhub install assemblyai-audio-intelligence-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/assemblyai-audio-intelligence-agent/
