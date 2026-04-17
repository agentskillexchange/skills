---
title: "Podcast RSS Feed Transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python’s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation.

Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio’s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment.

Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/podcast-rss-feed-transcriber
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/podcast-rss-feed-transcriber` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
