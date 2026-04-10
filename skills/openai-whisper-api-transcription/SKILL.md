---
title: "OpenAI Whisper API Transcription"
description: "API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script."
slug: "openai-whisper-api-transcription"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://developers.openai.com/api/docs/guides/speech-to-text"
---

# OpenAI Whisper API Transcription

API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install openai-whisper-api-transcription
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-whisper-api-transcription/)
