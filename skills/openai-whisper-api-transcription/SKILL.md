---
title: "OpenAI Whisper API Transcription"
description: "API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script."
verification: "security_reviewed"
source: "https://developers.openai.com/api/docs/guides/speech-to-text"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# OpenAI Whisper API Transcription

This skill wraps OpenAI’s hosted transcription endpoint for fast, lightweight audio-to-text. Send audio files and get back plain-text or JSON transcripts with minimal setup.

How it differs from the local Whisper skill
The already-live OpenAI Whisper (local) listing runs the Whisper model directly on your machine using Python and requires downloading model weights and a capable CPU/GPU. This listing uses the hosted API — no model downloads, no local compute requirements, no Python ML dependencies. The tradeoff is API cost and network dependency.

Best for

- Meeting recordings and podcast notes

- Voice memos and interview transcripts

- Any audio-to-text workflow where convenience and speed matter more than running your own model

Install notes
Set your OPENAI_API_KEY environment variable or configure it in OpenClaw skill config. Requires curl (pre-installed on most systems). No other dependencies.

Source: OpenClaw skills/openai-whisper-api

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/openai-whisper-api-transcription/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openai-whisper-api-transcription
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/openai-whisper-api-transcription`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-whisper-api-transcription/)
