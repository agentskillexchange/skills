---
name: "Podcast RSS Feed Audio Normalizer"
description: "Parses podcast RSS feeds with feedparser and normalizes audio loudness to -16 LUFS broadcast standard using ffmpeg loudnorm filter with dual-pass EBU R128 analysis. Integrates with Podbean API and Buzzsprout API for automated episode re-upload."
category: "Media & Transcription"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/"
tool_ecosystem:
  tool: "ffmpeg"
  github_stars: 58283
  github_repo: "FFmpeg/FFmpeg"
  maintained: true
---

# Podcast RSS Feed Audio Normalizer

Parses podcast RSS feeds with feedparser and normalizes audio loudness to -16 LUFS broadcast standard using ffmpeg loudnorm filter with dual-pass EBU R128 analysis. Integrates with Podbean API and Buzzsprout API for automated episode re-upload.

## Overview

Overview

The Podcast RSS Feed Audio Normalizer ensures consistent listening experiences across podcast episodes by standardizing audio loudness levels to broadcast specifications. It processes episodes from RSS feeds and re-uploads normalized audio to podcast hosting platforms automatically.

Key Capabilities

This skill parses podcast RSS feeds using Python’s `feedparser` library to discover and download episode audio files. It applies the FFmpeg `loudnorm` filter in dual-pass mode for EBU R128 compliant loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP true peak limiting to prevent clipping on consumer devices.

Platform Integration

Integrates with the `Podbean API` and `Buzzsprout API` for automated episode re-upload after normalization, preserving original metadata including episode titles, descriptions, chapter markers, and artwork. Supports batch processing of back-catalog episodes with parallel download and encoding queues, and generates before/after loudness comparison reports using `ffmpeg astats` filter measurements for quality verification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-audio-normalizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-audio-normalizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-audio-normalizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill podcast-rss-feed-audio-normalizer -a codex
```

### OpenClaw

```bash
clawhub install podcast-rss-feed-audio-normalizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/
