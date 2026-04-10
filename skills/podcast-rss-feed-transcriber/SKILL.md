---
title: "Podcast RSS Feed Transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
slug: "podcast-rss-feed-transcriber"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

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
clawhub install podcast-rss-feed-transcriber
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python’s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation.
Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio’s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment.
Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
