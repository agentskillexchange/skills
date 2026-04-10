---
title: "Audio Fingerprint Identifier"
description: "Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases."
slug: "audio-fingerprint-identifier-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/"
---

# Audio Fingerprint Identifier

Identifies audio content using Chromaprint/AcoustID fingerprinting, Shazam API recognition, and ACRCloud monitoring. Matches music, speech, and ambient audio against fingerprint databases.

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
clawhub install audio-fingerprint-identifier-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Audio Fingerprint Identifier provides robust audio content recognition using multiple fingerprinting technologies. It generates acoustic fingerprints using the Chromaprint library (fpcalc CLI) and queries the AcoustID API for music identification with MusicBrainz metadata enrichment. For real-time audio recognition, it integrates with the Shazam API (RapidAPI endpoint) providing song title, artist, album, and ISRC codes. The agent also connects to ACRCloud for broadcast monitoring and custom fingerprint database matching. Audio preprocessing uses FFmpeg for sample rate normalization, channel mixing, and segment extraction. The identifier supports continuous monitoring mode for radio/TV streams, detecting music tracks, advertisements, and spoken word segments using energy-based voice activity detection (VAD) via WebRTC VAD. It builds local fingerprint databases using the Dejavu audio fingerprinting library for custom content catalogs. Metadata enrichment pulls from the Spotify Web API, Discogs API, and MusicBrainz API to provide comprehensive track information. Results are stored in PostgreSQL with PostGIS extensions for temporal indexing and exported via CSV or JSON-LD with Schema.org MusicRecording markup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audio-fingerprint-identifier-agent/)
