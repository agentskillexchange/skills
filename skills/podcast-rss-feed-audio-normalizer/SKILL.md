---
title: Podcast RSS Feed Audio Normalizer
description: Overview The Podcast RSS Feed Audio Normalizer ensures consistent listening
  experiences across podcast episodes by standardizing audio loudness levels to broadcast
  specifications. It processes episodes from RSS feeds and re-uploads normalized audio
  to podcast hosting platforms automatically. Key Capabilities This skill parses podcast
  RSS feeds using Python’s feedparser library to discover and download episode audio
  files. It applies the FFmpeg loudnorm filter in dual-pass mode for EBU R128 compliant
  loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP
  true peak limiting to prevent clipping on consumer devices. Platform Integration
  Integrates with the Podbean API and Buzzsprout API for automated episode re-upload
  after normalization, preserving original metadata including episode titles, descriptions,
  chapter markers, and artwork. Supports batch processing of back-catalog episodes
  with parallel download and encoding queues, and generates before/after loudness
  comparison reports using ffmpeg astats filter measurements for quality verification.
verification: security_reviewed
source: https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/
category:
- Media &amp; Transcription
framework:
- MCP
---

# Podcast RSS Feed Audio Normalizer

Overview The Podcast RSS Feed Audio Normalizer ensures consistent listening experiences across podcast episodes by standardizing audio loudness levels to broadcast specifications. It processes episodes from RSS feeds and re-uploads normalized audio to podcast hosting platforms automatically. Key Capabilities This skill parses podcast RSS feeds using Python’s feedparser library to discover and download episode audio files. It applies the FFmpeg loudnorm filter in dual-pass mode for EBU R128 compliant loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP true peak limiting to prevent clipping on consumer devices. Platform Integration Integrates with the Podbean API and Buzzsprout API for automated episode re-upload after normalization, preserving original metadata including episode titles, descriptions, chapter markers, and artwork. Supports batch processing of back-catalog episodes with parallel download and encoding queues, and generates before/after loudness comparison reports using ffmpeg astats filter measurements for quality verification.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/)
