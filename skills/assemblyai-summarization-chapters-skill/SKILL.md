---
name: "AssemblyAI Summarization & Chapters Skill"
description: "Transcribes audio and generates auto-chapters with summaries using AssemblyAI's /v2/transcript endpoint with auto_chapters=true. Extracts key topics, sentiment analysis, and content safety labels via AssemblyAI SDK."
category: "Media &amp; Transcription"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/"
---
# AssemblyAI Summarization & Chapters Skill

Transcribes audio and generates auto-chapters with summaries using AssemblyAI's /v2/transcript endpoint with auto_chapters=true. Extracts key topics, sentiment analysis, and content safety labels via AssemblyAI SDK.

## Overview

This skill integrates with AssemblyAI's transcription and audio intelligence API to provide comprehensive audio analysis beyond basic transcription. It uses the AssemblyAI Python SDK: client = assemblyai.Client(api_key=key) and initiates transcription via transcript = client.transcribe(audio_url, config=TranscriptionConfig(auto_chapters=True, sentiment_analysis=True, content_safety=True, entity_detection=True)). The auto_chapters feature automatically segments audio into topical chapters with gist, headline, and summary for each segment, along with start/end timestamps. Sentiment analysis provides per-sentence sentiment labels (POSITIVE, NEGATIVE, NEUTRAL) with confidence scores. Content safety detection flags sensitive content categories (profanity, violence, drugs, etc.) with severity scores and timestamp ranges. Entity detection identifies and categorizes PII including names, locations, organizations, dates, and phone numbers using the entity_detection parameter. The skill supports webhook callbacks via webhook_url parameter for async processing of long recordings. It handles file uploads using client.upload(local_path) for local files and accepts direct URLs for cloud-hosted audio. Rate limiting is managed with exponential backoff on 429 responses. Output is structured as JSON with sections for full transcript, chapters array, sentiment timeline, detected entities, and content safety report.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill assemblyai-summarization-chapters-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill assemblyai-summarization-chapters-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill assemblyai-summarization-chapters-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill assemblyai-summarization-chapters-skill -a codex
```

### OpenClaw

```bash
clawhub install assemblyai-summarization-chapters-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemblyai-summarization-chapters-skill/)
