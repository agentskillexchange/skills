---
name: "Podcast RSS Feed Transcriber"
description: "Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio."
category: "Media & Transcription"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/openai/whisper"
tool_ecosystem:
  tool: whisper
  github_repo: openai/whisper
  github_stars: 97065
---
# Podcast RSS Feed Transcriber

Automatically fetches podcast episodes from RSS feeds using feedparser, downloads audio enclosures, and transcribes them through OpenAI Whisper API or local faster-whisper models. Generates timestamped SRT files and searchable markdown transcripts with speaker diarization via pyannote.audio.

## Overview

Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python’s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation.

Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio’s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment.

Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-transcriber
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-transcriber -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-transcriber -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-transcriber -a codex
```

### OpenClaw

```bash
clawhub install podcast-rss-feed-transcriber
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
