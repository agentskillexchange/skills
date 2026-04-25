---
title: "Audio Fingerprint Identifier"
description: "Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
---

# Audio Fingerprint Identifier

The Audio Fingerprint Identifier provides robust audio content recognition using multiple fingerprinting technologies. It generates acoustic fingerprints using the Chromaprint library (fpcalc CLI) and queries the AcoustID API for music identification with MusicBrainz metadata enrichment. For real-time audio recognition, it integrates with the Shazam API (RapidAPI endpoint) providing song title, artist, album, and ISRC codes. The agent also connects to ACRCloud for broadcast monitoring and custom fingerprint database matching. Audio preprocessing uses FFmpeg for sample rate normalization, channel mixing, and segment extraction. The identifier supports continuous monitoring mode for radio/TV streams, detecting music tracks, advertisements, and spoken word segments using energy-based voice activity detection (VAD) via WebRTC VAD. It builds local fingerprint databases using the Dejavu audio fingerprinting library for custom content catalogs. Metadata enrichment pulls from the Spotify Web API, Discogs API, and MusicBrainz API to provide comprehensive track information. Results are stored in PostgreSQL with PostGIS extensions for temporal indexing and exported via CSV or JSON-LD with Schema.org MusicRecording markup.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audio-fingerprint-identifier-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audio-fingerprint-identifier-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/)
