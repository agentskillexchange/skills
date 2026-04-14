---
title: "Podcast RSS Feed Audio Normalizer"
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
This skill parses podcast RSS feeds using Python’s feedparser library to discover and download episode audio files. It applies the FFmpeg loudnorm filter in dual-pass mode for EBU R128 compliant loudness normalization, targeting -16 LUFS for podcast distribution with -1 dBTP true peak limiting to prevent clipping on consumer devices.

Platform Integration
Integrates with the Podbean API and Buzzsprout API for automated episode re-upload after normalization, preserving original metadata including episode titles, descriptions, chapter markers, and artwork. Supports batch processing of back-catalog episodes with parallel download and encoding queues, and generates before/after loudness comparison reports using ffmpeg astats filter measurements for quality verification.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-audio-normalizer/)
