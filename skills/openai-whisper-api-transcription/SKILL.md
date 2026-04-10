---
name: "OpenAI Whisper API Transcription"
description: "API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script."
verification: security_reviewed
source: "https://developers.openai.com/api/docs/guides/speech-to-text"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
---

# OpenAI Whisper API Transcription

This skill wraps OpenAI's hosted transcription endpoint for fast, lightweight audio-to-text. Send audio files and get back plain-text or JSON transcripts with minimal setup.
How it differs from the local Whisper skill
The already-live OpenAI Whisper (local) listing runs the Whisper model directly on your machine using Python and requires downloading model weights and a capable CPU/GPU. This listing uses the hosted API — no model downloads, no local compute requirements, no Python ML dependencies. The tradeoff is API cost and network dependency.
Best for

Meeting recordings and podcast notes
Voice memos and interview transcripts
Any audio-to-text workflow where convenience and speed matter more than running your own model

Install notes
Set your OPENAI_API_KEY environment variable or configure it in OpenClaw skill config. Requires curl (pre-installed on most systems). No other dependencies.
Source: OpenClaw skills/openai-whisper-api

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-whisper-api-transcription/)
