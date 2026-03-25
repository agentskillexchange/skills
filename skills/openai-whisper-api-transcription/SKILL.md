---
name: "OpenAI Whisper API Transcription"
description: "API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script."
category: "Media & Transcription"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openai-whisper-api-transcription/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "whisper"  # from ase_tool_match
  github_stars: 96530  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/whisper"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAI Whisper API Transcription

API-based speech-to-text transcription through OpenAI. No local model downloads, no GPU, no Python ML stack — just an API key and a shell script.

## Overview

This skill wraps OpenAI’s hosted transcription endpoint for fast, lightweight audio-to-text. Send audio files and get back plain-text or JSON transcripts with minimal setup.

How it differs from the local Whisper skill

The already-live OpenAI Whisper (local) listing runs the Whisper model directly on your machine using Python and requires downloading model weights and a capable CPU/GPU. This listing uses the **hosted API** — no model downloads, no local compute requirements, no Python ML dependencies. The tradeoff is API cost and network dependency.

Best for

Meeting recordings and podcast notes

Voice memos and interview transcripts

Any audio-to-text workflow where convenience and speed matter more than running your own model

Install notes

Set your `OPENAI_API_KEY` environment variable or configure it in OpenClaw skill config. Requires `curl` (pre-installed on most systems). No other dependencies.

**Source:** [OpenClaw skills/openai-whisper-api](https://github.com/openclaw/openclaw/tree/main/skills/openai-whisper-api)

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-api-transcription
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-api-transcription -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-api-transcription -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openai-whisper-api-transcription -a codex
```

### OpenClaw

```bash
clawhub install openai-whisper-api-transcription
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openai-whisper-api-transcription/
