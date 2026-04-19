---
title: "Podcast RSS Feed Transcriber"
description: "Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python&#8217;s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation. Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio&#8217;s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment. Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms."
source: "https://github.com/openai/whisper"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97391
---

# Podcast RSS Feed Transcriber

Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python&#8217;s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation. Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio&#8217;s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment. Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
