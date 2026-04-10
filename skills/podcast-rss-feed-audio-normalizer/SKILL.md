---
name: "Podcast RSS Feed Audio Normalizer"
description: "Parses podcast RSS feeds with feedparser and normalizes audio loudness to -16 LUFS broadcast standard using ffmpeg loudnorm filter with dual-pass EBU R128 analysis. Integrates with Podbean API and Buzzsprout API for automated episode re-upload."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/"
category:
  - "Media &amp; Transcription"
framework:
  - "MCP"
---

# Podcast RSS Feed Audio Normalizer

Overview
The Podcast RSS Feed Audio Normalizer ensures consistent listening experiences across podcast episodes by standardizing audio loudness levels to broadcast specifications. It processes episodes from RSS feeds and re-uploads normalized audio to podcast hosting platforms automatically.
Key Capabilities
This skill parses podcast RSS feeds using Python's feedparser library to discover and download episode audio files. It applies the FFmpeg loudnorm filter in dual-pass mode for EBU R128 compliant loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP true peak limiting to prevent clipping on consumer devices.
Platform Integration
Integrates with the Podbean API and Buzzsprout API for automated episode re-upload after normalization, preserving original metadata including episode titles, descriptions, chapter markers, and artwork. Supports batch processing of back-catalog episodes with parallel download and encoding queues, and generates before/after loudness comparison reports using ffmpeg astats filter measurements for quality verification.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/)
