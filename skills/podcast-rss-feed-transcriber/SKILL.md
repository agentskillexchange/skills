---
title: Podcast RSS Feed Transcriber
description: Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast
  feed subscription to searchable transcript generation. It parses RSS feeds using
  Python’s feedparser library, extracts audio enclosure URLs, and downloads episodes
  with proper handling of redirects, CDN authentication tokens, and content-type validation.
  Audio processing routes through either the OpenAI Whisper API for cloud-based transcription
  or local faster-whisper models for privacy-sensitive workflows. The skill automatically
  selects the appropriate Whisper model size based on audio duration and available
  compute resources. Speaker diarization uses pyannote.audio’s pretrained pipeline
  to segment transcripts by speaker, assigning speaker labels to each utterance segment.
  Output formats include timestamped SRT and VTT subtitle files, speaker-attributed
  markdown transcripts, and plain text for full-text search indexing. The transcriber
  maintains a local SQLite database tracking processed episodes to avoid re-transcription.
  For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds
  for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is
  improved through post-processing that corrects common Whisper errors using a custom
  dictionary of domain-specific terms.
verification: security_reviewed
source: https://github.com/openai/whisper
category:
- Media &amp; Transcription
framework:
- OpenClaw
tool_ecosystem:
  github_repo: openai/whisper
  github_stars: 97065
---

# Podcast RSS Feed Transcriber

Podcast RSS Feed Transcriber automates the end-to-end workflow from podcast feed subscription to searchable transcript generation. It parses RSS feeds using Python’s feedparser library, extracts audio enclosure URLs, and downloads episodes with proper handling of redirects, CDN authentication tokens, and content-type validation. Audio processing routes through either the OpenAI Whisper API for cloud-based transcription or local faster-whisper models for privacy-sensitive workflows. The skill automatically selects the appropriate Whisper model size based on audio duration and available compute resources. Speaker diarization uses pyannote.audio’s pretrained pipeline to segment transcripts by speaker, assigning speaker labels to each utterance segment. Output formats include timestamped SRT and VTT subtitle files, speaker-attributed markdown transcripts, and plain text for full-text search indexing. The transcriber maintains a local SQLite database tracking processed episodes to avoid re-transcription. For ongoing podcast monitoring, it runs on a configurable schedule, checking feeds for new episodes via ETag and Last-Modified HTTP headers. Transcript quality is improved through post-processing that corrects common Whisper errors using a custom dictionary of domain-specific terms.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-transcriber/)
