---
title: "Podcast RSS Feed Transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/podcast-rss-feed-transcriber
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/podcast-rss-feed-transcriber`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
