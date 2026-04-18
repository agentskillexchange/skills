---
title: "Podcast RSS Feed Audio Normalizer"
description: "Parses podcast RSS feeds with feedparser and normalizes audio loudness to -16 LUFS broadcast standard using ffmpeg loudnorm filter with dual-pass EBU R128 analysis. Integrates with Podbean API and Buzzsprout API for automated episode re-upload."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/"
category:
  - "Media & Transcription"
framework:
  - "MCP"
---

# Podcast RSS Feed Audio Normalizer

Overview The Podcast RSS Feed Audio Normalizer ensures consistent listening experiences across podcast episodes by standardizing audio loudness levels to broadcast specifications. It processes episodes from RSS feeds and re-uploads normalized audio to podcast hosting platforms automatically.

Key Capabilities This skill parses podcast RSS feeds using Python’s feedparser library to discover and download episode audio files. It applies the FFmpeg loudnorm filter in dual-pass mode for EBU R128 compliant loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP true peak limiting to prevent clipping on consumer devices.

Platform Integration Integrates with the Podbean API and Buzzsprout API for automated episode re-upload after normalization, preserving original metadata including episode titles, descriptions, chapter markers, and artwork. Supports batch processing of back-catalog episodes with parallel download and encoding queues, and generates before/after loudness comparison reports using ffmpeg astats filter measurements for quality verification.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/podcast-rss-feed-audio-normalizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/podcast-rss-feed-audio-normalizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/)
